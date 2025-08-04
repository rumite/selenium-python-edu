from pages.books.books_page import BooksPage

class TestBooks:
    def test_find_books_by_publisher(self, driver):
        books_page = BooksPage(driver, "https://demoqa.com/books")
        books_page.open()
        books_page.fill_search_box("No Starch Press")
        books = books_page.get_displayed_books()

        assert len(books) == 2, f"Expected 2 books, but found {len(books)}"