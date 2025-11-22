# Proyecto 1 - EDA

Este repositorio contiene el proyecto de **Exploración, Limpieza y Visualización Básica de un Dataset**.

## Estructura
- `data/`: contiene el dataset en formato CSV.
- `notebooks/`: incluye el notebook `eda.ipynb` con el análisis.
- `README.md`: explicación general del proyecto.
- `requirements.txt`: dependencias.

## Objetivo
Realizar un flujo completo de análisis exploratorio inicial (EDA) sobre un dataset real:
1. Carga del dataset.
2. Exploración inicial.
3. Limpieza y normalización.
4. Visualizaciones básicas.
5. Conclusiones exploratorias.

## Dataset utilizado
- Nombre: Student Performance Factors
- Fuente: [Kaggle](https://www.kaggle.com/datasets/ayeshaseherr/student-performance)
- Descripción: Dataset que recoge factores sociales, académicos y personales que pueden influir en el rendimiento estudiantil.

## Limpieza aplicada

- Se convirtieron los nombres de las columnas a minúsculas para facilitar el acceso y mantener coherencia.
- No se aplicaron otras transformaciones, ya que los nombres ya estaban correctamente formateados.
- Se sustituyeron valores nulos en tres columnas categóricas (`teacher_quality`, `distance_from_home`, `parental_education_level`) utilizando el modo (máxima frecuencia).
- Se convirtieron 13 columnas object al tipo `category` para optimizar el uso de memoria, facilitar visualizaciones y agrupaciones.
- Se verificó que no existieran duplicados.
- Se revisaron los rangos de las variables numéricas (`attendance`, `sleep_hours`, `hours_studied`, `tutoring_sessions`, `physical_activity`) y no se detectaron valores fuera de rango ni negativos.
- Se comprobó que las variables categóricas contienen únicamente las categorías esperadas.

La limpieza se realizó paso a paso en el notebook, sin encapsular en funciones, para facilitar la documentación  
y el seguimiento del razonamiento aplicado en cada etapa.

