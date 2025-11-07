from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def fluent_wait_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    try:
        # Enter login credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Create a Fluent Wait
        wait = WebDriverWait(driver, timeout=15, poll_frequency=2, ignored_exceptions=[NoSuchElementException])

        # Wait for product list to become visible
        element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        print("Products are visible on the page!")

    finally:
        time.sleep(2)
        driver.quit()

fluent_wait_demo()