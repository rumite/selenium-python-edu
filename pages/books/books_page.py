from locators.books_pages_locators import BooksPageLocators
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BooksPage(BasePage):
    locators = BooksPageLocators()

    def fill_search_box(self, keys):
        self.element_is_visible(self.locators.SEARCH_BOX).send_keys(keys)

    def get_displayed_books(self):
        all_rows = self.driver.find_elements(*self.locators.BOOK_ROW)
        valid_rows = []

        for row in all_rows:
            cells = row.find_elements(By.CLASS_NAME, "rt-td")
            if any(cell.text.strip() != "" for cell in cells):
                valid_rows.append(row)

        return valid_rows