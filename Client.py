#!/usr/bin/python

import json

class Client():
    def __init__(self, clientHostName, clientPort, channel):
        self.clientHostName = clientHostName
        self.clientPort = clientPort
        self.clientType = self.getClientType()
        self.channel = channel

    # TO DO implement this method properly
    def getClientType(self):
        try:
            self.WebClient = "Web Client"
            self.MobileClient = "Mobile Client"
            return self.WebClient

        except ImportError as e:
            print json.dumps({"status" : "error", "Client.getClientType" : str(e)})
            exit(0)