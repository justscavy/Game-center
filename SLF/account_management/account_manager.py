from .account import Account
from db_management.db_manager import DBManager

class AccountManager:
    """Allows account management."""

    def __init__(self, db_manager: DBManager) -> None:
        self.db_manager = db_manager

    def create(self) -> Account:
        """Create a newaccount."""

        while True:
            print("Creating account")
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            result = self.db_manager.create_account(name, password)

            if result:
                print("Account created\n")
                return Account(id=result, name=result, password=result)
            else:
                print("Account already exists. Please choose a different name.\n")
                

    def login(self) -> Account | None:
        """"Login to an existing account."""
        while True:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            result = self.db_manager.get_account(name=name, password=password)
            if result:
                print("Login successful!\n")
                return Account(id=result[0], name=result[1], password=result[2])
            else:
                print("Wrong name or password.")
                

