

from library_management.book import Book
from library_management.constants import BOOK_BORROW_LIMIT
from library_management.library import Library


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name


class Member(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.borrowed_books = []

    def borrow_book(self, book: Book) -> None:
        if len(self.borrowed_books) < BOOK_BORROW_LIMIT:
            if book.borrow():
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {book.title}\n")
            else:
                print(f"{book.title} is unavailable\n")
        else:
            print(f"{self.name} cannot borrow more than {BOOK_BORROW_LIMIT} books\n")


    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}\n")


class Librarian(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)

    def add_book(self, library: Library, book: Book) -> None:
        library.add_book(book)
        print(f"{self.name} added {book.title} to the library\n")
