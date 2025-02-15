class Book:
    def __init__(self, title, page_count):
        '''Initializes the book with a title and page_count.'''
        self.title = title
        self.page_count = page_count  # Set the initial page count
        self._page_count = page_count  # Store the page count privately (for validation)

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        '''Ensures page_count is an integer.'''
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            self._page_count = None  # Optional: handle invalid input gracefully

    def turn_page(self):
        '''Simulates flipping the page of the book.'''
        print("Flipping the page...wow, you read fast!")
