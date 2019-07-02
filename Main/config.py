from ccn_config import ccn_config
from instrument_manager import instrument_manager


class config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.instrument_mng = instrument_manager()
        self.project_name = 0;
        self.ccnstatus = 0;
        self.ccnconfig_path = 0
        self.ccnfile_path = 0

    def instrument_config(self):
        if self.ccnstatus == True:
            ccnconfig = ccn_config(self.ccnconfig_path)
            self.instrument_mng.instrument_creator('CCN', ccnconfig, self.ccnfile_path)
