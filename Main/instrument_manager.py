from Main.instrument import instrument as i
from Main.reader import reader
from Main.instrument_info import CCN, WIBS_NEO
from data import data as d

class instrument_manager:
    def __init__(self):
        self.instruments = []
        self.count = len(self.instruments)
        self.reader = reader

    def instrument_creator(self, name, config, file_path):
        instrument = i(self.count, name, config, file_path)
        self.instruments.append(instrument)

    def get_instrument(self, index):
        for i in range(len(self.instruments)):
            if i == index:
                return self.instruments[i-1]



