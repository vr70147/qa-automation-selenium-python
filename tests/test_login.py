from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest
from utils import confest
from utils.confest import valid_credentials


def test_login(valid_credentials):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to website
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys(valid_credentials["username"])
    driver.find_element(By.ID, "password").send_keys(valid_credentials["password"])
    driver.find_element(By.ID, "login-button").click()
    
    # Add sleep to wait until page will load
    time.sleep(3)
    
    # Verify that the login was successful by checking the new URL or page elements
    assert "inventory" in driver.current_url
    
    driver.quit()
    

@pytest.mark.parametrize("username, password, expected_error", [
    ("", "password", "Epic sadface: Username is required"),
    ("valid_user", "", "Epic sadface: Password is required"),
    ("valid_user", "invalid_password", "Epic sadface: Username and password do not match any user in this service"),
    ("' OR 1=1 --", "any_password", "Epic sadface: Username and password do not match any user in this service"),
    ("a" * 256, "password", "Epic sadface: Username and password do not match any user in this service"),
])
def test_invalid_login(username, password, expected_error):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    
    err_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert expected_error in err_message
    
    driver.quit()
    
    
