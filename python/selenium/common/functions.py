import os
import json

from . import constants

class CommonFunctions:
    def load_json_data(file_path):
        with open(f"{constants.PATH_ROOT}/{file_path}") as file:
            print(constants.PATH_ROOT)
            json_data = json.load(file)
            return dict(json_data)
        
    def get_root_path():
        while not os.path.isdir("test_data"): os.chdir("..")
        return os.getcwd()