import streamlit as st
from app.forms import user_form
from app.recommendations import generate_plan
from model.train_model import train_model
from model.train_model import train_final_model

def main():
    st.title("Sistema de Recomendación Nutricional para Personas con Diabetes")
    user_data = user_form()
    
    if st.button("Generar Plan Nutricional"):
        plan = generate_plan(user_data)
        st.write(plan)

    if st.button("Entrenar Modelo"):
        data = [torch.tensor([1.0] * 10) for _ in range(100)]  # Ejemplo de datos
        model = train_model(data)
        st.write("Modelo entrenado con éxito")

if __name__ == "__main__":
    main()
