from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")

# By link text
home_link = driver.find_element(By.LINK_TEXT, "Home")
driver.execute_script("arguments[0].scrollIntoView(true);", home_link)
home_link.click()



