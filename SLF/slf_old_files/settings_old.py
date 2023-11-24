import random
import string
import sys
from accounts import stats
from classes import Categories

def games():
    """choose game"""
    while True:
        select_game = input("Select a game\n1.StadtLandFluss\n2.game2\n3.Check ur Stats!\n4.exit\n--")
        print()
        if select_game == "1":
            letter = mode_slf()
            return letter   
        elif select_game == "2":
            pass
        elif select_game == "3":
            user_id = stats()
            return user_id
            
        elif select_game == "4":
            sys.exit()
        

def mode_slf():
    
    while True:
        select_mod = input("Select a game mode:\n1. Choose a letter\n2. Generate a random letter\n--")
        print()
        if select_mod == "1":
            letter = input("Choose a letter: ")
            if len(letter) == 1 and letter.isalpha():
                break
            else:
                print("Enter 1 letter only!\n")
        elif select_mod == "2":
            letter = random.choice(string.ascii_letters)
            print(f"Your letter is: {letter}\n")
            break
        else:
            print("Invalid Input\n")
       
    return letter
        

def counter(categories: Categories, letter, user_info):
    
    incorrect_answers: int = 0
    correct_answers: int = 0
    while True:
        cat_choice = input("Choose ur category:\n1.Standard\n2.celeb\n3.nerd\n--").lower()
        print()
        if cat_choice == "1":
            cat_list = categories.standard
            break
        elif cat_choice == "2":
            cat_list = categories.celeb
            break
        elif cat_choice == "3":
            cat_list = categories.nerd
            break
        else:
            print("invalid option\n")
        
    

    for user_input in cat_list:
        user_answers = input(f"{user_input}: ")
        if user_answers.lower().startswith(letter.lower()):
            print("correct")
            correct_answers += 1
        else:
            print("incorrect")
            incorrect_answers += 1
        user_info[user_input] = user_answers
    return correct_answers, incorrect_answers