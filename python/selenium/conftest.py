import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.constants import *
from common.helper import SeleniumHelper

## Arguments 

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="local",
                     help="local|docker")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="only chrome for now")
    parser.addoption("--headless",
                     action="store_true",
                     default=False,
                     help="use to hide the browser")

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

## Session-wide fixtures

@pytest.fixture
def browser_settings(request, env, scope="session"):
    selected_browser = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")

    if env == "local":
        base_url = BASE_URL_SITE_LOCAL

        options = Options()
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--verbose")

        if headless_mode or env == "docker": options.add_argument("--headless")

        if selected_browser == "chrome":
            name = "Google Chrome"
            driver = webdriver.Chrome(options=options)
        else:
            raise Exception("Invalid --browser option, please use 'chrome' for now")
    elif env == "docker":
        name = "Google Chrome"
        base_url = BASE_URL_SITE_DOCKER
        driver = webdriver.Remote(command_executor=f"http://selenium-hub:4444",
                                   options=webdriver.ChromeOptions())
    else:
        raise Exception("Invalid --env option, please use 'local' or 'docker'")

    print(f"\nOpening {name}...")

    yield { "base_url": base_url, "driver": driver }

    driver.close()
    driver.quit()

    print("\nQuitting Google Chrome...")

@pytest.fixture
def selenium_helper(browser_settings, scope="session"):
    return SeleniumHelper(browser_settings["driver"])