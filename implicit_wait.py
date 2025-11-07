from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def implicit_wait_demo():
    driver = webdriver.Chrome()
    # Set implicit wait (wait up to 10 seconds for elements)
    driver.implicitly_wait(10)
    try:
        driver.get("https://demoqa.com/login")

        # These will wait up to 10 seconds if elements are not immediately found
        username = driver.find_element(By.ID, "userName")
        password = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login")

        username.send_keys("test_user")
        password.send_keys("test_password")
        login_btn.click()
        print("Login button clicked")

        time.sleep(3)
    finally:
        driver.quit()

implicit_wait_demo()
