import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")

driver.find_element(By.XPATH, "//button[@title='Expand all']").click()
time.sleep(3)
