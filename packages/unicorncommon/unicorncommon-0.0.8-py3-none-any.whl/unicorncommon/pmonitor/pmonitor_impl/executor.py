import logging
logger = logging.getLogger(__name__)

import os
import subprocess
import signal
from datetime import datetime, timedelta
from shlex import split, quote

from jsonschema.exceptions import ValidationError

from unicorncommon.server_status import SERVER_STATUS
from .api_input import validate_model
from unicorncommon.dbagent_client import DBAgentException


class Executor:
    def __init__(self, *, dbagent_client, base_data_dir, node_id, cfg_dir):
        self.base_data_dir  = base_data_dir
        self.node_id        = node_id
        self.dbagent_client = dbagent_client
        self.cfg_dir        = cfg_dir

        self.runs_dir = os.path.join(self.base_data_dir, "runs")

    def on_idle(self):
        pass

    def handle_request_run_application(self, request):
        # request example
        # {
        #     "action": "run-application",
        #     "id": 123,
        #     "args": ["foo", "bar"]
        # }
        try:
            validate_model('run_application_input', request)
        except ValidationError:
            logger.warn("handle_request_run_application: validation error, schema: run_application_input")
            return {
                "status": SERVER_STATUS.INVALID_REQUEST_SCHEMA.value,
                "message": str(e)
            }

        application_id = request["id"]
        args = request.get('args', [])
        run = None
        launched = False
        try:
            try:
                run = self.dbagent_client.create_run(
                    application_id = application_id,
                    node_id = self.node_id,
                    args = args
                )
            except DBAgentException as e:
                logger.warn("handle_request_run_application: unable to create run")
                return {"status": e.respp["status"]}

            run_dir = os.path.join(self.runs_dir, str(run['id']))
            try:
                os.makedirs(run_dir)
            except OSError as e:
                logger.error(f"handle_request_run_application: unable to create run directory {run_dir}, error: {str(e)}")
                return {
                    "status": SERVER_STATUS.INTERNAL_ERROR.value,
                }

            try:
                r = subprocess.Popen(
                    f"pwrapper -r {run['id']} --data-dir {self.base_data_dir} --cfg-dir {self.cfg_dir}",
                    shell = True,
                )
                launched = True
                logger.info(f"handle_request_run_application: wrapper launched for Run(id={run['id']}), pid={r.pid}")
            except OSError as e:
                logger.exception(f"handle_request_run_application: process launch failed for Run(id={run['id']}), error: {str(e)}")
                return {
                    "status": SERVER_STATUS.LAUNCH_PROCESS_FAILED.value,
                    "message": str(e)
                }

            # successfully launched
            return {
                "status": SERVER_STATUS.OK.value,
                "run_id": run['id']
            }
        finally:
            if not launched:
                logger.info(f"handle_request_run_application: cleanup on launch failure!")
                if run is not None:
                    try:
                        self.dbagent_client.delete_run(run['id'])
                        logger.warn(f"handle_request_run_application: unset_active_run({task['id']}) succeeded")
                    except DBAgentException as e:
                        # dounle error, absorb it
                        logger.warn(f"handle_request_run_application: unset_active_run({task['id']}) failed")


    # execute an application using task
    def handle_request_run_task(self, request):
        # request example
        # {
        #     "action": "run-task",
        #     "id": 123,
        # }
        try:
            validate_model('run_task_input', request)
        except ValidationError as e:
            logger.warn("handle_request_run_task: validation error, schema: run_task_input")
            return {
                "status": SERVER_STATUS.INVALID_REQUEST_SCHEMA.value,
                "message": str(e)
            }

        task_id = request["id"]
        try:
            task = self.dbagent_client.get_task(task_id)
        except DBAgentException as e:
            logger.warn("handle_request_run_task: unable to get task, task_id={task_id}")
            return {"status": e.respp["status"]}

        application = task["application"]
        run = None
        active_run_set = False
        launched = False
        try:
            try:
                run = self.dbagent_client.create_run(
                    application_id = application['id'],
                    node_id = self.node_id,
                    args = task['args'],
                    task_id = task['id']
                )
            except DBAgentException as e:
                logger.warn("handle_request_run_task: create_run failed")
                return {"status": e.respp["status"]}

            if task['is_singleton']:
                try:
                    self.dbagent_client.set_active_run(task['id'], run_id = run['id'])
                    active_run_set = True
                except DBAgentException as e:
                    logger.warn("handle_request_run_task: set_active_run failed")
                    return {"status": e.respp["status"]}

            run_dir = os.path.join(self.runs_dir, str(run['id']))
            try:
                os.makedirs(run_dir)
            except OSError as e:
                logger.error(f"handle_request_run_task: unable to create run directory {run_dir}, error: {str(e)}")
                return {
                    "status": SERVER_STATUS.INTERNAL_ERROR.value,
                }

            try:
                r = subprocess.Popen(
                    f"pwrapper -r {run['id']} --data-dir {self.base_data_dir} --cfg-dir {self.cfg_dir}",
                    shell = True,
                )
                launched = True
                logger.info(f"handle_request_run_task: wrapper launched for Run(id={run['id']}), pid={r.pid}")
            except OSError as e:
                logger.exception(f"handle_request_run_task: process launch failed for Run(id={run['id']}), error: {str(e)}")
                return {
                    "status": SERVER_STATUS.LAUNCH_PROCESS_FAILED.value,
                    "message": str(e)
                }

            # successfully launched
            return {
                "status": SERVER_STATUS.OK.value,
                "run_id": run['id']
            }
        finally:
            if not launched:
                logger.info(f"handle_request_run_task: cleanup on launch failure!")
                if active_run_set:
                    try:
                        self.dbagent_client.unset_active_run(task['id'])
                        logger.warn(f"handle_request_run_task: unset_active_run({task['id']}) succeeded")
                    except DBAgentException as e:
                        # dounle error, absorb it
                        logger.warn(f"handle_request_run_task: unset_active_run({task['id']}) failed")
                if run is not None:
                    try:
                        self.dbagent_client.delete_run(run['id'])
                        logger.warn(f"handle_request_run_task: delete_run({run['id']}) succeeded")
                    except DBAgentException as e:
                        # dounle error, absorb it
                        logger.warn(f"handle_request_run_task: delete_run({run['id']}) failed")


    def handle_request_stop_run(self, request):
        # request example
        # {
        #     "action": "stop-run",
        #     "id": 123,
        # }
        try:
            validate_model('stop_run_input', request)
        except ValidationError as e:
            logger.warn("handle_request_stop_run: validation error, schema: stop_run_input")
            return {
                "status": SERVER_STATUS.INVALID_REQUEST_SCHEMA.value,
                "message": str(e)
            }

        id = request["id"]
        try:
            run = self.dbagent_client.get_run(id)
        except DBAgentException as e:
            logger.warn("handle_request_stop_run: unable to get run, run_id={id}")
            return {"status": e.respp["status"]}

        if run["is_finished"]:
            logger.error(f"handle_request_stop_run: Run(id={id}) is already stopped")
            return {
                "status": SERVER_STATUS.RUN_ALREADY_STOPPED.value,
            }

        if run["pid"] is None:
            logger.error(f"handle_request_stop_run: Run(id={id}) is missing pid")
            return {
                "status": SERVER_STATUS.INTERNAL_ERROR.value,
            }

        try:
            os.kill(run["pid"], signal.SIGTERM)
        except OSError as e:
            logger.exception(f"handle_request_stop_run: failed to send SIGTERM to process for Run(id={run['id']}, pid={run['pid']})")
            return {
                "status": SERVER_STATUS.STOP_PROCESS_FAILED.value,
                "message": str(e)
            }

        return {
            "status": SERVER_STATUS.OK.value,
        }


    def handle_request(self, request):
        logger.info(f"request: {request}")
        action = request.get('action')
        if action == "run-application":
            response = self.handle_request_run_application(request)
        elif action == "run-task":
            response = self.handle_request_run_task(request)
        elif action == "stop-run":
            response = self.handle_request_stop_run(request)
        else:
            response = {"status": SERVER_STATUS.INVALID_ACTION.value}
        return response
