

from library_management.library import Library
from library_management.role_menus.librarian_menu import LibrarianMenu
from library_management.role_menus.member_menu import MemberMenu
from library_management.user import Librarian, Member


class LibraryMenu:
    def __init__(self, library: Library, librarian: Librarian, member: Member):
        self.library = library
        self.librarian = librarian
        self.member = member
        self.logged_in_user = None
        self.menu_options = []

    def login_menu(self) -> None:
        print("Choose a number:")
        print("1. Librarian")
        print("2. Member")
        print("3. Exit\n")
        choice = input("> ")

        match choice:
            case "1":
                self.logged_in_user = self.librarian
                LibrarianMenu(self.librarian, self.library).run_menu()
            case "2":
                self.logged_in_user = self.member
                MemberMenu(self.member, self.library).run_menu()
            case "3":
                print("Exiting program")
                exit()
            case _:
                print("Invalid choice")
                self.login_menu()
