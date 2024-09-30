

from library_management.library import Library
from library_management.user import Member


class MemberHandler:
    def __init__(self, member: Member, library: Library):
        self.member = member
        self.library = library

    def handle_borrow_book(self) -> None:
        title = input("Enter the title of the book: ")
        book = self.library.find_book(title)
        if book:
            self.member.borrow_book(book)
        else:
            print(f"{title} is not available at the moment\n")

    def handle_return_book(self,) -> bool:
        title = input("Enter the title of the book")
        for book in self.member.borrowed_books:
            if book.title == title:
                self.member.return_book(book)
                return True

        print(f"{self.member.name} hasn't borrowed the book titled: '{title}'\n")
        return False

