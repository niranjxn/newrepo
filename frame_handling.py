from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def frame_handling_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Switch to main frame on the page (where the example runs)
        driver.switch_to.frame("iframeResult")
        print("Switched to outer frame")

        # Inside that frame, there's another iframe — switch to it
        inner_frame = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(inner_frame)
        print("Switched to inner iframe")

        # Wait for and extract heading text inside inner iframe
        heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        print(f"Heading inside inner iframe: {heading}")

        # Switch back to the main document
        driver.switch_to.default_content()
        print("Switched back to main content")

        time.sleep(2)

    finally:
        driver.quit()

frame_handling_demo()
