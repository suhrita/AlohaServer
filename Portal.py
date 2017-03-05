#!/usr/bin/python

import json
from ConnectionManager import ConnectionManager
from Client import Client

class Portal:
    def __init__(self):
        self.numberOfConnections = 10
        self.ClientConnections = []

    def establishConnections(self):
        try:
            conn = ConnectionManager()
            serverSocket = conn.getSocket()
            while True:
                serverSocket.listen(self.numberOfConnections)
                (channel, (clientHostname, clientPort)) = serverSocket.accept()
                client = Client(clientHostname, clientPort, channel)
                self.ClientConnections.append(client)

        except ImportError as e:
            print json.dumps({"status" : "error", "Portal.establishConnections" : str(e)})
            exit(0)


if __name__ == "__main__":
        portal = Portal()
        portal.establishConnections()