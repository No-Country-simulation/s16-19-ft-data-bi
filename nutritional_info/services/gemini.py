import google.generativeai as genai
from pathlib import Path
import streamlit as st
import os

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def input_image_setup(file_loc):
    if not (img := Path(file_loc)).exists():
        raise FileNotFoundError(f"Could not find image: {img}")

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": Path(file_loc).read_bytes()
        }
    ]
    return image_parts

def generate_gemini_response(input_prompt, nutritional_info):
    try:
        response = model.generate_content([input_prompt + str(nutritional_info)])
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "No se pudo generar una respuesta adecuada."
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Error generando la respuesta."

def generate_gemini_response_with_image(input_prompt, image_loc):
    try:
        image_prompt = input_image_setup(image_loc)
        prompt_parts = [input_prompt, image_prompt[0]]
        response = model.generate_content(prompt_parts)
        return response.text
    except Exception as e:
        st.error(f"Error generating response with image: {e}")
        return "Error generando la respuesta con la imagen."