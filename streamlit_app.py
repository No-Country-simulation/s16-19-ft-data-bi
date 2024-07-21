import streamlit as st
import openai
import pandas as pd
import torch
import torch.nn as nn
import os
from PIL import Image
from utils import load_datasets, preprocess_data, load_model, calculate_nutritional_plan, translate_conditions, format_recommendation
from dotenv import load_dotenv
from model import NutritionalRecommendationModel

# Carga variables de entorno desde el archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Carga el modelo entrenado con los mejores hiperparámetros
class NutritionalRecommendationModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NutritionalRecommendationModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Define hiperparámetros con los valores óptimos encontrados por Optuna
input_size = 6  # Define el tamaño de entrada, ajusta según el número de características de entrada
hidden_size = 64  # Valor encontrado por Optuna
output_size = 1  # Ajusta según sea necesario

# Se crea el modelo con los mejores hiperparámetros
model = NutritionalRecommendationModel(input_size, hidden_size, output_size)
model = load_model(model, 'saved_model/nutritional_recommendation_model.pth')

# Imágenes de fondo y logo
bg_image = Image.open("images/BK.png")
logo_image = Image.open("images/DH.png")

# Configuración de la página
st.set_page_config(page_title="Nutritional Recommendation System", page_icon="🍏")

# Mostrar logo
st.image(logo_image, width=100)

# Título de la aplicación
st.title("Nutritional Recommendation System for Diabetic Patients | APP")

# Ingresar datos del usuario
st.header("Enter your details")

weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
sleep_hours = st.number_input("Average sleep hours per night")
start_time = st.time_input("Start time of daily activity")
end_time = st.time_input("End time of daily activity")
activity_level = st.selectbox("Physical activity level", ["Low", "Moderate", "Intense"])
season = st.selectbox("Season of the year", ["Winter", "Spring", "Summer", "Fall"])
dietary_preference = st.text_input("Dietary Preference (enter a food you don't like)")
comorbidities = st.multiselect("Comorbidities", ["Cardiovascular Diseases", "Hypertension", "Dyslipidemia", "Gastroparesis", "Liver Disease", "Diabetic Nephropathy", "Overweight/Obesity"])
diabetes_type = st.selectbox("Type of Diabetes", ["Type 1", "Type 2"])

# Codificar las características categóricas
def encode_feature(feature, options):
    return options.index(feature)

# Función para obtener recomendaciones de la API de OpenAI
def get_recommendation(user_data):
    prompt = f"""
    Generate a nutritional plan for a diabetic patient with the following details:
    Weight: {user_data['weight']} kg
    Height: {user_data['height']} cm
    Sleep Hours: {user_data['sleep_hours']} hours per night
    Activity Start Time: {user_data['start_time']}
    Activity End Time: {user_data['end_time']}
    Activity Level: {user_data['activity_level']}
    Season: {user_data['season']}
    Dietary Preference: {user_data['dietary_preference']}
    Comorbidities: {', '.join(translate_conditions(user_data['comorbidities']))}
    Diabetes Type: {user_data['diabetes_type']}
    
    Provide a detailed nutritional plan including Breakfast, Mid-Morning, Lunch, Afternoon Snack, Dinner, and Evening Snack with portion sizes in grams. Consider the user's dietary preferences and comorbidities.
    """
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Procesar los datos y generar la recomendación
if st.button("Generate Recommendation"):
    user_data = {
        'weight': weight,
        'height': height,
        'sleep_hours': sleep_hours,
        'start_time': start_time.strftime("%H:%M"),
        'end_time': end_time.strftime("%H:%M"),
        'activity_level': encode_feature(activity_level, ["Low", "Moderate", "Intense"]),
        'season': encode_feature(season, ["Winter", "Spring", "Summer", "Fall"]),
        'dietary_preference': dietary_preference,
        'comorbidities': comorbidities,
        'diabetes_type': encode_feature(diabetes_type, ["Type 1", "Type 2"])
    }
    
    recommendation = get_recommendation(user_data)
    formatted_recommendation = format_recommendation(recommendation)
    
    st.subheader("Nutritional Plan")
    st.write(formatted_recommendation)

# Añadir opción para guardar o imprimir la recomendación
st.button("Save as PDF")
st.button("Print")