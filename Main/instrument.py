import datetime
import json
import data as d

from instrumentConfig import instrumentConfig

#creater instrumen object
class instrument:

    instCount = 0

    def __init__(self, id, name, signalType, data):
        self.id = self.instCount
        self.name = name
        self.status = 0
        self.signalType = signalType
        self.data = data
        instrument.instCount += 1
        self.instCount += 1

    def statusCheck(self, x):
        if x == 1:
            return True
        elif x == 0:
            return False

    def getid(self):
        return self.id

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def getSignalType(self):
        return self.signalType

    def getData(self):
        return self.data

    def setid(self, id):
        self.id = id

    def setname(self, name):
        self.name = name

    def setStatus(self, status):
        self.status = status

    def setSignalType(self, type):
        self.signalType = type

    def setData(self, data):
        self.data = data










