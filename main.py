import streamlit as st
from nutritional_info.services.get_nutritional_info import get_nutritional_info
import streamlit.components.v1 as components
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

    # URLs de los reportes de Power BI publicados
    powerbi_urls = [
        "https://app.powerbi.com/view?r=eyJrIjoiY2M1YjYzODAtMjBjOC00OTE0LWI4NDAtMzYwYTQyY2FlODlhIiwidCI6ImZhZTJmNWI5LTY3MTEtNGYyYy1iYWUzLTI2ZGIzM2M2M2QzZCIsImMiOjR9",
        "https://app.powerbi.com/view?r=eyJrIjoiY2ZlZWM3OTYtZDU3OC00ZGFmLTk4OGMtODQ0MWVkZDc0NmVkIiwidCI6ImI4OGNjNWQyLWMxMjctNDc1My1iZDJiLWFlZWZiNDU2N2FkMiIsImMiOjR9"
    ]

    for url in powerbi_urls:
        st.markdown(f"### Reporte de Power BI")
        components.html(
            f"""
            <iframe width="800" height="600" src="{url}" frameborder="0" allowFullScreen="true"></iframe>
            """,
            height=600,
        )
        st.markdown("---")
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