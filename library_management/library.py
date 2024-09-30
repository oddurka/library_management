

from typing import List
from library_management.book import Book


class Library:
    def __init__(self):
        self.books = []
        self.transactions = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Copies available: {book.copies_available}\n")

    def find_book(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None

    def load_books(self, books: List[Book]) -> None:
        for book in books:
            self.add_book(book)
