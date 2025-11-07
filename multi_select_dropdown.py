from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def multi_select_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/select-menu")

        # Multi-select dropdown
        multi_select = Select(driver.find_element(By.ID, "cars"))

        # Select multiple options
        multi_select.select_by_visible_text("Volvo")
        multi_select.select_by_visible_text("Audi")
        time.sleep(2)

        # Get all selected options
        selected_options = multi_select.all_selected_options
        for option in selected_options:
            print(f"Selected: {option.text}")

        # Deselect an option
        multi_select.deselect_by_visible_text("Volvo")
        time.sleep(2)

        # Deselect all
        multi_select.deselect_all()

    finally:
        driver.quit()

multi_select_demo()
