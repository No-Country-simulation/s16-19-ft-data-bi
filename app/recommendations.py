import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la clave de API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_plan(user_data):
    prompt = f"Genera un plan nutricional detallado para una persona con diabetes basado en los siguientes datos: {user_data}"

    # Usar la nueva API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un nutricionista experto en planes nutricionales para personas con diabetes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()
