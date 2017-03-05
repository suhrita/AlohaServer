#!/usr/bin/python

import socket
import ssl
import json

class ConnectionManager:

    def __init__(self):
        self.verify_mode = ssl.CERT_REQUIRED
        self.hostname = '127.0.0.1'
        self.port = 2099

    def getWrappedSocket(self, sock, hostname):
        try:
            # Get Context
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.verify_mode = self.verify_mode
            wrappedSocket = context.wrap_socket(sock, server_hostname = hostname)
            return wrappedSocket

        except ImportError as e:
            print json.dumps({"status" : "error", "ConnectionManager.getWrappedSocket" : str(e)})
            exit(0)

    def getSocket(self):
        try:
            # Create the socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Create the SSL wrapper for the socket object
            wrappedSocket = self.getWrappedSocket(sock, self.hostname)
            wrappedSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            wrappedSocket.bind((self.hostname, self.port))
            return wrappedSocket

        except ImportError as e:
            print json.dumps({"status" : "error", "ConnectionManager.createConnection" : str(e)})
            exit(0)