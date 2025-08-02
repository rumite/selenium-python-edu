import time

from locators.elements_pages_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Timur B")
        self.element_is_visible(self.locators.EMAIL).send_keys("test@test.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("ul. Pushkina d. Kolotushkina")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("ul. Bebry d. 47")
        submit = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(submit)
        submit.click()
        time.sleep(5)

