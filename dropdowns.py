import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

# Select dropdown with selects
select_value_dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"));
# By value
select_value_dropdown.select_by_value("5")
time.sleep(3)
# By visible text
select_value_dropdown.select_by_visible_text("Yellow")
time.sleep(3)
# By index
select_value_dropdown.select_by_index(2)
time.sleep(3)