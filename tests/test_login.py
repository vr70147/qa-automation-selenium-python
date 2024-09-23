from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    