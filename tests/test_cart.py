from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_add_to_cart():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
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
    
def test_remove_from_cart():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    # Setup Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Step 1: Navigate to the hompage and login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Step 2: Add a product to the cart
    driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
    
    # Step 3: Open the cart and remove the item
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.CSS_SELECTOR, ".cart_button").click()
    
    # Step 4: Verify the cart is empty
    assert len(driver.find_elements(By.CSS_SELECTOR, ".cart_item")) == 0
    
    driver.quit()