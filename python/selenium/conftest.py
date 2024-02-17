import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser(scope="session"):

    print("Opening Google Chrome...")
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")

    # return webdriver.Remote(
    #           command_executor=f"http://localhost:4444/wd/hub",
    #           options=options)
    browser = webdriver.Chrome(options=options)
    yield browser

    browser.close()
    browser.quit()
    print("Quitting Google Chrome...")