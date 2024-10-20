import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Change if your server is different
            user='root',  # Replace with your MySQL username
            password='uArC98zp@8n@XPmjLWnT'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
