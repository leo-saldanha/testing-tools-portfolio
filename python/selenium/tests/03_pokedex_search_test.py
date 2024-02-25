import pytest, time

from common.constants import *


class TestPokedexSearch:
    @pytest.mark.pokedex
    @pytest.mark.parametrize("pokemon", 
                             ["Poliwhirl", "Snorlax", "Magcargo", "Ninjask", "Pachirisu"])
    def test_fighting(self, browser_settings, selenium_helper, pokemon):
        driver = browser_settings["driver"]
        base_url = browser_settings["base_url"]

        driver.get(base_url + "/pokedex")
        selenium_helper.search_pokedex(pokemon)
        selenium_helper.assert_pokedex_entry(DICT_POKEMON_DATA[pokemon])
