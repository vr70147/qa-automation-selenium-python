from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

def load_test_data(file_name):
    with open(file_name) as file:
        return json.load(file)
    
test_data = load_test_data("utils/test_data.json")

@pytest.mark.parametrize("password", [
    (test_data["login"]["standard_user"]["password"]),
])
@pytest.mark.parametrize("username, expected_error", [
    ("", "Epic sadface: Username is required"),  # Empty username
    ("a" * 255, "Epic sadface: Username and password do not match any user in this service"),  # Max length username (valid)
    ("a" * 256, "Epic sadface: Username and password do not match any user in this service"),  # Above max length
])
def test_username_boundaries(browser, username, expected_error, password):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    if expected_error:
        err_message = browser.find_element(By.CSS_SELECTOR, ".error-message-container").text
        assert expected_error in err_message
    else:
        assert "inventory" in browser.current_url
        
    browser.quit()

@pytest.mark.parametrize("password", [
    (test_data["login"]["standard_user"]["password"]),
])
@pytest.mark.parametrize("username, expected_error", [
    ("<script>alert(1)</script>", "Epic sadface: Username and password do not match any user in this service"),
    ("' OR 1=1 --", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", None)  # Control test
])
def test_special_characters_username(browser, username, expected_error, password):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    if expected_error:
        err_message = browser.find_element(By.CSS_SELECTOR, ".error-message-container").text
        assert expected_error in err_message
    else:
        assert "inventory" in browser.current_url
        
    browser.quit()

@pytest.mark.parametrize("username, password", [
    (test_data["login"]["standard_user"]["username"], test_data["login"]["standard_user"]["password"]),
])
@pytest.mark.parametrize("quantity, expected_message", [
    (1, None),  # Valid quantity
])
def test_cart_quantity_boundaries(browser, quantity, expected_message, username, password):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    # Add a product to the cart before checking quantity
    browser.find_element(By.CSS_SELECTOR, ".inventory_item button").click()

    # Navigate to cart page
    browser.find_element(By.ID, "shopping_cart_container").click()

    # Wait for the cart quantity to be displayed
    wait = WebDriverWait(browser, 10)
    cart_quantity = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart_quantity")))

    # Perform the boundary checks
    if expected_message:
        assert expected_message in cart_quantity.text
    else:
        assert cart_quantity.text == str(quantity)
        
    browser.quit()
