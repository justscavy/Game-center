from datetime import datetime

from write_results import db_results, Datawriter
from settings import counter, mode_slf, games
from accounts import account_management
from classes import Categories
from accounts import stats
#from write_results.Datawriter import WriteResults

from account_management.account import Account
from account_management.account_menu import account_menu
from account_management.account_manager import AccountManager
from db_management.db_manager import DBManager
#from settings_new import SLF

def main():
    print()
    print()
    print("    GameMania")
    print()
    print("Good luck & Have fun")
    print()
    # user_id, name = account_management() #login or create account
    db_manager: DBManager = DBManager()
    account_manager: AccountManager = AccountManager(db_manager=db_manager)
    account: Account = account_menu(account_manager=account_manager)
    #game: SLF = SLF(account=account)
    #game.main_menu()
    #game.run_game()
    
    letter, cat_list = games(account)    #choose games or results
    #letter = options_slf()
    # Das hier ins SLF.run_game()
    start_time_dt: datetime = datetime.now()
    start_time: str = start_time_dt.strftime("%Y-%m-%d %H:%M:%S")
    # Das hier in SLF unterbringen - Infos sind vorhanden
    """create dict with name and the choosen letter"""
    user_info: dict = {"Your Name: ": account.name, "Your Letter: ": letter} 
    """create list of defined objects"""
    #words: list = ["city: ", "country: ", "river: ", "name: ", "animal: ", "job: "
    #correct_answers, incorrect_answers = counter(words, letter, user_info)  #count wrong/right answers
    #cat = Categories()
    correct_answers, incorrect_answers = counter(cat_list=cat_list, letter=letter, user_info=user_info)  #count wrong/right answers

    end_time_dt: datetime = datetime.now()
    duration: datetime = end_time_dt - start_time_dt 
    print(f"Your time: {duration.total_seconds():.2f} sec")
    print(f"Correct answers: {correct_answers}")
    print(f"Incorrect answers: {incorrect_answers}")
    duration_format: float = (duration.total_seconds())
    dyn_filename = f"/home/ubuntuuser/py_practice/day1/SLF/results/{account.name}_{letter}_{duration_format:.2f}.txt"
    dyn_filename_csv = f"/home/ubuntuuser/py_practice/day1/SLF/results/{account.name}_{letter}_{duration_format:.2f}.csv"
    datawriter: Datawriter = Datawriter(dyn_filename,
                                        dyn_filename_csv,
                                        user_info,
                                        duration_format,
                                        correct_answers,
                                        incorrect_answers)
    datawriter.WriteResults()
    datawriter.WriteResults_csv()
    #writing_results(dyn_filename, user_info, duration_format, correct_answers, incorrect_answers) #outsourced function to write game results
    db_results(start_time, letter, duration_format, correct_answers, incorrect_answers, account.id)
    
if __name__ == "__main__":
    
    main()
    






