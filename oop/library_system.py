# Base class for books
class Book:
    """A base class representing a book with a title and author."""
    
    def __init__(self, title, author):
        """Initialize the book with a title and an author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author}"


# Derived class for eBooks
class EBook(Book):
    """A class representing an eBook, derived from Book."""
    
    def __init__(self, title, author, file_size):
        """Initialize the eBook with a title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size  # file size in MB

    def __str__(self):
        """Return a string representation of the eBook."""
        return f"{super().__str__()} [EBook, File Size: {self.file_size}MB]"


# Derived class for PrintBooks
class PrintBook(Book):
    """A class representing a print book, derived from Book."""
    
    def __init__(self, title, author, page_count):
        """Initialize the print book with a title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count  # number of pages

    def __str__(self):
        """Return a string representation of the print book."""
        return f"{super().__str__()} [PrintBook, Pages: {self.page_count}]"


# Library class demonstrating composition
class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all the books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
