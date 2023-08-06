#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging.config
import logging
import os
import argparse
import json
import sys
import importlib
from shlex import split, quote
import subprocess
import signal

import yaml

from unicorncommon.server_status import SERVER_STATUS
from unicorncommon.dbagent_client import DBAgentException, DBAgentClient

def get_yaml_config(cfg_dir, filename):
    full_path = os.path.join(cfg_dir, filename)
    with open(full_path, "r") as f:
        return yaml.safe_load(f)

#############################################################
# pwrapper exit code
# 0: everything is ok
# 1: unable to get run details
# 2: unable to create output file for child process
# 3: unable to launch child process
# 4: unable to set run to started after child process is launched
# 5: unable to remove the task singleton lock after process is terminated
# 6: unable to remove set run to finished after process is terminated.
# 20: both 5 and 6
#############################################################

APP_CTX = { }
def shutdown_handler(logger):
    def handler(signal_umber, frame):
        _, _ = signal_umber, frame
        child_process = APP_CTX.get('child_process')
        if not child_process:
            logger.info("shutdown_handler: ignored since no child process found")
            return
        logger.info(f"shutdown_handler: send SIGTERM to process {child_process.pid}")
        child_process.terminate()
    return handler

def json_2_str(obj):
    return json.dumps(obj, indent=4, separators=(',', ': '))


def get_dbagent_client(cfg_dir):
    dbagent_client_cfg = get_yaml_config(cfg_dir, "dbagent_client.yaml")

    classname   = dbagent_client_cfg['classname']
    module      = importlib.import_module('.'.join(classname.split(".")[:-1]))
    klass       = getattr(module, classname.split('.')[-1])
    server_endpoint = dbagent_client_cfg['server_endpoint']
    config      = dbagent_client_cfg['config']
    dbagent_client = klass(server_endpoint, config)
    return dbagent_client

def get_path(path):
    if path is None:
        return None
    path = path.strip()
    if len(path) == 0:
        return None
    return os.path.expandvars(path)

def generate_execute_command(application, args):
    cmd = ""

    venv_dir = get_path(application.get('venv_dir'))
    if venv_dir is not None:
        # if the application has venv_dir, we need to activate virtual environment
        cmd += f"source {os.path.join(venv_dir, 'bin', 'activate')}\n"

    entry = application['entry']
    if entry.endswith(".py"):
        cmd_line = f"python {entry}"
    else:
        cmd_line = f"{entry}"
    for arg in args:
        cmd_line += f" {quote(arg)}"
    cmd += f"{cmd_line}\n"
    return cmd


def main():
    parser = argparse.ArgumentParser(
        description='Process Wrapper for Unicorn Cluster Manager'
    )
    parser.add_argument(
        "-r", "--run-id", type=str, required=True, help="Specify the run id for the wrapper"
    )
    parser.add_argument(
        "--data-dir", type=str, required=True, help="Specify the data directory"
    )
    parser.add_argument(
        "--cfg-dir", type=str, required=True, help="Specify the config directory"
    )
    args = parser.parse_args()

    run_id = int(args.run_id)
    run_dir = os.path.join(args.data_dir, "runs", str(run_id))
    cfg_dir = args.cfg_dir

    logging.config.dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": f"{run_dir}/pwrapper.log",
            },
        },
        "loggers": {
            "": {
                "handlers": ["fileHandler"],
                "level":    "DEBUG",
                "propagate": True
            },
        },
        "root": {
            "handlers": ["fileHandler"],
            "level": "DEBUG",
        },
    })

    logger = logging.getLogger(__name__)
    logger.info("main: enter")
    logger.info(f"run_id : {run_id}")
    logger.info(f"run_dir: {run_dir}")
    logger.info(f"cfg_dir: {cfg_dir}")

    # get dbagent client
    dbagent_client = DBAgentClient(get_dbagent_client(cfg_dir), logger=logger)

    try:
        run = dbagent_client.get_run(run_id)
    except DBAgentException as e:
        logger.info(f"main: unable to get run info, erro: {str(e)}")
        logger.info("main: exit")
        sys.exit(1)

    logger.info(f"main: run loaded\n{json_2_str(run)}\n")
    application = run['application']
    task = run['task']
    app_args = json.loads(run['args'])
    cmd = generate_execute_command(application, app_args)
    logger.info(f"main: generate command: cmd={cmd}")

    # create output file
    out_f = None
    filename = os.path.join(run_dir, "out.txt")
    try:
        out_f = open(filename, "wb")
        logger.info(f"main: output file {filename} is generated")
    except OSError:
        logger.warn(f"main: unable to create output file, error: {str(e)}")
        logger.info("main: exit")
        sys.exit(2)

    home_dir = get_path(application.get("home_dir"))
    try:
        child_process = subprocess.Popen(
            cmd,
            cwd = home_dir,
            shell = True,
            stdin = subprocess.DEVNULL,
            stdout = out_f,
            stderr = subprocess.STDOUT
        )
        launched = True
        logger.info(f"main: process launched, pid={child_process.pid}")
    except OSError as e:
        logger.exception(f"main: failed to launch process, error: {str(e)}")
        logger.info("main: exit")
        sys.exit(-1)
    finally:
        if out_f is not None:
            try:
                out_f.close()
            except OSError as e:
                logger.warn(f"main: unable to close output file, error: {str(e)}")

    try:
        dbagent_client.set_run_started(run_id)
    except DBAgentException as e:
        logger.info(f"main: unable to get set run to active, erro: {str(e)}")
        logger.info(f"main: terminate child process")
        child_process.terminate()
        child_process.wait()
        logger.info("main: exit")
        sys.exit(4)

    APP_CTX['child_process'] = child_process
    old_term_handler = signal.signal(signal.SIGTERM, shutdown_handler(logger))
    child_process.wait()

    # restore the old signal handler for kill since the child process is already finished
    signal.signal(signal.SIGTERM, old_term_handler)

    # need to set run to stopped
    exit_code = 0
    if task is not None and task['is_singleton']:
        try:
            dbagent_client.unset_active_run(task['id'])
            logger.info(f"main: unset_active_run({task['id']}) succeeded")
        except DBAgentException as e:
            logger.info(f"main: unset_active_run({task['id']}) failed")
            exit_code = 5
    try:
        dbagent_client.set_run_finished(run_id, exit_code=child_process.returncode)
        logger.info(f"main: set_run_finished({run_id}, exit_code={child_process.returncode}) succeeded")
    except DBAgentException as e:
        exit_code += 1
        logger.info(f"main: set_run_finished({run_id}, exit_code={child_process.returncode}) failed")
        if exit_code == 0:
            exit_code = 6
        else:
            exit_code = 20

    logger.info("main: exit")
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
