from app.database import DatabaseConnection
import openai
import os

# Configurar la API Key de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_plan(user_data):
    # Generar el prompt para la API de OpenAI basado en los datos del usuario
    prompt = f"Genera un plan nutricional detallado para una persona con diabetes. Datos del usuario: {user_data}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
