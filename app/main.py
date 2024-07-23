import streamlit as st
import torch
from app.forms import user_form
from app.recommendations import get_nutrition_recommendations
from model.train_model import train_final_model
from fpdf import FPDF

def app_logic():
    st.title("🍏 Sistema de Recomendación Nutricional para Personas con Diabetes")
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
        if st.button("📄 Exportar a PDF"):
            pdf_file_path = generate_pdf(plan)
            with open(pdf_file_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                st.download_button(label="Descargar PDF", data=pdf_bytes, file_name="plan_nutricional.pdf", mime='application/octet-stream')

def generate_pdf(plan):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Plan Nutricional para Personas con Diabetes", ln=True, align='C')
    pdf.ln(10)
    
    if isinstance(plan, dict):
        for meal, details in plan.items():
            pdf.cell(200, 10, f"{meal}:", ln=True, align='L')
            if isinstance(details, list):
                for detail in details:
                    pdf.cell(200, 10, f"- {detail}", ln=True, align='L')
            else:
                pdf.cell(200, 10, f"- {details}", ln=True, align='L')
            pdf.ln(5)
    else:
        pdf.cell(200, 10, "No se pudo generar el plan correctamente.", ln=True, align='L')
    
    pdf_file_path = "/tmp/plan_nutricional.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path

if __name__ == "__main__":
    # Entrenar el modelo al iniciar la aplicación
    data = [torch.tensor([1.0] * 10) for _ in range(100)]  # Ejemplo de datos
    model = train_final_model(data)
    print("Modelo entrenado con éxito")

    # Iniciar la lógica de la aplicación
    app_logic()
