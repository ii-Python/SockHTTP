# Modules
import socket
from .internals.core import Request
from .internals.workers import process, send

# Main class
class SockHTTP(object):

    def __init__(self, log_requests = True):
        self.endpoints = {}
        self.log_requests = log_requests

    def _create_socket(self, host, port, max_connections = 5):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(max_connections)

        return sock

    def endpoint(self, method, endpoint):

        def get_callback(callback):

            self.endpoints[endpoint] = {
                "method": method,
                "callback": callback
            }

        return get_callback

    def add_endpoint(self, method, endpoint, callback):

        self.endpoints[endpoint] = {
            "method": method,
            "callback": callback
        }

    def run(self, host, port, **kwargs):
    
        self.socket = self._create_socket(host, port, **kwargs)

        print(f"Server now running on {host}:{port}")
        print()

        while True:

            conn, addr = self.socket.accept()

            # Begin parsing request
            data = conn.recv(1024).decode()

            if not data:

                continue

            headers = data.split("\n")
            location = headers[0].split(" ")

            headers = headers[1:]

            # Locate method and endpoint
            method = location[0]
            endpoint = location[1]

            request = Request(endpoint, method, headers)
            
            # Do stuff with it
            resp, status = process(self, request)
            send(conn, resp, status)

            # Log
            if self.log_requests:

                print(f"[{addr[0]}]: {method} {endpoint} - {status}")
