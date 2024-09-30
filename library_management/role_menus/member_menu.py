


from library_management.handlers.member_handler import MemberHandler
from library_management.library import Library
from library_management.user import Member


class MemberMenu:
    def __init__(self, member: Member, library: Library) -> None:
        self.member = member
        self.library = library
        self.member_handler = MemberHandler(member, library)

    def run_menu(self) -> None:
        while True:
            print("Choose a number:")
            print("1. Borrow book")
            print("2. Return book")
            print("3. Logout")
            print("q. Exit\n")

            choice = input("> ")

            match choice:
                case "1":
                    self.member_handler.handle_borrow_book()
                case "2":
                    self.member_handler.handle_return_book()
                case "3":
                    print(f"Logging out\n")
                    self.member = None
                case "q":
                    print("Exiting program\n")
                    break
                case _:
                    print("Invalid choice\n")
                    self.run_menu()
