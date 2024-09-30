from datetime import datetime, timedelta

from library_management.book import Book
from library_management.user import User

class Transaction:
    def __init__(self, book: Book, user: User):
        self.book = book
        self.user = user
        self.borrow_date = datetime.now()
        self.return_date = None

    def return_book(self) -> None:
        self.return_date = datetime.now()
        delta = self.return_date - self.borrow_date
        if delta.days > 14:
            fine = (delta.days - 14) * 1 # $1 per day
            print(f"{self.user.name} is {delta.days - 14} days late.\nFine: ${fine}\n")
        else:
            print(f"{self.user.name} returned {self.book.title} on time\n")
