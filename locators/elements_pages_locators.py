from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    # Forms
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress.form-control")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress.form-control")

    # Buttons
    SUBMIT = (By.ID, "submit")

    # Output
    FULL_NAME_OUT = (By.CSS_SELECTOR, "#name")
    EMAIL_OUT = (By.CSS_SELECTOR, "email")
    CURRENT_ADDRESS_OUT = (By.CSS_SELECTOR, "#output #currentAddress")
    PERMANENT_ADDRESS_OUT = (By.CSS_SELECTOR, "#output #permanentAddress")


