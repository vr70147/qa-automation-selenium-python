from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_choice = request.config.getoption("--browser")
    if browser_choice == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_choice == "firefox":
        options = FirefoxOptions()
        options.binary_location = '/usr/bin/firefox'
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()