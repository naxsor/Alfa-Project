import os


class extensionManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.ext = os.path.splitext(self.file_path)[-1].lower()

    def extensionReader(self):
        if self.ext == '.csv':
            print ('Is an .CSV file')
            return 1
        elif self.ext == '.dat':
            print ('Is an .dat file')
            return 2
        elif self.ext == '.h5':
            print ('Is an .h5 file')
            return 3
        else:
            print ('No file extension detected')
            return False