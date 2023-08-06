from copy import deepcopy
import json
import socket

import zmq

class TCPServer:
    def __init__(self, server_endpoint, server_config):
        self.server_config = deepcopy(server_config)
        self.server_endpoint = deepcopy(server_endpoint)

    def get_client(self):
        server_endpoint = deepcopy(self.server_endpoint)
        ip = self.server_endpoint.get('ip')
        if ip is None:
            hostname = socket.gethostname()
            ip       = socket.gethostbyname(hostname)
            server_endpoint['ip'] = ip

        return "unicorncommon.channels.tcp.TCPClient", deepcopy(server_endpoint)

    def start_server(self, server, quit_requested):
        ip = self.server_endpoint.get('ip')
        endpoint = f"tcp://{'*' if ip is None else ip}:{self.server_endpoint['port']}"
        poll_timeout = self.server_config.get("poll_timeout", 15000) # 15 seconds
        with zmq.Context() as context:
            with context.socket(zmq.REP) as socket:
                socket.bind(endpoint)
                while not quit_requested():
                    flags = socket.poll(timeout=poll_timeout)
                    if flags == 0:
                        # no message
                        server.on_idle()
                        continue

                    message = socket.recv()
                    request = json.loads(message.decode("utf-8"))
                    response = server.handle_request(request)
                    socket.send(json.dumps(response).encode("utf-8"))
                    server.on_idle()


class TCPClient:
    def __init__(self, server_endpoint, client_config):
        self.client_config = deepcopy(client_config)
        self.server_endpoint = deepcopy(server_endpoint)

    def send(self, request):
        with zmq.Context() as context:
            with context.socket(zmq.REQ) as socket:
                endpoint = f"tcp://{self.server_endpoint['ip']}:{self.server_endpoint['port']}"
                socket.connect(endpoint)

                message = json.dumps(request)
                socket.send(message.encode("utf-8"))

                message = socket.recv()
                response = json.loads(message.decode("utf-8"))
                return response
