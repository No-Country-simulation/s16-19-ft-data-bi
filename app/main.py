import streamlit as st
from app.forms import user_form
from app.recommendations import generate_plan
from model.train_model import train_final_model
import torch
from fpdf import FPDF

def generate_pdf(plan):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)

    pdf.cell(200, 10, txt = "Plan Nutricional para Personas con Diabetes", ln = True, align = 'C')
    pdf.ln(10)
    
    for meal, details in plan.items():
        pdf.cell(200, 10, txt = f"{meal}:", ln = True, align = 'L')
        for detail in details:
            pdf.cell(200, 10, txt = f"- {detail}", ln = True, align = 'L')
        pdf.ln(5)
    
    pdf_file_path = "/tmp/plan_nutricional.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path

def main():
    st.title("Sistema de Recomendación Nutricional para Personas con Diabetes")
    user_data = user_form()
    
    if st.button("Generar Plan Nutricional"):
        plan = generate_plan(user_data)
        st.write(plan)
        
        pdf_file_path = generate_pdf(plan)
        
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(label="Descargar PDF", data=pdf_bytes, file_name="plan_nutricional.pdf", mime='application/octet-stream')

    if st.button("Entrenar Modelo"):
        data = [torch.tensor([1.0] * 10) for _ in range(100)]  # Ejemplo de datos
        model = train_final_model(data)
        st.write("Modelo entrenado con éxito")

if __name__ == "__main__":
    main()

