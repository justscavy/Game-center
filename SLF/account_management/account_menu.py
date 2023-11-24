import sys

from account_management.account_manager import AccountManager
from account_management.account import Account


def account_menu(account_manager: AccountManager) -> Account:
    """"Startmenu for login/create_acc."""

    while True:
        print("Options:")

        options_str: str = (
            '1. Create Account\n'
            '2. Login to existing Account\n'
            '3. Quit\n'
        )

        choice = input(options_str)
        if choice == "1":
            return account_manager.create()
        elif choice == "2":  
            return account_manager.login()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid option.")