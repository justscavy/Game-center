import random
import string
import sys
from accounts import stats
from classes import Categories


class SLF:
    def __init__(self, account) -> None:
        self.account = account
        self.categories: Categories = Categories()
        self.letter: str | None = None
        self.category_items: list[str] = []
        # self.main_menu()
        # self.run_game()

    def main_menu(self):
        while True:
            selected_game = input("Select a game\n1.StadtLandFluss\n2.game2\n3.Check ur Stats!\n4.exit\n--")
            print()
            if selected_game == "1":
                self.letter = self.get_letter()
                self.category_items = self.get_category_items()
            elif selected_game == "2":
                pass
            elif selected_game == "3":
                pass
                # user_id = stats()
            elif selected_game == "4":
                sys.exit()

    def get_letter(self) -> str:
        """Get a letter based on the user's input."""

        while True:
            selected_mode = input("Select a game mode:\n1. Choose a letter\n2. Generate a random letter\n--")
            print()
            if selected_mode == "1":
                selected_letter = input("Choose a letter: ")
                if len(selected_letter) == 1 and selected_letter.isalpha():
                    return selected_letter
                else:
                    print("Enter 1 letter only!\n")
            elif selected_mode == "2":
                selected_letter = random.choice(string.ascii_letters)
                print(f"Your letter is: {selected_letter}\n")
                return selected_letter
            else:
                print("Invalid Input\n")

    def get_category_items(self) -> list[str]:
        """Get a category items based on the user's input."""
        
        while True:
            selected_category = input("Choose ur category:\n1.Standard\n2.celeb\n3.nerd\n--").lower()
            print()
            if selected_category == "1":
                return self.categories.standard
            elif selected_category == "2":
                return self.categories.celeb
            elif selected_category == "3":
                return self.categories.nerd
            else:
                print("invalid option\n")

    def run_game(self, account):
        """count wrong/right answers FIX ME PLS"""

        incorrect_answers: int = 0
        correct_answers: int = 0
        
        for item in self.category_items:
            user_answer = input(f"{item}: ")
            if user_answer.casefold().startswith(self.letter.casefold()):
                print("correct")
                correct_answers += 1
            else:
                print("incorrect")
                incorrect_answers += 1
            account[item] = user_answer
        return correct_answers, incorrect_answers


# def games():
#     cat = Categories()
#     """choose which game to play"""
#     while True:
#         select_game = input("Select a game\n1.StadtLandFluss\n2.game2\n3.Check ur Stats!\n4.exit\n--")
#         print()
#         if select_game == "1":
#             letter, cat_list = mode_slf(cat
#             return letter, cat_list   
#         elif select_game == "2":
#             pass
#         elif select_game == "3":
#             user_id = stats()
#             pass
#         elif select_game == "4":
#             sys.exit()

# def mode_slf(categories: Categories):
#     """slf choose mode"""
#     while True:
#         cat_choice = input("Choose ur category:\n1.Standard\n2.celeb\n3.nerd\n--").lower()
#         print()
#         if cat_choice == "1":
#             cat_list = categories.standard
#             break
#         elif cat_choice == "2":
#             cat_list = categories.celeb
#             break
#         elif cat_choice == "3":
#             cat_list = categories.nerd
#             break
#         else:
#             print("invalid option\n")
        
    # while True:
    #     select_mod = input("Select a game mode:\n1. Choose a letter\n2. Generate a random letter\n--")
    #     print()
    #     if select_mod == "1":
    #         letter = input("Choose a letter: ")
    #         if len(letter) == 1 and letter.isalpha():
    #             break
    #         else:
    #             print("Enter 1 letter only!\n")
    #     elif select_mod == "2":
    #         letter = random.choice(string.ascii_letters)
    #         print(f"Your letter is: {letter}\n")
    #         break
    #     else:
    #         print("Invalid Input\n")
       
    # return letter, cat_list
       #correct_answers, incorrect_answers = counter(categories=cat, letter=letter, user_info=user_info)  #count wrong/right answers 

# def counter(cat_list: list[str], letter, user_info):
#     """count wrong/right answers FIX ME PLS"""
#     incorrect_answers: int = 0
#     correct_answers: int = 0
    
#     for item in cat_list:
#         user_answer = input(f"{item}: ")
#         if user_answer.casefold().startswith(letter.casefold()):
#             print("correct")
#             correct_answers += 1
#         else:
#             print("incorrect")
#             incorrect_answers += 1
#         user_info[item] = user_answer
#     return correct_answers, incorrect_answers