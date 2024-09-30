
import json
from typing import List
from library_management.book import Book
from library_management.library import Library
from library_management.menu import LibraryMenu
from library_management.transaction import Transaction
from library_management.user import Librarian, Member

def load_books_from_file(file_path: str) -> List[Book]:
    books = []
    with open(file_path, 'r') as file:
        books_data = json.load(file)

    for book_data in books_data:
        book = Book(
            title=book_data["title"],
            author=book_data["author"],
            isbn=book_data["isbn"],
            total_copies=book_data["total_copies"]
        )
        books.append(book)

    return books


def main():
    books = load_books_from_file("library_management/book_db.json")

    library = Library()
    librarian = Librarian(1, "Alice")
    member = Member(1, "Bob")

    library.load_books(books)
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 5)
    book2 = Book("The Da Vinci Code", "Dan Brown", "9780307474278", 3)

    library.add_book(book1)
    library.add_book(book2)

    menu = LibraryMenu(library, librarian, member)
    menu.login_menu()

if __name__ == "__main__":
    main()
