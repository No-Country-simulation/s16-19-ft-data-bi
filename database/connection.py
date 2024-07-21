import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None
            self.cursor = None

    def fetch_data(self, query):
        if self.connection and self.cursor:
            try:
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Exception as e:
                print(f"Error executing query: {e}")
                return None
        else:
            print("No connection to the database.")
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    db = DatabaseConnection()

    if db.connection:
        query = "SELECT * FROM food LIMIT 10"
        results = db.fetch_data(query)

        if results:
            for row in results:
                print(row)

        db.close_connection()
    else:
        print("No connection to the database.")
