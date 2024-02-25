import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class SeleniumHelper:
    def __init__(self, driver):
       self.driver = driver

    def get_by_test_id(self, test_id, base_element=None, seconds_to_retry=1, total_retries=5):
        if base_element == None: base_element = self.driver
        elements = []
        retries = total_retries

        while retries > 0 or len(elements) == 0:
            elements = base_element.find_elements(By.CSS_SELECTOR, f"[data-testid='{test_id}']")

            if len(elements) > 1: return elements
            elif len(elements) == 1: return elements[0]
            else:
                time.sleep(seconds_to_retry)
                retries -= 1

        raise Exception(
            f"No element(s) with testid {test_id} found after {total_retries} retries.")

    def search(self, element, text):
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def select_types(self, type, is_offensive=True):
        type_list = type.split("-")

        for value in type_list:
            if is_offensive:
                self.get_by_test_id(f"option-{value.lower()}").click()
            else:
                current_pos = type_list.index(value)
                self.get_by_test_id(f"radio-{value.lower()}")[current_pos].click()

    def search_pokedex(self, pokemon):
        pokedex_page = self.get_by_test_id("page-pokedex")
        search_bar = self.get_by_test_id("search-bar", pokedex_page)
        self.search(search_bar, pokemon)

    def assert_type_matchups(self, matchups_dict):
        for section, matchups in matchups_dict.items():
            section_element = self.get_by_test_id(f"section-{section}")
            print(f"\nSection: {section}")
            for matchup in matchups:
                result = self.get_by_test_id(f"result-{matchup.lower()}", section_element)
                assert result.text == matchup

    def assert_pokedex_entry(self, expected_data):
        id, types, stats = expected_data["id"], expected_data["type"], expected_data["stats"]
        summed_stats = 0

        pokedex_page = self.get_by_test_id("page-pokedex")
        pokedex_entry = self.get_by_test_id(f"entry-{id}", pokedex_page)

        if isinstance(types, list):
            for type in types:
                type_tag = self.get_by_test_id(f"tag-{type.lower()}", pokedex_entry)
                assert type_tag.text == type
        else:
            type_tag = self.get_by_test_id(f"tag-{types.lower()}", pokedex_entry)
            assert type_tag.text == types

        for stat, value in stats.items():
            stat_entry = self.get_by_test_id(f"text-{stat.lower()}", pokedex_entry)
            assert stat_entry.text == str(value)

            summed_stats += value

        total_stats = self.get_by_test_id("text-total", pokedex_entry)
        assert int(total_stats.text) == summed_stats
