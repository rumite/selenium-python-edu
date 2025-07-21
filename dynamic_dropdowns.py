import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/auto-complete")

autocomplete_field = driver.find_element(By.ID, "autoCompleteMultipleInput")
driver.execute_script("arguments[0].scrollIntoView(true);", autocomplete_field)
autocomplete_field.click()
autocomplete_field.send_keys("w")
time.sleep(3)
elements = driver.find_elements(By.CSS_SELECTOR, "div[id*='react-select']")

# Shows how much elements in the list
print(len(elements))

# Select an option in the list
for element in elements:
    if element.text == "Yellow":
        element.click()
        break
time.sleep(3)
