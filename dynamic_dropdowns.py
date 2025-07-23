import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/auto-complete")

autocomplete_field = driver.find_element(By.ID, "autoCompleteSingleInput")
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

selected_text = driver.find_element(By.CSS_SELECTOR, "div.auto-complete__single-value").text

assert "Yellow" == selected_text
time.sleep(3)
