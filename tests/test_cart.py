from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_cart():
    driver = webdriver.Chrome()
    
    driver.get("https://www.saucedemo.com/")
    
    # Log in as a valid user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Add the first product to the cart
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Open the cart and verify the product is added
    driver.find_element(By.ID, "shopping_cart_container").click()
    
    # check if product is in the cart
    cart_item = driver.find_element(By.CSS_SELECTOR, ".cart_item")
    assert cart_item is not None
    
    driver.quit()