
from Main.reader import reader
from Main.ccn_config import ccn_config
from Main.instrument_manager import instrument_manager
from Main.data import data as d

class manualtest:
    # CCN Config Reader Tester
    #ccn_config = ccn_config(
    #    r'C:\Users\naxso\PycharmProjects\Alfa-Project\Main\config_files\CCN100configurationACAS.txt')

    # instrument manager tester
    #instrument_manager = instrument_manager()
    #instrument_manager.instrument_creator('CCN',
    #                                      r'C:\Users\naxso\PycharmProjects\Alfa-Project\Main\config_files\CCN100configurationACAS.txt',
    #                                      r'C:\Users\naxso\PycharmProjects\Alfa-Project\Main\File_Samples\ccnfile.csv')
    #instrument = instrument_manager.get_instrument(0)

    #Test Reader
    reader_test = reader(r'C:\Users\naxso\PycharmProjects\Alfa-Project\Main\File_Samples\ccnfile.csv')
    reader_test = reader(r'C:\Users\naxso\PycharmProjects\Alfa-Project\Main\File_Samples\20190619143438__x2.h5')

