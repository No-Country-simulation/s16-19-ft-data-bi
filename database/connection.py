import os
import psycopg2
from psycopg2 import OperationalError

import streamlit as st
from dotenv import load_dotenv

def is_streamlit():
    try:
        return st._is_running_with_streamlit
    except:
        return False


class DatabaseConnection:
    def __init__(self):
        if is_streamlit():
            self.load_from_streamlit()
        else:
            self.load_from_env()

        try:
            self.connection = psycopg2.connect(
                host=self.db_host,
                port=self.db_port,
                database=self.db_name,
                user=self.db_user,
                password=self.db_password
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except OperationalError as e:
            self.handle_error(f"Error connecting to the database: {e}")
            self.connection = None
            self.cursor = None

    def load_from_streamlit(self):
        self.db_host = st.secrets["DB_HOST"]
        self.db_port = st.secrets["DB_PORT"]
        self.db_name = st.secrets["DB_NAME"]
        self.db_user = st.secrets["DB_USER"]
        self.db_password = st.secrets["DB_PASSWORD"]

    def load_from_env(self):
        load_dotenv()
        self.db_host = os.getenv("DB_HOST")
        self.db_port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")

    def fetch_data(self, query):
        if self.connection and self.cursor:
            try:
                self.cursor.execute(query)
                columns = [desc[0] for desc in self.cursor.description]
                results = self.cursor.fetchall()
                print(f"Columns: {columns}")
                print(f"Results: {results}")
                return columns, results
            except Exception as e:
                self.handle_error(f"Error executing query: {e}")
                return None, None
        else:
            self.handle_error("No connection to the database.")
            return None, None


    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def handle_error(self, message):
        if is_streamlit():
            st.error(message)
        else:
            print(f"Error: {message}")

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
