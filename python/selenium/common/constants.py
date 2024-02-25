from . import functions


# Paths
PATH_ROOT = functions.CommonFunctions.get_root_path()
PATH_TYPE_MATCHUP_DATA = "test_data/type_matchup.json"
PATH_POKEMON_DATA = "test_data/pokemons.json"

## URLs
URL_MASK_WEBSITE = "http://{0}:5173"
URL_MASK_GRID = "http://{0}:4444/wd/hub"
BASE_URL_SITE_LOCAL = "localhost"
BASE_URL_SITE_DOCKER = "website"

## JSON data
DICT_TYPE_MATCHUPS = functions.CommonFunctions.load_json_data(PATH_TYPE_MATCHUP_DATA)
DICT_POKEMON_DATA = functions.CommonFunctions.load_json_data(PATH_POKEMON_DATA)

## Exception messages
EXCEPTION_INVALID_ENV = "Invalid --env option, please use 'local', 'docker-local' or 'docker-ci'"
