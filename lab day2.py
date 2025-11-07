from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def locators_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 1. ID Locator
        username = driver.find_element(By.ID, "username")
        username.send_keys("student")

        # 2. NAME Locator
        password = driver.find_element(By.NAME, "password")
        password.send_keys("Password123")

        # 3. CLASS_NAME Locator
        login_btn = driver.find_element(By.CLASS_NAME, "btn")
        login_btn.click()
        time.sleep(2)

        # 4. TAG_NAME Locator
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Number of links: {len(links)}")




    finally:
        driver.quit()


# Run the function
locators_demo()
