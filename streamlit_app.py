import sys
import os

# Agregar el directorio principal del proyecto a sys.path
current_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_path)
if project_root not in sys.path:
    sys.path.append(project_root)

import streamlit as st
from app.main import app_logic

def main():
    app_logic()

if __name__ == "__main__":
    main()

# Añadir opción para guardar o imprimir la recomendación
st.button("📄 Exportar a PDF")
st.button("🖨️ Imprimir")


