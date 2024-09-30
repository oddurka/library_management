

from library_management.handlers.librarian_handler import LibrarianHandler
from library_management.library import Library
from library_management.user import Librarian


class LibrarianMenu:
    def __init__(self, librarian: Librarian, library: Library):
        self.librarian = librarian
        self.library = library
        self.librarian_handler = LibrarianHandler(librarian)

    def run_menu(self):
        while True:
            print("Choose a number:")
            print("1. Add book")
            print("2. Check book status")
            print("3. Logout")
            print("q. Exit\n")

            choice = input("> ")

            match choice:
                case "1":
                   self.librarian_handler.handle_add_book(self.library)
                case "2":
                    print("NOT IMPLEMENTED YET\n")
                case "3":
                    print(f"Logging out")
                    self.member = None
                case "q":
                    print("Exiting program\n")
                    break
                case _:
                    print("Invalid choice\n")
                    self.run_menu()
