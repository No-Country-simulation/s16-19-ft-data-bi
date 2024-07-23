import streamlit as st
from datetime import time

def user_form():
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    altura = st.number_input("Altura (cm)", min_value=0.0, step=0.1)
    pais = st.text_input("País")
    estacion = st.selectbox("Estación del Año?", ["Verano", "Otoño", "Primavera", "Invierno"])
    nivel_actividad = st.selectbox("Nivel de Actividad Física", ["Bajo", "Moderado", "Intenso"])
    horas_sueno = st.number_input("Horas de Sueño Promedio por Día", min_value=0, max_value=24, step=1)
    inicio_act = st.time_input("Hora de Despertarse", time(6, 0))  # Valor predeterminado 6:00 AM
    fin_act = st.time_input("Hora de Dormirse", time(23, 0))  # Valor predeterminado 11:00 PM
    patologia = st.multiselect("Patología Subyacente", ["Enfermedad Cardiovascular", "Hipertensión", "Dislipemia", "Gastroparesia", "Hígado Graso"])
    tipo_diabetes = st.selectbox("Tipo de Diabetes", ["Tipo I", "Tipo II"])
    preferencia_dietetica = st.text_input("Preferencia Dietética")
    restriccion_dietetica = st.text_input("Restricción Dietética")

    return {
        "edad": edad,
        "genero": genero,
        "peso": peso,
        "altura": altura,
        "pais": pais,
        "estacion": estacion,
        "nivel_actividad": nivel_actividad,
        "horas_sueno": horas_sueno,
        "inicio_act": inicio_act,
        "fin_act": fin_act,
        "patologia": patologia,
        "tipo_diabetes": tipo_diabetes,
        "preferencia_dietetica": preferencia_dietetica,
        "restriccion_dietetica": restriccion_dietetica
    }
