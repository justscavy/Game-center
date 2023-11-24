import mysql.connector
import sys
from account_management.account import Account
#from class_user import user
from settings import games


def db_connect(host: str = "localhost", user: str = "root", password: str = "ubuntu123", database: str = "accounts_slf"):
    """Connect to DB."""
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )    
    return connection


def account_management():
    """create/login"""
    while True:                 #for invalid options
        print("Options:")
        option = input("1. Create Account\n2. Login to existing Account\n3. Quit\n-")
        if option == "1":
            create_account()        #create account
        elif option == "2":  
            user_id = login() # korrekt!
            games(user_id)
            return user_id                     
        elif option == "3":
            sys.exit()              #byebye
        else:
            print("Invalid option.")


def create_account():
    while True:
        connection = db_connect()
        try:
            cursor = connection.cursor()
            print("Creating account")
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
            connection.commit()
            print("Account created\n")
            connection.close()
            break
        except mysql.connector.Error:
            print("Account already exists. Please choose a different name.\n")


def login():
    connection = db_connect()
    try:
        cursor = connection.cursor()
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        cursor.execute("SELECT * FROM users WHERE name = %s AND password = %s", (name, password))
        result = cursor.fetchone()
        if result:
            user_id = result[0]
            name = result[1]
            print("Login successful!\n")
            return user_id, name
        else:
            print("Wrong name or password.")
            return None
    except mysql.connector.Error:
        print("im fixing already")
        return None  
    finally:
        connection.close()


#class Account:
#    """User account."""
#
#    id: int
#    name: str
#    password: str
def stats(user_id):
    connection = db_connect()
    cursor = connection.cursor()
    try:  
        cursor.execute("SELECT * FROM results WHERE user_id = %s", (user_id,))
        user_result = cursor.fetchall()
        if user_result:
            user_id = user_result[0][5]
            for row in user_result[-10:]:
                print(row)
            
            connection.commit()
            return user_id
            
    except mysql.connector.Error as err:
        
        print(f"damn, im on it!: {err}")
    finally:
        
        cursor.close()
        connection.close()



