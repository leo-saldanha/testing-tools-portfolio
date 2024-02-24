from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class SeleniumHelper:
    def __init__(self, driver):
       self.driver = driver

    def get_by_test_id(self, test_id, base_element=None) -> WebElement:
        if base_element == None: base_element = self.driver
        elements = base_element.find_elements(By.CSS_SELECTOR, f"[data-testid='{test_id}']")

        print(f"test_id: {test_id}")
        print(f"elements: {elements}")

        return elements if len(elements) > 1 else elements[0]

    def select_types(self, type, is_offensive=True):
        type_list = type.split("-")

        for value in type_list:
            if is_offensive:
                self.get_by_test_id(f"option-{value.lower()}").click()
            else:
                current_pos = type_list.index(value)
                self.get_by_test_id(f"radio-{value.lower()}")[current_pos].click()

    def assert_type_matchups(self, matchups_dict):
        for section, matchups in matchups_dict.items():
            section_element = self.get_by_test_id(f"section-{section}")
            print(f"\nSection: {section}")
            for matchup in matchups:
                result = self.get_by_test_id(f"result-{matchup.lower()}", section_element)
                print(f"assert {result.text} == {matchup}")
                assert result.text == matchup
