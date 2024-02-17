import json

from . import constants

class CommonFunctions:
    def get_type_matchups():
        with open(f"{constants.PATH_ROOT}/test_data/type_matchup.json") as file:
            json_data = json.load(file)
            return dict(json_data)