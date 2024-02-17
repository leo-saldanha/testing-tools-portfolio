import time

from selenium.webdriver.common.by import By

# Fighting
# Fire
# Fairy
# Psychic / Ghost
# Dragon / Steel

class TestOffensiveMatchup:
    def test_fighting(self, browser):
        browser.get("http://localhost:5173/offense")
        browser.find_element(By.CSS_SELECTOR, "[data-testid='option-fighting']").click()
        time.sleep(5)