from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_login():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security restrictions in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Navigate to website
    driver.get("https://www.saucedemo.com/")
    
    # Find the username and password fields
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Click to login
    driver.find_element(By.ID, "login-button").click()
    
    # Add sleep to wait until page will load
    time.sleep(3)
    
    # Verify that the login was successful by checking the new URL or page elements
    assert "inventory" in driver.current_url
    
    driver.quit()
    
def test_empty_cart_checkout():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security restrictions in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Initialize Chrome WebDriver with headless options
    driver = webdriver.Chrome(options=chrome_options)

    # Test code
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Perform checkout operations as in the original test
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    # Verifying empty cart behavior
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(cart_items) == 0, "Cart should be empty but contains items."

    driver.quit()