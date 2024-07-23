import google.generativeai as genai
import toml
import streamlit as st

# Cargar las variables de configuración desde el archivo config.toml
config = toml.load('config.toml')

# Configurar la clave de API de Gemini
GEMINI_API_KEY = config['gemini']['api_key']
if GEMINI_API_KEY is None:
    raise Exception("API key for Gemini not found. Make sure it's set in the config.toml file.")

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

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config=generation_config,
    safety_settings=safety_settings
)

def generate_gemini_response(input_prompt, nutritional_info):
    try:
        response = model.generate_content([input_prompt + str(nutritional_info)])
        if response and hasattr(response, 'text'):
            return response.text
        else:
            return "No se pudo generar una respuesta adecuada."
    except IndexError as e:
        st.error(f"IndexError generating response: {e}")
        return "Error de índice al generar la respuesta."
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Error generando la respuesta."

def get_nutrition_recommendations(user_data):
    input_prompt = "Genera un plan nutricional detallado para una persona con diabetes como si fueras un nutricionista experto, basado en los siguientes datos: "
    recommendations = generate_gemini_response(input_prompt, user_data)
    return recommendations
