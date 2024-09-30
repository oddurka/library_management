

from library_management.book import Book
from library_management.library import Library
from library_management.user import Librarian


class LibrarianHandler:
    def __init__(self, librarian: Librarian):
        self.librarian = librarian

    def handle_add_book(self, library: Library) -> None:
        title = input("Enter book title: ")
        author = input("Enter the author: ")
        isbn = input("Enter ISBN number: ")
        total_copies = int(input("Enter number of how many copies: "))

        book = Book(title, author, isbn, total_copies)

        try:
            self.librarian.add_book(library, book)
            print(f"Book '{title}' by {author} added successfully.")
        except Exception as e:
            print(f"Error adding book: {e}")
