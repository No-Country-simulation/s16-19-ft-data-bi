import streamlit as st
import tempfile
import torch
import os
from model.train_model import train_final_model
from app.forms import user_form
from app.recommendations import get_nutrition_recommendations
from fpdf import FPDF

def app_logic():
    user_data = user_form()

    plan = None  # Inicializar la variable plan

    if st.button("🍽️ Generar Plan Nutricional"):
        # Generar plan nutricional
        try:
            plan = get_nutrition_recommendations(user_data)
            st.write("### Plan Nutricional Orientativo")
            st.write(plan)
        except Exception as e:
            st.error(f"Error al generar el plan nutricional: {e}")

    # Añadir opción para guardar o imprimir la recomendación
    if plan:
        st.write("📄 Haz click en ⋮ para Imprimir y en Destino: Guardar como PDF")
        # Generar PDF sin la opción de descargar directamente
        generate_pdf(plan)

def generate_pdf(plan):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Plan Nutricional para Personas con Diabetes", ln=True, align='C')
    pdf.ln(10)

    if isinstance(plan, dict):
        for meal, details in plan.items():
            pdf.cell(200, 10, txt=f"{meal}:", ln=True, align='L')
            if isinstance(details, list):
                for detail in details:
                    pdf.cell(200, 10, txt=f"- {detail}", ln=True, align='L')
            else:
                pdf.cell(200, 10, txt=f"- {details}", ln=True, align='L')
            pdf.ln(5)
    else:
        pdf.multi_cell(0, 10, plan)

    temp_dir = tempfile.gettempdir()
    pdf_file_path = os.path.join(temp_dir, "plan_nutricional.pdf")
    pdf.output(pdf_file_path)

    # Devolver la ruta del archivo PDF
    return pdf_file_path

if __name__ == "__main__":
    # Entrenar el modelo al iniciar la aplicación
    data = [torch.tensor([1.0] * 10) for _ in range(100)]  # Ejemplo de datos
    model = train_final_model(data)
    print("Modelo entrenado con éxito")

    # Iniciar la lógica de la aplicación
    app_logic()
