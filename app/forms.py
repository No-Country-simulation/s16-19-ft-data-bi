import streamlit as st

def user_form():
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    altura = st.number_input("Altura (cm)", min_value=0.0, step=0.1)
    pais = st.text_input("País")
    nivel_actividad = st.selectbox("Nivel de Actividad Física", ["Bajo", "Moderado", "Intenso"])
    horas_sueno = st.number_input("Horas de Sueño Promedio por Día", min_value=0, max_value=24, step=1)
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
        "nivel_actividad": nivel_actividad,
        "horas_sueno": horas_sueno,
        "patologia": patologia,
        "tipo_diabetes": tipo_diabetes,
        "preferencia_dietetica": preferencia_dietetica,
        "restriccion_dietetica": restriccion_dietetica
    }
