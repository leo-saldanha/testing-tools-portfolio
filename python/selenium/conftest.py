import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from common.constants import *
from common.helper import SeleniumHelper


## Arguments 

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="local",
                     help="local|docker-local|docker-ci")
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
    shared_options = []

    # Set extra options regardless of which browser
    if headless_mode or env == "docker": shared_options.append("--headless")

    browser_info = get_driver_settings(env, selected_browser, shared_options)

    yield browser_info

    browser_info["driver"].close()
    browser_info["driver"].quit()

@pytest.fixture
def selenium_helper(browser_settings, scope="session"):
    return SeleniumHelper(browser_settings["driver"])

## Shared functions

def get_driver_settings(env, selected_browser, shared_options):
    if selected_browser == "chrome":
        options = ChromeOptions()
        for option in shared_options: options.add_argument(option)
    else:
        raise Exception("Invalid --browser option, please use 'chrome' for now")

    if env == "local":
        base_url_website = URL_MASK_WEBSITE.format(BASE_URL_SITE_LOCAL)
        driver = webdriver.Chrome(options=options)
    elif "docker" in env:
        if env == "docker-local": base_url_selenium_grid = "localhost"
        elif env == "docker-ci": base_url_selenium_grid = "selenium-hub"
        else: raise Exception(EXCEPTION_INVALID_ENV)

        base_url_website = URL_MASK_WEBSITE.format(BASE_URL_SITE_DOCKER)
        driver = webdriver.Remote(command_executor=URL_MASK_GRID.format(base_url_selenium_grid),
                                  options=options)
    else:
        raise Exception(EXCEPTION_INVALID_ENV)

    return { "base_url": base_url_website, "driver": driver }
