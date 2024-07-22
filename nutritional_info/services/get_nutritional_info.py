import streamlit as st
from database.queries.get_nutritional_info_from_db import get_nutritional_info_from_db
from nutritional_info.services.gemini import generate_gemini_response
from nutritional_info.services.gemini import generate_gemini_response_with_image
from nutritional_info.prompt_templates.input_prompt import input_prompt
from nutritional_info.prompt_templates.input_prompt_image import input_prompt_image
from nutritional_info.utils.file_handling import save_uploadedfile

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