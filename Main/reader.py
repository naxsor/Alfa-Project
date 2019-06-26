import data as d
import pandas as pd
import numpy as np
import h5py as h5

from Main.extensionManager import extensionManager as ext_mng
from instrumentConfig import instrumentConfig



class reader:
    def __init__(self, file_path):
        self.extensionmngr = ext_mng(file_path)
        self.ext = self.extensionmngr.extensionReader()
        self.data = d.data(file_path)
        self.num_lines = d.data.getNum_line(self.data)
        self.readerSelector()
        # self.getData()

    def readerSelector(self):
        if self.ext == 1:
            print ('Calling CSV reader...')
            self.readerCSV()
            return 1
        elif self.ext == 3:
            print ('Calling h5 reader...')
            self.readerh5()
            return 3

    def readerCSV(self):
        with open(d.data.getfile_path(self.data), 'r') as file:
            d.data.setorigin_path(self.data, next(file))
            d.data.setDate(self.data, next(file))
            d.data.setTime(self.data, next(file))
        with open(d.data.getfile_path(self.data), 'r') as file:
            dataframe = pd.read_csv(file, skiprows=self.num_lines, header=3, skip_blank_lines=True, comment="!",
                                    keep_default_na=False, na_values=[""])
            # Fix headers
            dataframe.columns = dataframe.columns.str.strip()
            d.data.setDataframe(self.data, dataframe)
            d.data.setNumlines(self.data, len(dataframe))

    def readerh5(self):

        dataframe_list = []
        header = instrumentConfig.WIBS_NEO('instrumentVariables')


        def get_all(name):
            print(name)

        def merge():
            merged = dataframe_list[0]
            for i in range(len(dataframe_list)):
                merged = pd.concat([merged, dataframe_list[i+1]], axis=1, sort=False)

        def get_objects(name, obj):
            if isinstance(obj, h5.Dataset):
                print (obj)
                dataframe = pd.DataFrame(obj)
                dataframe_list.append(dataframe)


        with h5.File(d.data.getfile_path(self.data), 'r') as file:
            MonitoringData = file.get('/NEO/MonitoringData')
            ParticleData = file.get('/NEO/ParticleData')
            NEO_MonitorinData = list(MonitoringData.items())
            NEO_ParticleData = list(ParticleData.items())
            file.visititems(get_objects)
            merge()


    def getData(self):
        return self.data
