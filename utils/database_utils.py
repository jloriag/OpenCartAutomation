import mysql.connector
from mysql.connector import Error

class DatabaseUtils:

    @staticmethod
    def create_mysql_database(host, user, password, db_name):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            if connection.is_connected():
                print("Connected to MySQL server")
                cursor = connection.cursor()
                create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
                cursor.execute(create_db_query)
                print(f"MySQL Database '{db_name}' created successfully.")
                use_db_query = f"USE {db_name};"
                cursor.execute(use_db_query)
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")