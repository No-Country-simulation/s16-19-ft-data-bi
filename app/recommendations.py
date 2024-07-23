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
    input_prompt = (
        "Generar un plan nutricional detallado para una persona con diabetes. "
        "Considerar edad, género, peso y altura para empezar."
        "Personalizarlo adecuadamente para estación del año y país, en cuestión de elección de alimentos."
        "Enfocarse en nivel de actividad física, para aconcejar acertivamente un plan de actividad física semanal."
        "Considerar hora de sueño promedio por día, horarios de despertar y dormir, debido a que el plan nutricional debería seguir estos parámetros para definir el desayuno, la media mañana, el almuerzo, la media tarde, merienda y cena a lo largo de las horas activas."
        "Aconcejar sobre ordenar las horas de sueño, si las horas de sueño promedio por día, exceden las 8 horas."
        "Encuadrar el plan nutricional, considerando además las patologías subyacentes además de las de diabetes."
        "Enfocar en tipo de diabetes, 1 o 2 para mejorar la recomendación nutricional."
        "Las preferencias y restricciones dietéticas, deben analizarse según sean compatibles o no con una persona que padece diabetes más patologías subyacentes."
        "Importante que aquello no compatible con la diabetes y patología subyacente, se aconceje reemplazar por otro alimento."
        
    )
    recommendations = generate_gemini_response(input_prompt, user_data)
    return recommendations
