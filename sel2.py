from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website_url = "https://www.youtube.com"
page_title_expected = "YouTube"

# Launch Chrome Browser
browser = webdriver.Chrome()
browser.get(website_url)

page_title_actual = browser.title
if page_title_expected in page_title_actual:
    print("Chrome: The title contains 'YouTube'")
else:
    print("Chrome: The title does not contain 'YouTube'")

time.sleep(2)
browser.quit()
