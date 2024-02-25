import pytest

from common.constants import *

DEFENSIVE_MATCHUPS = DICT_TYPE_MATCHUPS["Defensive"]


class TestDefensiveMatchup:
    @pytest.mark.matchup
    @pytest.mark.parametrize("types", ["Poison", "Bug", "Ground-Grass"])
    def test_fighting(self, browser_settings, selenium_helper, types):
        driver = browser_settings["driver"]
        base_url = browser_settings["base_url"]

        driver.get(base_url + "/defense")
        selenium_helper.select_types(types, is_offensive=False)
        selenium_helper.assert_type_matchups(DEFENSIVE_MATCHUPS[types])
