from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import pytest

def load_test_data(file_name):
    with open(file_name) as file:
        return json.load(file)
    
test_data = load_test_data("utils/test_data.json")

@pytest.mark.parametrize("username, password", [
    (test_data["login"]["standard_user"]["username"], test_data["login"]["standard_user"]["password"]),
])
def test_add_to_cart(browser, username, password):
    browser.get("https://www.saucedemo.com/")
    
    # Log in as a valid user
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    # Add the first product to the cart
    browser.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Open the cart and verify the product is added
    browser.find_element(By.ID, "shopping_cart_container").click()
    
    # check if product is in the cart
    cart_item = browser.find_element(By.CSS_SELECTOR, ".cart_item")
    assert cart_item is not None
    
    browser.quit()
@pytest.mark.parametrize("username, password", [
    (test_data["login"]["standard_user"]["username"], test_data["login"]["standard_user"]["password"]),
])   
def test_remove_from_cart(browser, username, password):
    # Step 1: Navigate to the hompage and login
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    # Step 2: Add a product to the cart
    browser.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Step 3: Open the cart and remove the item
    browser.find_element(By.ID, "shopping_cart_container").click()
    browser.find_element(By.CSS_SELECTOR, ".cart_button").click()
    
    # Step 4: Verify the cart is empty
    assert len(browser.find_elements(By.CSS_SELECTOR, ".cart_item")) == 0
    
    browser.quit()
    
@pytest.mark.parametrize("username, password", [
    (test_data["login"]["standard_user"]["username"], test_data["login"]["standard_user"]["password"]),
])    
def test_empty_cart_checkout(browser, username, password):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    # Perform checkout operations as per your test logic
    browser.find_element(By.ID, "shopping_cart_container").click()
    browser.find_element(By.ID, "checkout").click()

    # Verifying empty cart behavior
    cart_items = browser.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(cart_items) == 0, "Cart should be empty but contains items."

    browser.quit()