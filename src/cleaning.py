import pandas as pd


def clean_dataset(df):
    # Normalización de nombres de columnas
    df.columns = df.columns.str.lower()
    return df


def coherence_ranges(df):
    # Revisar rangos en columnas numéricas
    print("% Asistencia fuera de rango:",
          df[~df["attendance"].between(0, 100)].shape[0])
    print("Horas de sueño fuera de rango:",
          df[~df["sleep_hours"].between(0, 24)].shape[0])
    print("Horas de estudio negativas:", df[df["hours_studied"] < 0].shape[0])
    print("Sesiones de tutoría negativas:",
          df[df["tutoring_sessions"] < 0].shape[0])
    print("Actividad física semanal negativas:",
          df[df["physical_activity"] < 0].shape[0])
    print("Notas de Examen fuera de rango:",
          df[~df["exam_score"].between(0, 100)].shape[0])
    print("Puntuaciones de examen anteriores fuera de rango:",
          df[~df["previous_scores"].between(0, 100)].shape[0])

    # Revisar los valores únicos de las categorías
    for col in df.select_dtypes(include=["object", "category"]).columns:
        print(f"{col}: {df[col].unique()}")
