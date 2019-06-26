

class data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.origin_path = 0
        self.date = 0
        self.time = 0
        self.data_frame = 0
        self.num_line = 0

    def getfile_path(self):
        return self.file_path

    def getorigin_path(self):
        return self.origin_path

    def getDate(self):
        return self.date

    def getTime(self):
        return self.time

    def getDataframe(self):
        return self.data_frame

    def getNum_line(self):
        return self.num_line

    def setfile_path(self, file_path):
        self.file_path = file_path

    def setorigin_path(self, origin_path):
        self.origin_path = origin_path

    def setDate(self, date):
        self.date = date

    def setTime(self, time):
        self.time = time

    def setDataframe(self, data_frame):
        self.data_frame = data_frame

    def setNumlines(self, num_lines):
        self.num_line = num_lines
