from selenium.webdriver.common.by import By

class BooksPageLocators:
    # Forms
    SEARCH_BOX = (By.CSS_SELECTOR, "#searchBox")

    # Elements
    BOOK_ROW = (By.XPATH, "//div[@role='rowgroup']")