import sys
import os
import toml

# Cargar las variables de configuración desde el archivo config.toml
config = toml.load('config.toml')

# Agregar el directorio principal del proyecto a sys.path
current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_path)
if project_root not in sys.path:
    sys.path.append(project_root)

import streamlit as st
from app.main import app_logic
from model.train_model import train_final_model
import torch

# Función principal de la aplicación
def main():
    # Entrenar el modelo al iniciar la aplicación
    data = [torch.tensor([1.0] * 10) for _ in range(100)]  # Ejemplo de datos
    model = train_final_model(data)
    print("Modelo entrenado con éxito")

    # Ejecutar la lógica de la aplicación
    app_logic()

if __name__ == "__main__":
    main()


