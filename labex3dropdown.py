from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def dropdown_demo():
    driver = webdriver.Chrome()
    try:
        # 1. Navigate to website
        driver.get("https://demo.automationtesting.in/Register.html")
        driver.maximize_window()
        time.sleep(2)

        # 2. Single-select dropdown: Skills
        skills_dropdown = Select(driver.find_element(By.ID, "Skills"))
        skills_dropdown.select_by_visible_text("Adobe Photoshop")
        time.sleep(1)

        # # 3. Single-select dropdown: Country
        # country_dropdown = Select(driver.find_element(By.ID, "countries"))
        # country_dropdown.select_by_value("Japan")
        # time.sleep(1)

        # 4. Single-select dropdown: Year (Date of Birth)
        year_dropdown = Select(driver.find_element(By.ID, "yearbox"))
        year_dropdown.select_by_index(5)  # Select 6th option (index starts from 0)
        time.sleep(1)

        # 5. Multi-select dropdown: Languages
        languages_box = driver.find_element(By.ID, "msdd")
        languages_box.click()
        time.sleep(1)

        # 6. Select English and French
        english_option = driver.find_element(By.XPATH, "//a[text()='English']")
        french_option = driver.find_element(By.XPATH, "//a[text()='French']")
        english_option.click()
        french_option.click()
        time.sleep(1)

        # Click outside to close the dropdown
        driver.find_element(By.XPATH, "//label[text()='Skills']").click()
        time.sleep(1)

    finally:
        # 7. Close the browser
        driver.quit()

dropdown_demo()
