import streamlit as st
import os
from services.gemini import generate_gemini_response

input_prompt = """
               Como experto especializado en evaluar la idoneidad de frutas y alimentos para personas con diabetes, tu tarea implica analizar imágenes de entrada que presentan varios alimentos. Tu primer objetivo es identificar el tipo de fruta o alimento presente en la imagen. Posteriormente, debes determinar el índice glucémico del artículo identificado. Basándote en este índice glucémico, proporciona recomendaciones sobre si las personas con diabetes pueden incluir el alimento detectado en su dieta. Si se considera adecuado, especifica la cantidad recomendada para el consumo. PORFAVOR CONTESTA EN ESPANOL
               """

# Configurar Streamlit
st.set_page_config(
    page_title="Sistema de Recomendación de Dietas para Diabéticos",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Función para procesar la información nutricional
def get_nutritional_info(input_text=None, image=None, search_type=None):
    if search_type == "Código de barras" and input_text:
        st.write(f"Buscando información nutricional para el código de barras {input_text}...")
        # Implementar lógica para buscar información nutricional basada en el código de barras
        st.write("Información Nutricional Placeholder")
    elif search_type == "Nombre del producto" and input_text:
        st.write(f"Buscando información nutricional para el producto {input_text}...")
        # Implementar lógica para buscar información nutricional basada en el nombre del producto
        st.write("Información Nutricional Placeholder")
    elif search_type == "Imagen del producto" and image:
        st.write("Procesando imagen del producto...")
        image_path = save_uploadedfile(image)
        response = generate_gemini_response(input_prompt, image_path)
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


# Menú desplegable
st.sidebar.header("🛠️Secciones")
options = ["Información Nutricional", "Recomendaciones de Dieta", "Estadísticas"]
selection = st.sidebar.radio("Seleccionar Opción", options)

# Título de la página
st.title("🛠️Sistema de Recomendación de Dietas para Diabéticos")

if selection == "Información Nutricional":
    st.subheader("Información Nutricional")
    search_type = st.selectbox("Seleccione el tipo de búsqueda",
                               ["Código de barras", "Nombre del producto", "Imagen del producto"])

    if search_type in ["Código de barras", "Nombre del producto"]:
        input_text = st.text_input(f"Ingrese el {search_type.lower()}")
    else:
        input_text = None

    if search_type == "Imagen del producto":
        image_upload = st.file_uploader("Sube una imagen del producto", type=["jpg", "png"])
    else:
        image_upload = None

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
        # Implementar lógica para generar recomendaciones de dieta
        st.write("Recomendaciones Placeholder")

elif selection == "Estadísticas":
    st.subheader("Estadísticas")
