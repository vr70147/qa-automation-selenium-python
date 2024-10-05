from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.binary_location = '/usr/bin/firefox'
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()