**This repository is part of No Country's Simulation Tech Program in Data-BI.**

💎 **Nombre del Producto**

![logo](https://github.com/No-Country-simulation/s16-19-ft-data-bi/blob/bf4bb2563273080a8798ecab892a77b0c960606b/DH.png)

📊 **Rubro**

Orientado a Healthtech. Sistema de Recomendación Nutricional para Pacientes Diabéticos.

🍏 **Análisis**

Completar...

🍏 **Implementación**

El Sistema de Recomendación Nutricional para Pacientes Diabéticos desarrollado utiliza una combinación de datasets personalizados que son extraídos previamente de una base de datos en PostgresSQL, donde mediante un proceso de ETL, se extrajo lo más útil y significativo además de que se hizo una estructuración de los mismos.
Luego, se integra la API de OpenAI, técnicas avanzadas de optimización de hiperparámetros, y un modelo de lenguaje grande (LLM) para proporcionar planes nutricionales personalizados. En resumen, se plantea una integración híbrida. 
Los componentes y el flujo del sistema son:

**1. Datasets como Base de Datos**

- Bases de Datos Iniciales: En PostgresSQL, se recopila y almacenan los datos iniciales relacionados a parámetros, marcadores e indicadores de pacientes diabéticos, así como también de alimentos, proteínas, entre otros.
  
- Preprocesamiento: Los datos se cargan y se preprocesan para eliminar valores nulos y normalizar las características, asegurando así que el modelo de machine learning recibe datos de calidad.
  
- Carga de Datos: Se utilizan múltiples archivos CSV (dataset1.csv, dataset2.csv, dataset3.csv, dataset4.csv) que contienen información relevante para la creación de planes nutricionales.

**2. Modelo de Machine Learning con PyTorch**

- Definición del Modelo: Se define una red neuronal simple utilizando PyTorch. El modelo consta de una capa de entrada, una capa oculta y una capa de salida.
  
- Entrenamiento: El modelo se entrena con los datos preprocesados para aprender a generar recomendaciones nutricionales basadas en las características del usuario.
  
- Optimización de Hiperparámetros con Optuna: Optuna se utiliza para encontrar los mejores hiperparámetros del modelo (por ejemplo, tamaño de la capa oculta, tasa de aprendizaje, número de épocas) mediante una serie de pruebas y optimización bayesiana.

**3. Integración con la API de OpenAI y Uso de LLM**

- Generación de Planes Nutricionales: Se utiliza un modelo de lenguaje grande (LLM) proporcionado por OpenAI para enriquecer las recomendaciones generadas por el modelo de machine learning. A través de prompts específicos, el LLM genera un plan nutricional detallado que incluye porciones de alimentos y consideraciones dietéticas, en general.
  
- Generación de Texto Natural: OpenAI puede generar planes nutricionales detallados y personalizados en lenguaje natural, mejorando la comprensión y la utilidad de las recomendaciones para el usuario final.
  
- Personalización: La información ingresada por el usuario (peso, altura, horas de sueño, nivel de actividad, estación del año, preferencias dietéticas, comorbilidades, y tipo de diabetes) se utiliza para personalizar las recomendaciones generadas por el LLM. La API puede manejar aspectos contextuales y preferencias específicas del usuario que no están completamente cubiertas por los datos estructurados.
  
**4. Interfaz de Usuario con Streamlit**

- Recopilación de Datos del Usuario: Se utiliza Streamlit para crear una interfaz de usuario interactiva donde los usuarios pueden ingresar sus datos personales y preferencias.
  
- Visualización de Resultados: Los planes nutricionales generados se muestran directamente en la aplicación y se proporciona la opción de guardarlos como PDF o imprimirlos.
  
- Visualización y Usabilidad: Imágenes de fondo y logos personalizados se integran en la aplicación para mejorar la experiencia del usuario.

**5. Manejo de Características Categóricas**

- Codificación de Características: Las características categóricas como nivel de actividad, estación del año, y tipo de diabetes se codifican numéricamente para ser utilizadas por el modelo de machine learning.

**6. Funcionalidades Adicionales**

- Traducción de Condiciones Médicas: Las comorbilidades ingresadas en español se traducen al inglés para ser procesadas correctamente por la API de OpenAI.
- Formateo de Recomendaciones: Las recomendaciones generadas se formatean para presentarlas de manera clara y legible al usuario.

📉 **Flujo del Sistema**

- Carga de Datos: Los datasets se cargan y preprocesan.
- Entrenamiento del Modelo: El modelo se entrena utilizando los datos preprocesados.
- Optimización: Se optimizan los hiperparámetros del modelo con Optuna.
- Ingreso de Datos del Usuario: El usuario ingresa sus datos a través de la interfaz de Streamlit.
- Generación de Recomendaciones: El modelo de machine learning genera una recomendación inicial que se enriquece mediante el LLM de la API de OpenAI.
- Visualización: El plan nutricional personalizado se muestra al usuario y se ofrecen opciones para guardar o imprimir.

🦾 **Propuesta de Valor**

- Complementariedad de Fuentes: El uso combinado de datasets estructurados y la API de OpenAI permite aprovechar lo mejor de ambos mundos, por un lado la precisión de los modelos entrenados en datos específicos y la flexibilidad y comprensión contextual de los modelos de lenguaje grande.

- Streamlit facilita la creación de interfaces interactivas y amigables para el usuario, lo que mejora la experiencia del usuario final y facilita la adopción del sistema.

🤖 **Stack Tech**

- Lenguaje de Programación: ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4479A1?logo=sql&logoColor=white)
- Base de Datos: ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)
- IDE: ![Amazon SageMaker](https://img.shields.io/badge/Amazon_SageMaker-232F3E?logo=amazon&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white)
- Visualización de datos: ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=power-bi&logoColor=white)
- Creación de aplicación web interactiva: ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
- Gestión del Código Fuente y Desarrollo Colaborativo: ![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)
- MVP y Gestión de Equipo: ![Trello](https://img.shields.io/badge/Trello-0079BF?logo=trello&logoColor=white)

🧩 **Colaboradores**

- Alejandro Asor Corrales Gómez - Data Engineer **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aacg/) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/AlejandroAsor/)

- Tomás Del Barco - Data Engineer **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tomás-del-barco-b74337229/) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/tDelbarco/)

- Ramiro Hernán Cabri - Data Analyst **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ramiro-hernan-cabri-93063523b/) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/RamiroCabri1/)

- Daniela Andrea Puebla Mosca - Data Analyst **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniela-pueblam31) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/Danny3431/)

- Guillermo Gallo García - Data Analyst **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guillermo-patricio-gallo-garcia-0a3bb3bb/) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/Galo0000/)

- Jorge Henríquez Novoa - Data Scientist **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorge-henriquez-novoa) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/jorgea-hn/)

- Andrés Felipe Corzo Angarita - Data Scientist **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/andres-felipe-corzo-angarita/) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/AndresFCA/)

- Delicia Fedele Boria - Machine Learning **>>** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deliciafedeleboria/) [![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/defedeleboria/)

🔗 **Enlaces Relevantes**

- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](diabeathealthcare.streamlit.app)
- [![Trello](https://img.shields.io/badge/Trello-0079BF?logo=trello&logoColor=white)](https://trello.com/b/nGylF9YE/s16-19-databi)
- completar...
