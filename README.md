# Proyecto 1 - EDA

Este repositorio contiene el proyecto de **Exploración, Limpieza y Visualización Básica de un Dataset**.

## 📁 Estructura
- `data/`: contiene el dataset original en formato CSV y el limpio
  - student_performance.csv
  - student_clean.csv

- `notebooks/`: incluye los notebooks:
  - 1_exploration.ipynb
  - 2_transformation.ipynb
  - 3_eda.ipynb

- `src/`: contiene los 2 los dos .py que usaremos en la limpieza y visualización
  - cleaning.py
  - visualization.py

- `README.md`: explicación general del proyecto.
- `requirements.txt`: dependencias.

## 🎯 Objetivo
Realizar un flujo completo de análisis exploratorio inicial (EDA) sobre un dataset real, dividido en tres etapas:
1. Exploración inicial del dataset para detectar incoherencias, nulos y patrones generales.
2. Limpieza estructurada mediante funciones modulares encapsuladas en cleaning.py.
3. Visualizaciones básicas para interpretar el comportamiento de las variables clave.
4. Conclusiones exploratorias, documentadas al final de cada notebook.

## Dataset utilizado
- Nombre: Student Performance Factors
- Fuente: [Kaggle](https://www.kaggle.com/datasets/ayeshaseherr/student-performance)
- Descripción: Dataset que recoge factores sociales, académicos y personales que pueden influir en el rendimiento estudiantil.