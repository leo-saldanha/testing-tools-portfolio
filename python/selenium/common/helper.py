from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class SeleniumHelper:
    def __init__(self, driver):
       self.driver = driver

    def get_by_test_id(self, test_id, base_element=None) -> WebElement:
        if base_element == None: base_element = self.driver
        return base_element.find_element(By.CSS_SELECTOR, f"[data-testid='{test_id}']")