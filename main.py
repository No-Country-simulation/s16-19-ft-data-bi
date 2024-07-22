import streamlit as st
from nutritional_info.services.get_nutritional_info import get_nutritional_info

st.set_page_config(
    page_title="Sistema de Recomendación de Dietas para Diabéticos",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("️🍏 Secciones")
options = ["Información Nutricional", "Recomendaciones de Dieta", "Estadísticas"]
selection = st.sidebar.radio("Seleccionar Opción", options)

st.title("️🍏 Sistema de Recomendación Nutricional para Personas con Diabetes")

if selection == "Información Nutricional":
    st.subheader("Información Nutricional")
    search_type = st.selectbox("Seleccione el tipo de búsqueda",
                               ["Código de barras", "Nombre del producto", "Imagen del producto"])

    if search_type in ["Código de barras", "Nombre del producto"]:
        input_text = st.text_input(f"Ingrese el {search_type.lower()}")
        image_upload = None
    else:
        input_text = None

    if search_type == "Imagen del producto":
        image_upload = st.file_uploader("Sube una imagen del producto", type=["jpg", "png"])

    if st.button("Obtener Información Nutricional"):
        response = get_nutritional_info(input_text, image_upload, search_type)
        if response:
            st.write(response)

elif selection == "Recomendaciones de Dieta":
    st.subheader("Recomendaciones de Dieta")
    st.header("️🍏 Personalizar Recomendaciones")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Edad", min_value=0, max_value=120)
        weight = st.number_input("Peso (kg)", min_value=0)
        diabetes_type = st.selectbox("Tipo de Diabetes", ["Tipo 1", "Tipo 2", "Gestacional"])

    with col2:
        preferences = st.text_input("Preferencias Alimenticias")

    if st.button("Obtener Recomendaciones"):
        st.write("Generando recomendaciones personalizadas...")
        st.write("Recomendaciones Placeholder")

elif selection == "Estadísticas":
    st.subheader("Estadísticas")