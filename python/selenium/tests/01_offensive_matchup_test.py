import time
import pytest

from common.constants import *

OFFENSIVE_MATCHUPS = DICT_TYPE_MATCHUPS["Offensive"]


## Reusable functions

def assertTypeMatchups(selenium_helper, matchups_dict):
    for section, matchups in matchups_dict.items():
        section_element = selenium_helper.get_by_test_id(f"section-{section}")
        print(f"\nSection: {section}")
        for matchup in matchups:
            result = selenium_helper.get_by_test_id(f"result-{matchup.lower()}", section_element)
            print(f"assert {result.text} == {matchup}")
            assert result.text == matchup

def selectTypes(selenium_helper, type):
    type = type.split("-")
    for value in type: selenium_helper.get_by_test_id(f"option-{value.lower()}").click()

## Test suite

class TestOffensiveMatchup:
    @pytest.mark.parametrize("types", ["Fighting", "Fairy", "Fire", "Psychic-Ghost", "Dragon-Steel"])
    def test_fighting(self, browser_settings, selenium_helper, types):
        driver = browser_settings["driver"]
        base_url = browser_settings["base_url"]

        print(f"http://{base_url}:5173/offense")

        driver.get(f"http://{base_url}:5173/offense")
        selectTypes(selenium_helper, types)
        assertTypeMatchups(selenium_helper, OFFENSIVE_MATCHUPS[types])
