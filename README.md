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

## 📈 Visualizaciones realizadas: `3_eda.ipynb`

El proyecto incluye las siguientes visualizaciones para explorar el comportamiento de las variables clave:

➡️ En las variables categóricas con valores nulos (`parental_education_level`, `distance_from_home`), las visualizaciones se han generado excluyendo automáticamente los registros incompletos. 
Esto confirma que la decisión de no imputar nulos no compromete la calidad del análisis.

- **Histograma:** `attendance`  
  - Propósito: visualizar la distribución de asistencia entre estudiantes y detectar concentraciones en los valores altos.
  - Lectura: La mayoría de estudiantes presentan niveles de asistencia elevados, con un pico claro en el valor máximo (100 asistencias). Esto sugiere un patrón de compromiso generalizado, aunque también se observan algunos casos con asistencia más baja que podrían requerir atención.

- **Histograma:** `sleep_hours`  
  - Propósito: mostrar la forma de la distribución de horas de sueño, identificar patrones de descanso y posibles casos de sueño insuficiente o excesivo.
  - Lectura: La distribución es aproximadamente normal, con un pico en las 7 horas de sueño. Esto indica que la mayoría de estudiantes mantienen hábitos de descanso saludables, aunque también hay casos de sueño insuficiente (<6h) o excesivo (>9h) que podrían influir en el rendimiento académico.

- **Boxplots:** `exam_score` y `hours_studied`  
  - Propósito: detectar valores atípicos, comparar rangos y medianas.
  - Lectura:
    - `exam_score`: distribución centrada, con varios valores atípicos en el extremo inferior, lo que sugiere que algunos estudiantes tienen dificultades significativas.

    - `hours_studied`: zona media estrecha, con algunos estudiantes que estudian mucho más o mucho menos que la mayoría, lo que refleja diferencias marcadas en el esfuerzo individual.

- **Gráfico de barras agrupadas de `parental_education_level` por `school_type`**  
  - Propósito: comparar el nivel educativo de los padres según el tipo de escuela (pública o privada).  
  - Lectura: en ambos tipos de escuela predominan padres con estudios secundarios, aunque las escuelas privadas tienen una proporción ligeramente mayor de padres con estudios universitarios o de posgrado. El gráfico aporta contexto sobre el perfil educativo de las familias.

- **Boxplot de `exam_score` por `parental_education_level`**  
  - Propósito: comparar el rendimiento académico según el nivel educativo de los padres.  
  - Lectura: los estudiantes cuyos padres tienen estudios universitarios o de posgrado tienden a obtener notas más altas, mientras que los de padres con estudios secundarios muestran mayor variabilidad. El gráfico sugiere que el entorno educativo familiar puede influir en el desempeño.

- **Boxplot de `exam_score` por `school_type`**  
  - Propósito: comparar el rendimiento académico entre estudiantes de escuelas públicas y privadas.  
  - Lectura: las medianas son similares en ambos grupos, aunque las escuelas privadas muestran una dispersión ligeramente menor. El gráfico sugiere que el rendimiento es comparable entre tipos de escuela.

- **Gráfico de barras agrupadas de `motivation_level` por `distance_from_home`**  
  - Propósito: explorar si la distancia entre el hogar y la escuela influye en la motivación del alumnado.  
  - Lectura: la motivación media es la más común en todos los grupos, especialmente entre quienes viven cerca. El gráfico sugiere que la cercanía podría tener un efecto positivo sobre la motivación.