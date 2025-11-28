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

## 🔍 Carga y Exploración: `1_exploration.ipynb`

En esta primera etapa se realizó:

- Carga del dataset original y revisión de su estructura.  
- Nombres de columnas en formato `snake_case` ya presente.  
- Comprobación de duplicados: el resultado fue **0 filas duplicadas**, por lo que no fue necesario eliminar registros repetidos.  
- Detección de valores *nulos* en tres columnas categóricas:  
  - `teacher_quality` (78 nulos)  
  - `parental_education_level` (90 nulos)  
  - `distance_from_home` (67 nulos)  

  ➡️ Se decidió **no imputar nulos**, manteniendo los datos originales y dejando que las visualizaciones trabajen únicamente con registros completos.  
  
  ➡️ La validación detallada de **rangos y coherencia** se documenta en el notebook **2_transformation.ipynb** como parte de la limpieza estructural.  

Estas observaciones confirmaron que el dataset requería una limpieza estructurada, abordada en el notebook `2_transformation.ipynb`.

## 🧹 Limpieza aplicada: `2_transformation.ipynb`

La limpieza se realizó mediante funciones modulares definidas en `cleaning.py`, aplicadas en orden lógico:

- Se convirtieron los nombres de las columnas a **minúsculas** para facilitar el acceso y mantener coherencia.  
- No se aplicaron otras transformaciones, ya que los nombres ya estaban correctamente formateados.  
- Se identificaron valores nulos en tres columnas categóricas (`teacher_quality`, `distance_from_home`, `parental_education_level`).  
  ➡️ No se realizó imputación, siguiendo la decisión de mantener los datos originales y permitir que las visualizaciones gestionen automáticamente los registros incompletos.  
- Se añadieron **comprobaciones de coherencia y rangos** en todas las **variables numéricas**:  
  - `attendance` (0–100)  
  - `sleep_hours` (0–24)  
  - `hours_studied`, `tutoring_sessions`, `physical_activity` (no negativos)  
  - `exam_score` y `previous_scores` (0–100)  
- En estas comprobaciones se detectó un único valor fuera de rango en `exam_score` (101).  
  ➡️ Se corrigió manualmente a 100, documentando la decisión de forma explícita.  
- Se revisaron también los valores únicos de las columnas categóricas para confirmar su coherencia.