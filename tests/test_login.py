from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_login():
    # Setup Chrome driver
    driver = webdriver.Chrome()
    
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
    
def test_invalid_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for CI
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security restrictions in CI environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
    assert "Username and password do not match" in error_message

    driver.quit()
