import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

MY_NAME = "Timur"

driver.find_element(By.ID, "userName").send_keys(MY_NAME)

# XPath //tagname[@attribute='value']
email_form = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']")
email_form.send_keys("bakhtiyarowtn@gmail.com")

# Scroll to Submit button

SUBMIT_BTN_XPATH = "//button[text()='Submit']"
submit_btn = driver.find_element(By.XPATH, SUBMIT_BTN_XPATH)
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()

message_name = driver.find_element(By.ID, "name").text
message_email = driver.find_element(By.CSS_SELECTOR, "[id='email']").text

# Print what we see after clicking submit
print(message_name)
print(message_email)

# Add assertion
assert MY_NAME in message_name