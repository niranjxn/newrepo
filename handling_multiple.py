from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def multiple_elements():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.google.com")

        # Find all links on the page
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Total links found: {len(links)}")

        # Print first 10 links
        for i, link in enumerate(links[:10]):
            href = link.get_attribute("href")
            text = link.text
            if text:  # Only print links with visible text
                print(f"{i+1}. {text} -> {href}")
    finally:
        driver.quit()

multiple_elements()
