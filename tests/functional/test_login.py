from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest
import json

def load_test_data(file_name):
    with open(file_name) as file:
        return json.load(file)
    
test_data = load_test_data("utils/test_data.json")

@pytest.mark.parametrize("username, password", [
    (test_data["login"]["standard_user"]["username"], test_data["login"]["standard_user"]["password"]),
])
def test_login(browser, username, password):
    
    # Navigate to website
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    # Add sleep to wait until page will load
    time.sleep(3)
    
    # Verify that the login was successful by checking the new URL or page elements
    assert "inventory" in browser.current_url
    
    browser.quit()
    
@pytest.mark.parametrize("username, password", [
    ("locked_out_user", "secret_sauce"),
])
def test_login_locked_out_user(browser, username, password):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    # Check for the locked out user error message
    error_message = browser.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Sorry, this user has been locked out." in error_message
    

@pytest.mark.parametrize("username, password, expected_error", [
    ("", "password", "Epic sadface: Username is required"),
    ("valid_user", "", "Epic sadface: Password is required"),
    ("valid_user", "invalid_password", "Epic sadface: Username and password do not match any user in this service"),
    ("' OR 1=1 --", "any_password", "Epic sadface: Username and password do not match any user in this service"),
    ("a" * 256, "password", "Epic sadface: Username and password do not match any user in this service"),
])
def test_invalid_login(browser, username, password, expected_error):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    err_message = browser.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert expected_error in err_message
    
    browser.quit()
    
@pytest.mark.parametrize("username, password, expected_error", [
    ("a" * 255, "password", "Epic sadface: Username and password do not match any user in this service"),  # Maximum allowed username length
    ("a" * 256, "password", "Epic sadface: Username and password do not match any user in this service"),  # Exceed maximum username length
    ("", "password", "Epic sadface: Username is required"),  # Empty username
    ("valid_user", "", "Epic sadface: Password is required"),  # Empty password
])
def test_login_boundary_values(browser, username, password, expected_error):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    # Verify the error message for invalid input
    err_message = browser.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert expected_error in err_message
    
    browser.quit()
    

    
    
    
    
