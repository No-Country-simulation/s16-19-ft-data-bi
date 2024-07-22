import pandas as pd
import streamlit as st
from database.connection import DatabaseConnection

def get_nutritional_info_from_db(column, value):
    db = DatabaseConnection()
    if db.connection:
        query = f"SELECT * FROM food WHERE {column} ILIKE '%{value}%'"
        columns, results = db.fetch_data(query)
        db.close_connection()
        if results and columns:
            df = pd.DataFrame(results, columns=columns)

            df_clean = df.dropna(axis=1, how='all').replace('', pd.NA).dropna(axis=1, how='all')

            clean_results = df_clean.to_dict(orient='records')
            if clean_results:
                result_dict = clean_results[0]
                print(f"Clean Results: {result_dict}")
                return result_dict
            else:
                return None
        else:
            st.error("No se encontraron resultados para la consulta.")
            return None
    else:
        st.error("No connection to the database.")
        return None
