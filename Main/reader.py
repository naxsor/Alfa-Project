import data as d
import pandas as pd
import numpy as np
import h5py as h5
import os.path, time
import shutil

from instrument_info import WIBS_NEO, CCN



class reader:
    def __init__(self, file_path):
        self.ext = os.path.splitext(file_path)[-1].lower()
        self.data = d.data(file_path)
        self.num_lines = d.data.getNum_line(self.data)
        self.extensionReader()


    def extensionReader(self):
        if self.ext == '.csv':
            self.readerSelector(1)
        elif self.ext == '.dat':
            self.readerSelector(2)
        elif self.ext == '.h5':
            self.readerSelector(3)
        else:
            print ('No file extension detected')
            return False

    #Calls Specific Reader
    def readerSelector(self, int):
        if int == 1:
            self.readerCCN()
        elif int == 3:
            self.readerNEO()

    #Reader for CCN File
    def readerCCN(self):
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

    #Reader for NEO file
    def readerNEO(self):

        dataframe_list = []

        #Iterate through .h5 file
        def get_objects(name, obj):
            if isinstance(obj, h5.Dataset):
                dataframe = pd.DataFrame(obj)
                dataframe_list.append(dataframe)

        def merge():
            #Extract a concatenate dataframes from data sets in dataframe list
            for i in range(len(dataframe_list)):
                if i == 0:
                    merged = dataframe_list[i]
                else:
                    merged = pd.concat([merged, dataframe_list[i]], axis=1, sort=False)
            #Set Column Headers
            merged.columns = WIBS_NEO.instrumentVariables
            d.data.setDataframe(self.data, merged)

        with h5.File(d.data.getfile_path(self.data), 'r') as file:
            file.visititems(get_objects)
            merge()


