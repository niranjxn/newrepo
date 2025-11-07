from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def registration_automation():
    driver = webdriver.Chrome()
    try:
        # Step 1: Go to index page
        driver.get("https://demo.automationtesting.in/Index.html")
        driver.maximize_window()
        time.sleep(2)

        # Step 2: Click "Skip Sign In"
        driver.find_element(By.ID, "btn2").click()
        time.sleep(3)

        # Step 3: Enter First Name (placeholder)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Niranjan")
        time.sleep(1)

        # Step 4: Enter Last Name (ng-model)
        driver.find_element(By.XPATH, "//input[@ng-model='LastName']").send_keys("Revant")
        time.sleep(1)

        # ✅ Step 5: Enter Address (using ng-model instead of rows/cols)
        driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys("123, Main Street, Hyderabad")
        time.sleep(1)

        # Step 6: Get header text
        header_text = driver.find_element(By.TAG_NAME, "h1").text

        # Step 7: Print the header
        print("Header Text:", header_text)

        # Step 8: Navigate back
        driver.back()
        time.sleep(2)

    finally:
        # Step 9: Close browser
        driver.quit()

# Run
registration_automation()
