from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def radio_checkbox_demo():
    driver = webdriver.Chrome()
    try:
        # Step 1: Open the practice website
        driver.get("https://demo.automationtesting.in/Register.html")
        driver.maximize_window()
        time.sleep(2)

        # Step 2: Locate and click the "Male" radio button
        male_radio = driver.find_element(By.XPATH, "//input[@value='Male']")
        male_radio.click()
        time.sleep(1)

        # Step 3: Check if "Male" is selected and print status
        print("Male radio selected:", male_radio.is_selected())

        # Step 4: Locate and click "Cricket" checkbox
        cricket_checkbox = driver.find_element(By.XPATH, "//input[@value='Cricket']")
        cricket_checkbox.click()
        time.sleep(1)

        # Step 5: Locate and click "Movies" checkbox
        movies_checkbox = driver.find_element(By.XPATH, "//input[@value='Movies']")
        movies_checkbox.click()
        time.sleep(1)

        # Step 6: Click "Movies" again to de-select
        movies_checkbox.click()
        time.sleep(1)

        # Step 7: Print status of "Cricket" and "Movies" checkboxes
        print("Cricket checkbox selected:", cricket_checkbox.is_selected())
        print("Movies checkbox selected:", movies_checkbox.is_selected())

    finally:
        # Step 8: Close the browser
        driver.quit()

# Run the demo
radio_checkbox_demo()
