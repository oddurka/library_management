

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.copies_available = total_copies

    def borrow(self) -> bool:
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        return False

    def return_book(self) -> None:
        if self.copies_available < self.total_copies:
            self.copies_available += 1
