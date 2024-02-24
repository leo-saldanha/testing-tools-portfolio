from . import functions


PATH_ROOT = functions.CommonFunctions.get_root_path()

## URLs
URL_MASK_WEBSITE = "http://{0}:5173"
URL_MASK_GRID = "http://{0}:4444/wd/hub"
BASE_URL_SITE_LOCAL = "localhost"
BASE_URL_SITE_DOCKER = "website"

## JSON data
DICT_TYPE_MATCHUPS = functions.CommonFunctions.get_type_matchups()

## Exception messages
EXCEPTION_INVALID_ENV = "Invalid --env option, please use 'local', 'docker-local' or 'docker-ci'"
