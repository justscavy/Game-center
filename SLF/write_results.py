import mysql.connector
from datetime import datetime
from accounts import db_connect
import csv

#def writing_results(dyn_filename: str, user_info: dict, duration_format: float, correct_answers: int, incorrect_answers: int):
#    with open(file=dyn_filename, mode="w") as f:  
#        f.write(f"Your time: {duration_format:.2f}sec\n")
#        f.write(f"Correct answers: {correct_answers}\n")
#        f.write(f"Incorrect answers: {incorrect_answers}\n\n")
#        for key, value in user_info.items():
#            f.write(f"{key}{value}\n")
            

def db_results(start_time: str, letter: str, duration_format: float, correct_answers: int, incorrect_answers: int, user_id: int):
    start_time_dt = datetime.now
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    connection = db_connect()
    cursor = connection.cursor()
    try:  
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        user_exists = cursor.fetchone()
        if user_exists:
           
            cursor.execute("INSERT INTO results (date, letter, duration, correct, incorrect, user_id) VALUES (%s, %s, %s, %s, %s, %s)",
                           (start_time, letter, duration_format, correct_answers, incorrect_answers, user_id))
            connection.commit()
            return user_id
    except mysql.connector.Error as err:
        print(f"that wasnt planned: {err}")
    finally:
        cursor.close()
        connection.close()


class Datawriter:
    """write data in .txt and csv file"""
    def __init__(self,
                 dyn_filename_csv: str,
                 dyn_filename: str, 
                 user_info: dict, 
                 duration_format: float,
                 correct_answers: int,
                 incorrect_answers: int) -> None:

                 self.dyn_filename_csv = dyn_filename_csv
                 self.dyn_filename = dyn_filename
                 self.user_info = user_info
                 self.duration_format = duration_format
                 self.correct_answers = correct_answers
                 self.incorrect_answers = incorrect_answers
                 

    def WriteResults(self)  -> None:
        with open(file=self.dyn_filename, mode="w") as f:  
            f.write(f"Your time: {self.duration_format:.2f}sec\n")
            f.write(f"Correct answers: {self.correct_answers}\n")
            f.write(f"Incorrect answers: {self.incorrect_answers}\n\n")
            for key, value in self.user_info.items():
                f.write(f"{key}{value}\n")



    def WriteResults_csv(self)  -> None:
        with open(file=self.dyn_filename_csv, mode="w", newline='') as f:
            rows = ["your time",
                      "correct answers",
                      "incorrect answers",
                      list(self.user_info.keys())
                      ]
            for key in rows:
                if key in self.user_info:
                    f.write(f"{key}{self.user_info[key]}\n")
            
         
