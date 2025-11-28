import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# Histograma: asistencia entre los estudiantes
def histogram_attendance(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["attendance"], bins=20, kde=True, color="salmon")
    plt.title("Distribución de asistencia (attendance)")
    plt.xlabel("Número de asistencias")
    plt.ylabel("Cantidad de estudiantes")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Histograma: horas de sueño entre el alumnado
def histogram_sleep_hours(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['sleep_hours'], bins=15, kde=True,
                 color='skyblue', edgecolor='black')
    plt.title('Distribución de horas de sueño')
    plt.xlabel('Horas de sueño')
    plt.ylabel('Cantidad de estudiantes')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()


# Boxplots: rendimiento académico vs esfuerzo individual
def boxplots_exam_studied(df):
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(["exam_score", "hours_studied"], 1):
        plt.subplot(1, 2, i)
        sns.boxplot(x=df[col], color="lightgreen")
        plt.title(f"Boxplot de {col}")
        plt.xlabel(col.replace("_", " ").capitalize())
    plt.tight_layout()
    plt.show()


# G. de Barras: nivel educativo de los padres y el tipo de escuela
def bar_parents_school(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(x="parental_education_level",
                  hue="school_type", data=df, palette="Set2")
    plt.title("Nivel educativo de los padres según tipo de escuela")
    plt.xlabel("Nivel educativo de los padres")
    plt.ylabel("Cantidad de estudiantes")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend(title="Tipo de escuela")
    plt.show()


# Boxplots: nivel educativo de los padres y el rendimiento académico de los hijos.
def boxplots_exam_parents(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="parental_education_level",
                y="exam_score", data=df, palette="Set3")
    plt.title("Rendimiento académico según nivel educativo de los padres")
    plt.xlabel("Nivel educativo de los padres")
    plt.ylabel("Nota en el examen")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()


# Boxplots: rendimiento académico de los estudiantes según el tipo de escuela
def boxplots_exam_school(df):
    plt.figure(figsize=(6, 4))
    sns.boxplot(x="school_type", y="exam_score", data=df, palette="Set2")
    plt.title("Notas según tipo de escuela")
    plt.xlabel("Tipo de escuela")
    plt.ylabel("Nota en el examen")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.show()


# G. Barras: Distancia desde casa a la escuela vs Motivacion del alumno.
def bar_motivation_distance(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(x="motivation_level", hue="distance_from_home",
                  data=df, palette="Set1")
    plt.title("Motivación del alumnado según distancia desde casa")
    plt.xlabel("Nivel de motivación")
    plt.ylabel("Cantidad de estudiantes")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend(title="Distancia desde casa")
    plt.show()
