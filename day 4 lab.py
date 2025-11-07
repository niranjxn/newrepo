from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to buttons page
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    # Move to "Double Click Me" button and double click
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.move_to_element(double_click_btn).double_click(double_click_btn).perform()
    time.sleep(2)
    print("Double click message:", driver.find_element(By.ID, "doubleClickMessage").text)

    # Move to "Right Click Me" button and context click
    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.move_to_element(right_click_btn).context_click(right_click_btn).perform()
    time.sleep(2)
    print("Right click message:", driver.find_element(By.ID, "rightClickMessage").text)

    # Move to "Click Me" button and click
    click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    actions.move_to_element(click_me_btn).click(click_me_btn).perform()
    time.sleep(2)
    print("Click Me button clicked")

    # Navigate to droppable page
    driver.get("https://demoqa.com/droppable")
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    # Drag and drop using drag_and_drop
    actions.drag_and_drop(source, target).perform()
    time.sleep(2)
    print("Target text after drag_and_drop:", target.text)

    # Drag and drop by offset
    actions.click_and_hold(source).move_by_offset(150, 0).release().perform()
    time.sleep(2)
    print("Performed drag_and_drop_by_offset")

finally:
    driver.quit()
