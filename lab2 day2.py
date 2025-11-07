from selenium import webdriver
from selenium.webdriver.common.by import By

def xpath_examples():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.saucedemo.com")

        # Absolute XPath
        # username = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")

        # Relative XPath by attribute
        username = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username.send_keys("standard_user")

        # XPath with multiple attributes
        password = driver.find_element(By.XPATH, "//input[@id='password' and @name='password']")
        password.send_keys("secret_sauce")

        # XPath by text
        login_btn = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_btn.click()

        # XPath contains
        menu_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Open Menu')]")

        # XPath starts-with
        # menu_btn = driver.find_element(By.XPATH, "//button[starts-with(@id, 'react')]")

    finally:
        driver.quit()

xpath_examples()
