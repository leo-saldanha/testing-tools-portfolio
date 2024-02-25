import pytest

from common.constants import *

OFFENSIVE_MATCHUPS = DICT_TYPE_MATCHUPS["Offensive"]


class TestOffensiveMatchup:
    @pytest.mark.matchup
    @pytest.mark.parametrize("types", ["Fighting", "Fairy", "Fire", "Psychic-Ghost", "Dragon-Steel"])
    def test_fighting(self, browser_settings, selenium_helper, types):
        driver = browser_settings["driver"]
        base_url = browser_settings["base_url"]

        driver.get(base_url + "/offense")
        selenium_helper.select_types(types)
        selenium_helper.assert_type_matchups(OFFENSIVE_MATCHUPS[types])
