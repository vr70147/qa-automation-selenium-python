from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("username, expected_error", [
    ("", "Epic sadface: Username is required"),  # Empty username
    ("a" * 255, None),  # Max length username (valid)
    ("a" * 256, "Epic sadface: Username and password do not match any user in this service"),  # Above max length
])
def test_username_boundaries(username, expected_error, valid_credentials):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(valid_credentials["password"])
    driver.find_element(By.ID, "login-button").click()
    
    if expected_error:
        err_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        assert expected_error in err_message
    else:
        assert "inventory" in driver.current_url
        
    driver.quit()


@pytest.mark.parametrize("username, expected_error", [
    ("<script>alert(1)</script>", "Epic sadface: Username and password do not match any user in this service"),
    ("' OR 1=1 --", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", None)  # Control test
])
def test_special_characters_username(username, expected_error, valid_credentials):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(valid_credentials["password"])
    driver.find_element(By.ID, "login-button").click()
    
    if expected_error:
        err_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        assert expected_error in err_message
    else:
        assert "inventory" in driver.current_url
        
    driver.quit()


@pytest.mark.parametrize("quantity, expected_message", [
    (-1, "Quantity cannot be negative"),  # Negative number
    (0, "Quantity must be at least 1"),  # Zero
    (1, None)  # Valid quantity
])
def test_cart_quantity_boundaries(quantity, expected_message, valid_credentials):
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(valid_credentials["username"])
    driver.find_element(By.ID, "password").send_keys(valid_credentials["password"])
    driver.find_element(By.ID, "login-button").click()
    
    # Add product to cart
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Change quantity in cart
    quantity_input = driver.find_element(By.CSS_SELECTOR, ".cart_quantity")
    quantity_input.clear()
    quantity_input.send_keys(str(quantity))
    
    if expected_message:
        err_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        assert expected_message in err_message
    else:
        assert "checkout" in driver.page_source
        
    driver.quit()
