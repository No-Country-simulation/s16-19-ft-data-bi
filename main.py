import os
import pandas as pd
import streamlit as st
from database.connection import DatabaseConnection
from services.gemini import generate_gemini_response, generate_gemini_response_with_image

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

def get_nutritional_info(input_text=None, image=None, search_type=None):
    if search_type == "Código de barras" and input_text:
        st.write(f"Buscando información nutricional para el código de barras {input_text}...")
        nutritional_info = get_nutritional_info_from_db('code', input_text)
        if nutritional_info:
            response = generate_gemini_response(input_prompt, nutritional_info)
            return response
        else:
            st.error("No se encontró información para el código de barras proporcionado.")
            return None
    elif search_type == "Nombre del producto" and input_text:
        st.write(f"Buscando información nutricional para el producto {input_text}...")
        nutritional_info = None
        for column in ['product_name', 'abbreviated_product_name', 'generic_name']:
            nutritional_info = get_nutritional_info_from_db(column, input_text)
            if nutritional_info:
                break
        if nutritional_info:
            response = generate_gemini_response(input_prompt, nutritional_info)
            return response
        else:
            st.error("No se encontró información para el nombre del producto proporcionado.")
            return None
    elif search_type == "Imagen del producto" and image:
        st.write("Procesando imagen del producto...")
        image_path = save_uploadedfile(image)
        response = generate_gemini_response_with_image(input_prompt_image, image_path)
        return response
    else:
        st.error("Por favor ingrese la información correcta según el tipo de búsqueda seleccionado.")
        return None

def save_uploadedfile(uploadedfile):
    if not os.path.exists("tempDir"):
        os.makedirs("tempDir")
    file_path = os.path.join("tempDir", uploadedfile.name)
    with open(file_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    return file_path

st.set_page_config(
    page_title="Sistema de Recomendación de Dietas para Diabéticos",
    layout="wide",
    initial_sidebar_state="expanded",
)

input_prompt = """
Como experto especializado en evaluar la idoneidad de frutas y alimentos para personas con diabetes, tu tarea implica analizar alimentos. Tu primer objetivo es identificar el tipo de fruta o alimento presente en el código de barras. Posteriormente, debes determinar el índice glucémico del artículo identificado. Basándote en este índice glucémico, proporciona recomendaciones sobre si las personas con diabetes pueden incluir el alimento detectado en su dieta. Si se considera adecuado, especifica la cantidad recomendada para el consumo. POR FAVOR CONTESTA EN ESPAÑOL.
"""

input_prompt_image = """
Como experto especializado en evaluar la idoneidad de frutas y alimentos para personas con diabetes, tu tarea implica analizar imágenes de alimentos. Tu primer objetivo es identificar el tipo de fruta o alimento presente en la imagen. Posteriormente, debes determinar el índice glucémico del artículo identificado. Basándote en este índice glucémico, proporciona recomendaciones sobre si las personas con diabetes pueden incluir el alimento detectado en su dieta. Si se considera adecuado, especifica la cantidad recomendada para el consumo. POR FAVOR CONTESTA EN ESPAÑOL.
"""

st.sidebar.header("🛠️Secciones")
options = ["Información Nutricional", "Recomendaciones de Dieta", "Estadísticas"]
selection = st.sidebar.radio("Seleccionar Opción", options)

st.title("🛠️Sistema de Recomendación de Dietas para Diabéticos")

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
    st.header("🔧 Personalizar Recomendaciones")

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