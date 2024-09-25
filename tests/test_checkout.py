from selenium import webdriver
from selenium.webdriver.common.by import By

def test_checkout_flow():
    driver = webdriver.Chrome()
    
    # Step 1: Navigate to the homepage and login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Step 2: Add a product to the cart
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Step 3: Proceed to the cart
    driver.find_element(By.ID, "shopping_cart_container").click()
    
    # Step 4: Proceed to checkout
    driver.find_element(By.ID, "checkout").click()
    
    # Step 5: Fill out checkout form
    driver.find_element(By.ID, "first-name").send_keys("Raanan")
    driver.find_element(By.ID, "last-name").send_keys("Adut")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    
    # Step 6: Finish checkout
    driver.find_element(By.ID, "finish").click()
    
    # Step 7: Verify checkout success message
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in success_message
    
    driver.quit()
    
def test_empty_cart_checkout():
    driver = webdriver.Chrome()
    
    # Step 1: Navigate to the homepage and login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Step 2: Go to cart without adding any products
    driver.find_element(By.ID, "shopping_cart_container").click()
    
    # Step 3: Attempt to proceed to checkout
    driver.find_element(By.ID, "checkout").click()

    # Step 4: Verify that the cart is empty at checkout
    # Check if there's a message or indication that the cart is empty during checkout
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(cart_items) == 0, "Cart should be empty but contains items."

    # Step 5: Attempt to finish checkout and ensure it fails
    finish_button = driver.find_element(By.ID, "finish")
    assert not finish_button.is_enabled(), "Finish button should be disabled for empty cart."

    driver.quit()
    
    