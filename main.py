import streamlit as st
from nutritional_info.services.get_nutritional_info import get_nutritional_info
from app.main import app_logic

st.set_page_config(
    page_title="Sistema de Recomendación de Dietas para Diabéticos",
    layout="wide",
    initial_sidebar_state="expanded",
)
logo_path = "assets/DH.png"
st.sidebar.image(logo_path, width=150)
st.sidebar.header("️🍏 Secciones")
options = ["📈 Visualizaciones y Análisis", "🔍 Búsqueda de Información Nutricional", "🍽️ Recomendación de Plan Nutricional"]
selection = st.sidebar.radio("Seleccionar Opción", options)

st.title("️🍏 Sistema de Recomendación Nutricional para Personas con Diabetes")

if selection == "📈 Visualizaciones y Análisis":
    st.subheader("📈 Visualizaciones y Análisis")

elif selection == "🔍 Búsqueda de Información Nutricional":
    st.subheader("🔍 Búsqueda de Información Nutricional")
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

elif selection == "🍽️ Recomendación de Plan Nutricional":
    st.subheader("🍽️ Recomendación de Plan Nutricional")
    app_logic()