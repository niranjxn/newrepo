from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def javascript_scroll_demo():
    driver = webdriver.Chrome()
    try:
        # 1. Navigate to the website
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        time.sleep(2)

        # 2. Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # 4. Scroll back to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        # 6. Scroll until "Mouse Hover" button is visible
        mouse_hover_button = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView();", mouse_hover_button)
        time.sleep(2)

    finally:
        # 7. Close the browser
        driver.quit()

javascript_scroll_demo()
