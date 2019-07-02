

class ccn_config:
    def __init__(self, file_path):
        self.file_path = file_path
        #Project Title
        self.title = 0;
        #Number of Channels
        self.numberofChannels = 0;
        #Size Thresholds
        self.threshold_size = []
        #Line where data starts
        self.data_line =0;
        #SS Column
        self.ss_column = 0;
        #PSD Column
        self.psd_column = 0;
        #Sample Flow Column
        self.sample_flow_column=0;
        #Column where house keeping starts
        self.housekeeping_start=0;
        #Names of housekeeping variables
        self.housekeeping_names=[];
        #Number of housekeeping variables
        self.housekeeping_parameters=0;
        self.read()

    def read(self):
        with open(self.file_path, 'r') as file:
            temp = file.read().splitlines()
            #self.threshold_size = temp[5:25]
            for i, line in enumerate(temp):
                if i == 3:
                    self.numberofChannels = int(line)
                elif 4 < i < 25:
                    self.threshold_size.append(int(line))
                elif i == 26:
                    self.data_line = int(line)
                elif i == 28:
                    self.ss_column = int(line)
                elif i == 30:
                    self.psd_column = int(line)
                elif i == 32:
                    self.sample_flow_column = int(line)
                elif i == 34:
                    self.housekeeping_start = int(line)
                elif i == 36:
                    self.housekeeping_parameters = int(line)
                elif i >= 38:
                    self.housekeeping_names.append(line)
