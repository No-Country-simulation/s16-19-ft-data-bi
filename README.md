**This repository is part of No Country's Simulation Tech Program in Data-BI.**

💎 **Nombre del Producto**

![logo](https://github.com/No-Country-simulation/s16-19-ft-data-bi/blob/bf4bb2563273080a8798ecab892a77b0c960606b/DH.png)

📊 **Rubro**

Orientado a Healthtech. Sistema de Recomendación Nutricional para Pacientes Diabéticos.

🍏 **Visualizaciones y Análisis**

Este proyecto inicia teniendo primero múltiples Bases de Datos en PostgreSQL, y de allí se revisa una por una teniendo como objetivo realizar un análisis exploratorio de datos (EDA) para extraer datasets claves con información sobre pacientes diabéticos (incluyendo parámetros, marcadores e indicadores) y otro con datos detallados sobre alimentos y sus propiedades nutricionales. A través de este análisis, buscamos comprender la relación entre las características de los pacientes y sus necesidades nutricionales, así como identificar patrones y tendencias en los datos que puedan ser útiles para el desarrollo de un sistema de recomendación nutricional personalizado.

Utilizando Python, Pandas y diversas bibliotecas de visualización de datos, exploraremos la distribución de las variables, identificaremos valores atípicos y datos faltantes, y analizaremos las correlaciones entre diferentes características. Además, realizaremos un análisis descriptivo de los datos para obtener una visión general de las características de los pacientes y los alimentos incluidos en el estudio.

Este análisis exploratorio proporcionará las bases necesarias para el desarrollo de un modelo de machine learning que pueda generar búsquedas y recomendaciones de planes nutricionales personalizadas para pacientes diabéticos, considerando sus características individuales y necesidades específicas. El objetivo final es mejorar la calidad de vida de los pacientes con diabetes mediante una orientación nutricional óptima y personalizada.

1. **Foco Principal**
   
   - El objetivo principal de este análisis es explorar y comprender la información contenida en la base de datos "international_diabetes_federation" para identificar patrones, relaciones y tendencias relevantes para el desarrollo de un sistema de recomendación nutricional personalizado para pacientes diabéticos. Queremos descubrir cómo las características de los alimentos (contenido nutricional, índice glucémico, etc.) se relacionan con las necesidades y condiciones de salud de los pacientes, para así generar recomendaciones dietéticas precisas y efectivas.

2. **Fases del Análisis**
   
- Fase 1: Comprensión de los Datos

  - Recopilación y carga de datos: Detallamos cómo se accedió a los datos, ya sea desde PostgresSQL, archivos CSV, entre otros.
  - Inspección inicial: Describimos las primeras observaciones sobre los datos, incluyendo sus dimensiones y tipos de variables.
  - Limpieza y preprocesamiento: Enumeramos las tareas realizadas para preparar los datos, como el manejo de valores nulos, duplicados y outliers.

- Fase 2: Análisis Exploratorio de Datos (EDA)

   - Análisis univariado: Describimos la distribución de las variables clave mediante histogramas, gráficos de barras y medidas de resumen.
   - Análisis bivariado: Exploramos las relaciones entre variables utilizando gráficos de dispersión, tablas de contingencia y pruebas de correlación.
   - Identificación de patrones y tendencias: Destacamos hallazgos interesantes o relevantes para el proyecto.

- Fase 3: Preparación de Datos para Modelado

  - Selección de características: Explicamos qué variables se utilizarán para entrenar el modelo y justificamos nuestra elección.
  - Ingeniería de características: Detallamos las transformaciones realizadas y la creación de nuevas variables.
  - División de datos: Describimos cómo se dividieron los datos en conjuntos de entrenamiento y prueba.

- Fase 4: Modelado y Evaluación

  - Selección del modelo: Mencionamos el tipo de modelo planeado (regresión, clasificación, etc.) y justificamos la elección.
  - Entrenamiento del modelo: Describimos el proceso de entrenamiento del modelo y las métricas utilizadas para evaluar su rendimiento.
  - Optimización del modelo: Explicamos cómo se realizará la optimización de los hiperparámetros, si es aplicable.
  - Evaluación final: Presentamos los resultados del modelo en el conjunto de prueba y discutimos su desempeño.

- Fase 5: Conclusiones y Recomendaciones

  - Resumen de hallazgos clave: Destacamos los resultados más importantes del análisis.
  - Implicaciones para el sistema de recomendación: Explicamos cómo los hallazgos informarán el desarrollo del sistema de recomendación.
  - Próximos pasos: Sugerimos posibles direcciones futuras para el análisis o el desarrollo del sistema.

3. **Visualizaciones**

   Completar...

🍏 **Implementación de Búsqueda y Recomendación**

El Sistema de Recomendación Nutricional desarrollado utiliza una combinación de una base de datos que hicimos en PostgresSQL, donde mediante un proceso de ETL, se extrajo lo más útil y significativo, haciendo una estructuración de los mismos. Luego, se integra la API de Gemini como un modelo de lenguaje grande (LLM) para enriquecer las búsquedas de productos comerciales y planes nutricionales personalizados a la vez que se el usuario completa con datos requeridos por la plataforma, por medio de la técnica de procesamiento de lenguaje natural (NLP). En resumen, se plantea una integración híbrida. Los componentes y el flujo del sistema son:

1. **Base de Datos**

- Bases de Datos Iniciales: En PostgresSQL, se recopila y almacenan los datos iniciales relacionados a parámetros, marcadores e indicadores de pacientes diabéticos, así como también de alimentos, proteínas, entre otros.

- Preprocesamiento: Los datos se cargan y se preprocesan para eliminar valores nulos y normalizar las características, asegurando así que el modelo de machine learning recibe datos de calidad.

2. **Modelo de Machine Learning con PyTorch**

- Definición del Modelo: Se define una red neuronal simple utilizando PyTorch. El modelo consta de una capa de entrada, una capa oculta y una capa de salida.

- Entrenamiento: El modelo se entrena con los datos preprocesados para aprender a generar recomendaciones nutricionales basadas en las características del usuario.

- Optimización de Hiperparámetros con Adam: Es un algoritmo de optimización muy popular utilizado para entrenar modelos de Deep Learning, que ajusta la tasa de aprendizaje para cada parámetro según los momentos de primer y segundo orden del gradiente, permitiendo adaptarse a las características de los datos. Utiliza el concepto de momento para considerar tanto el gradiente actual como los anteriores, suavizando las actualizaciones y acelerando la convergencia. Además, incluye una corrección de desviación que mejora la estabilidad y rendimiento en las primeras iteraciones.

3. **Integración con la API de Gemini y Uso de LLM**

- Búsqueda de Productos Comerciales y Generación de Planes Nutricionales: Se utiliza un modelo de lenguaje grande (LLM) proporcionado por Gemini para enriquecer lo solicitado por el usuario al modelo de machine learning. A través de prompts específicos, el LLM genera una búsqueda o un plan nutricional detallado que incluye datos relevantes de consumición y contenido, porciones de alimentos y consideraciones dietéticas, en general.

- Generación de Texto Natural: Gemini puede generar búsquedas y planes nutricionales detallados y personalizados en lenguaje natural, mejorando la comprensión y la utilidad de las recomendaciones para el usuario final.

- Personalización: La información ingresada por el usuario (edad, género, peso, altura, país, estación del año, horas de sueño promedio, hora en que se despierta y se duerme usualmente, nivel de actividad física, tipo de diabetes, preferencias y restricciones dietéticas así como patologías subyacentes) se utiliza para personalizar las recomendaciones generadas por el LLM. La API puede manejar aspectos contextuales y preferencias específicas del usuario que no están completamente cubiertas por los datos estructurados.

4. **Interfaz de Usuario con Streamlit**

- Recopilación de Datos del Usuario: Se utiliza Streamlit para crear una interfaz de usuario interactiva donde los usuarios pueden ingresar sus datos de búsquedas, personales y preferencias.

- Visualización de Resultados: Aquello que se genera se muestra directamente en la aplicación y se proporciona la opción de guardarlos como PDF o imprimirlos por defecto.

- Visualización y Usabilidad: Imágenes de fondo y logos personalizados se integran en la aplicación para mejorar la experiencia del usuario.

5. **Manejo de Características Categóricas**

- Codificación de Características: Las características categóricas como nivel de actividad, estación del año, comorbilidad y tipo de diabetes se codifican numéricamente para ser utilizadas por el modelo de machine learning.

📉 **Flujo del Sistema**

- Carga de Datos: La base de datos se preprocesa.
- Entrenamiento del Modelo: El modelo se entrena utilizando los datos preprocesados.
- Optimización: Se optimizan los hiperparámetros del modelo con Adam.
- Ingreso de Datos del Usuario: El usuario ingresa sus datos a través de la interfaz de Streamlit.
- Generación de Recomendaciones: El modelo de machine learning genera una recomendación inicial que se enriquece mediante el LLM de la API de Gemini.
- Visualización: Las búsquedas y los planes se muestran al usuario y se ofrecen opciones para guardar o imprimir.

🦾 **Propuesta de Valor**

- Complementariedad de Fuentes: El uso combinado de una base de datos internacional y la API de Gemini permite aprovechar lo mejor de ambos mundos, por un lado la precisión de los modelos entrenados en datos específicos y la flexibilidad y comprensión contextual de los modelos de lenguaje grande.

- Streamlit facilita la creación de interfaces interactivas y amigables para el usuario, lo que mejora la experiencia del usuario final y facilita la adopción del sistema.

🤖 **Stack Tech**

- Lenguaje de Programación: ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4479A1?logo=sql&logoColor=white)
- Base de Datos: ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white)
- Nube: ![Rackspace](https://img.shields.io/badge/Rackspace-000000?logo=rackspace&logoColor=white)
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

- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://diabeat-healthcare.streamlit.app)
- [![Trello](https://img.shields.io/badge/Trello-0079BF?logo=trello&logoColor=white)](https://trello.com/b/nGylF9YE/s16-19-databi)
- completar...
