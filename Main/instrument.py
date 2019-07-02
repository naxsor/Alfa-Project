import datetime
import json
import data as d



#creater instrumen object
class instrument:

    def __init__(self, id, name, config_file, file_path):
        self.id = id
        self.name = name
        self.config_file = config_file
        self.data = d.data(file_path)

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










