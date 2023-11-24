import mysql.connector


class DBManager:
    """Connect to DB."""

    def __init__(
        self,
        host: str = "localhost",
        user: str = "root",
        password: str = "ubuntu123",
        database: str = "accounts_slf"
    ) -> None:
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    
    def get_account(self, name: str, password: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE name = %s AND password = %s", (name, password))
            result = cursor.fetchone()
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"SQL query failed. Details: '{e}'")
            
        return result
        
    def create_account(self, name: str, password: str):
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, password))
            #result = cursor.fetchone()
            self.connection.commit()
            if cursor.rowcount > 0:
                return True
            else:
                return False
        except mysql.connector.Error as e:
            print(f"SQL query failed. Details: '{e}'")
            return False
            
            

            
            


    def __del__(self):
        self.connection.close()