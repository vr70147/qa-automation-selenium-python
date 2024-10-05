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
def test_checkout_flow(browser, username, password): 
    # Step 1: Navigate to the homepage and login
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()
    
    # Step 2: Add a product to the cart
    browser.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Step 3: Proceed to the cart
    browser.find_element(By.ID, "shopping_cart_container").click()
    
    # Step 4: Proceed to checkout
    browser.find_element(By.ID, "checkout").click()
    
    # Step 5: Fill out checkout form
    browser.find_element(By.ID, "first-name").send_keys("Raanan")
    browser.find_element(By.ID, "last-name").send_keys("Adut")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    browser.find_element(By.ID, "continue").click()
    
    # Step 6: Finish checkout
    browser.find_element(By.ID, "finish").click()
    
    # Step 7: Verify checkout success message
    success_message = browser.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in success_message
    
    browser.quit()