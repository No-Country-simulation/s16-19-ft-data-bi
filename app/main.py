import streamlit as st
from app.forms import user_form
from app.recommendations import generate_plan

def main():
    st.title("Sistema de Recomendación Nutricional para Personas con Diabetes")
    user_data = user_form()
    
    if st.button("Generar Plan Nutricional"):
        plan = generate_plan(user_data)
        st.write(plan)

if __name__ == "__main__":
    main()
