from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os

def screenshot_and_broken_link_demo():
    driver = webdriver.Chrome()
    try:
        # 1. Navigate to the website
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        time.sleep(2)

        # 2. Take a screenshot of the current browser window
        screenshot_path = os.path.join(os.getcwd(), "practice_page.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

        # 3. Find the "Broken Link" element by its link text
        broken_link = driver.find_element(By.LINK_TEXT, "Broken Link")

        # 4a. Get the href attribute (URL)
        url = broken_link.get_attribute("href")
        print(f"Checking URL: {url}")

        # 4b. Send a GET request using requests
        response = requests.get(url)

        # 4c. Check status code
        if response.status_code == 404:
            print("The link is broken!")
        else:
            print("The link is valid.")

        time.sleep(2)

    finally:
        # 6. Close the browser
        driver.quit()

screenshot_and_broken_link_demo()
