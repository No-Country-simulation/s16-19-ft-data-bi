import streamlit as st
from app.main import app_logic

def main():
    app_logic()

if __name__ == "__main__":
    main()

# Añadir opción para guardar o imprimir la recomendación
st.button("Save as PDF")
st.button("Print")
