from pathlib import Path

from . import functions


PATH_ROOT = Path(__file__).parents[3]
BASE_URL_SITE_LOCAL = "localhost"
BASE_URL_SITE_DOCKER = "website"

DICT_TYPE_MATCHUPS = functions.CommonFunctions.get_type_matchups()
