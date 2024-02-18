import os
import json

from . import constants

class CommonFunctions:
    def get_type_matchups():
        with open(f"{constants.PATH_ROOT}/test_data/type_matchup.json") as file:
            print(constants.PATH_ROOT)
            json_data = json.load(file)
            return dict(json_data)
        
    def get_root_path():
        while not os.path.isdir("test_data"): os.chdir("..")
        return os.getcwd()