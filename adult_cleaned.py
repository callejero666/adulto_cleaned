import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Cargar el dataset desde el archivo Excel
df = pd.read_excel(r"D:\adulto_cleaned\adult_cleaned.xlsx")

st.write("""

## **Información general del conjunto de datos: Ingreso anual basado en el Censo de 1994**
Este conjunto de datos, extraído por Barry Becker del Censo de 1994, se utiliza para clasificar si una persona tiene un ingreso anual mayor o menor a $50,000. Incluye información demográfica, educativa y laboral de individuos mayores de 16 años, que trabajaron al menos una hora por semana y cumplen con ciertas condiciones de ingreso y relevancia estadística.

Atributos principales: Edad, clase laboral, educación, ocupación, relación, raza, sexo, horas trabajadas, ganancia/pérdida de capital y país de origen.""")

# Verificar las primeras filas del dataset
st.write(df.head())  # Usamos Streamlit para mostrar las primeras filas

st.write("""
### Contenido

### Para obtener más información, consulte la fuente original en UCI Machine Learning Repository.

### Variables de entrada (atributos):

* Edad ( age): Numérica continua.
* Clase laboral ( workclass): Tipo de empleo (privado, autónomo, gobierno, etc.).
* Peso final del censo ( fnlwgt): Peso estadístico en la población.
* Educación ( education): Nivel educativo alcanzado (licenciatura, maestría, etc.).
* Años de educación ( education-num): Años de estudio completos.
* Estado civil ( marital-status): Estado civil (casado, separado, viudo, etc.).
* Ocupación ( occupation): Profesión principal (ventas, transporte, gerencia, etc.).
* Relación ( relationship): Relación familiar (esposo, hijo propio, no familiar, etc.).
* Raza ( race): Categorías como blanco, negro, asiático, entre otros.
* Sexo ( sex): Masculino o Femenino.
* Ganancia de capital ( capital-gain): Valor continuo.
* Pérdida de capital ( capital-loss): Valor continuo.
* Horas por semana ( hours-per-week): Número de horas trabajadas por semana.
* País de origen ( native-country): País de nacimiento (Estados Unidos, India, México, etc.).
""")

# Interpretación de los resultados
st.write("""
## Interpretación de los Resultados

1. **Distribución de Ingresos por Nivel Educativo**:
   El gráfico de barras muestra cómo se distribuyen los ingresos según el nivel educativo. A partir de este análisis, podemos observar si hay una relación entre un nivel educativo más alto y mayores ingresos.

2. **Relación entre Edad y Horas Trabajadas**:
   El gráfico de dispersión revela la relación entre la edad de los individuos y las horas trabajadas por semana. Esta información puede ayudar a comprender los patrones de trabajo a lo largo de la vida laboral.

3. **Distribución por Workclass**:
   El gráfico circular muestra cómo se distribuyen los diferentes tipos de empleo (Workclass) entre los individuos con ingresos mayores o menores a 50K. Esto puede indicar qué sectores laborales tienen una mayor representación en ciertos niveles de ingresos.

4. **Distribución de Ingreso según Estado Civil**:
   El gráfico de barras revela si el estado civil de una persona influye en su nivel de ingresos. Esta relación puede ser útil para comprender los patrones socioeconómicos según el estado civil.

5. **Distribución de Edad según Estado Civil**:
   El gráfico de caja muestra cómo varía la edad según el estado civil y el nivel de ingresos. Esto proporciona información sobre las diferencias de edad entre personas casadas y no casadas en diferentes rangos de ingresos.

6. **Distribución de Educación por Estado Civil**:
   El gráfico de barras muestra cómo se distribuyen los niveles educativos según el estado civil. Esto puede ayudar a identificar si ciertos estados civiles tienen una mayor representación de personas con niveles educativos específicos.

7. **Distribución de Educación (Número de Años) según Ingreso**:
   El gráfico de barras revela cómo el número de años de educación influye en el nivel de ingresos de los individuos. Esto es crucial para comprender cómo la educación impacta el potencial de ingresos.

8. **Distribución de Raza según Ingreso**:
   El gráfico de barras muestra cómo se distribuyen las razas según los niveles de ingreso. Este análisis puede ser útil para entender las disparidades raciales en términos de ingresos.

9. **Distribución de Horas Trabajadas según Estado Civil**:
   El gráfico de caja muestra la relación entre las horas trabajadas por semana y el estado civil de los individuos. Nos ayuda a analizar si las personas casadas o no casadas tienen diferencias en las horas trabajadas.

10. **Distribución por País de Origen según Ingreso**:
    Este gráfico de barras muestra cómo se distribuyen los individuos por país de origen según su nivel de ingresos. Puede arrojar información sobre las diferencias en los ingresos dependiendo del país de origen de las personas.
""")

# Título del dashboard
st.title("Dashboard Interactivo - Análisis de Ingresos >50K")


# Filtros interactivos
st.sidebar.header("Filtros")
selected_workclass = st.sidebar.multiselect(
    "Selecciona Workclass:",
    options=df["workclass"].unique(),
    default=df["workclass"].unique()
)

selected_education = st.sidebar.multiselect(
    "Selecciona Educación:",
    options=df["education"].unique(),
    default=df["education"].unique()
)

selected_sex = st.sidebar.radio(
    "Selecciona Sexo:",
    options=df["sex"].unique()
)

# Filtrar los datos según los filtros seleccionados
df_filtered = df[
    (df["workclass"].isin(selected_workclass)) &
    (df["education"].isin(selected_education)) &
    (df["sex"] == selected_sex)
]

# Mostrar datos filtrados
st.write("### Datos Filtrados")
st.dataframe(df_filtered)

# Visualización de la distribución de ingresos (income)
plt.figure(figsize=(8,6))
sns.countplot(data=df, x='income')
plt.title('Distribución de Ingresos')
st.pyplot(plt)

st.write("""
Análisis del conjunto de datos
El conjunto de datos analiza características demográficas y laborales para predecir el ingreso anual de las personas.

Dimensiones del conjunto de datos después de la limpieza: Filas: 32.561. Columnas: 15. Frecuencia de la columna income: La variable objetivo ( income) clasifica los ingresos en dos categorías:

<=50K: Representa la mayoría de los casos, con 24.720 registros .
50K: Representa 7.841 registros .

Esto refleja una distribución desbalanceada , donde la mayoría de los ingresos se encuentran en la categoría de $50,000 o menos al año, lo cual podría requerir técnicas específicas para abordar el desbalance en tareas de modelado predictivo.""")

# 1. Gráfico de barras - Distribución por Nivel Educativo
st.write("### Distribución por Nivel Educativo")
fig_edu = px.histogram(
    df_filtered,
    x="education",
    color="income",
    barmode="group",
    title="Distribución de Ingresos por Nivel Educativo"
)
st.plotly_chart(fig_edu)

# 2. Gráfico de dispersión - Edad vs. Horas Trabajadas
st.write("### Relación entre Edad y Horas Trabajadas por Semana")
fig_age_hours = px.scatter(
    df_filtered,
    x="age",
    y="hours-per-week",
    color="income",
    title="Edad vs Horas Trabajadas por Semana",
    labels={"hours-per-week": "Horas por Semana", "age": "Edad"}
)
st.plotly_chart(fig_age_hours)

# 3. Gráfico circular - Distribución por Workclass
st.write("### Distribución por Workclass")
fig_workclass = px.pie(
    df_filtered,
    names="workclass",
    title="Distribución de Workclass",
    hole=0.4
)
st.plotly_chart(fig_workclass)

# 4. Tabla dinámica con estadísticas básicas
st.write("### Estadísticas Básicas por Ingreso")
stats = df_filtered.groupby("income").agg(
    {
        "age": ["mean", "median", "min", "max"],
        "hours-per-week": ["mean", "median", "min", "max"],
    }
)
st.write(stats)

# Crear una nueva columna 'is_married' que indique si la persona está casada
df['is_married'] = df[['marital-status_ Married-AF-spouse', 
                       'marital-status_ Married-civ-spouse', 
                       'marital-status_ Married-spouse-absent']].apply(
    lambda row: 'Married' if row.any() == 1 else 'Not Married', axis=1)

# Análisis y visualización

# Visualización de la relación entre la 'is_married' y la 'income'
st.write("### Distribución de Ingreso según Estado Civil")
fig_married_income = plt.figure(figsize=(8,6))
sns.countplot(data=df, x='is_married', hue='income')
plt.title('Distribución de Ingreso según Estado Civil')
st.pyplot(fig_married_income)

# Visualización de la distribución de edad según estado civil
st.write("### Distribución de Edad según Estado Civil")
fig_age_married = plt.figure(figsize=(8,6))
sns.boxplot(data=df, x='is_married', y='age', hue='income', showfliers=False)
plt.title('Distribución de Edad según Estado Civil')
st.pyplot(fig_age_married)

# Gráfico de barras de distribución por educación
st.write("### Distribución de Educación por Estado Civil")
fig_education_married = plt.figure(figsize=(10,6))
sns.countplot(data=df, y='education', hue='is_married')
plt.title('Distribución de Educación por Estado Civil')
st.pyplot(fig_education_married)

# Gráfico de barras sobre la relación de 'education-num' con 'income'
st.write("### Distribución de Educación (Número de años) según Ingreso")
fig_education_num_income = plt.figure(figsize=(10,6))
sns.countplot(data=df, x='education-num', hue='income')
plt.title('Distribución de Educación (Número de años) según Ingreso')
st.pyplot(fig_education_num_income)

# Gráfico sobre la relación de 'race' y 'income'
st.write("### Distribución de Raza según Ingreso")
fig_race_income = plt.figure(figsize=(8,6))
sns.countplot(data=df, x='race', hue='income')
plt.title('Distribución de Raza según Ingreso')
st.pyplot(fig_race_income)

# Visualización sobre la relación entre horas trabajadas y estado civil
st.write("### Distribución de Horas Trabajadas según Estado Civil")
fig_hours_married = plt.figure(figsize=(8,6))
sns.boxplot(data=df, x='is_married', y='hours-per-week', hue='income')
plt.title('Distribución de Horas Trabajadas según Estado Civil')
st.pyplot(fig_hours_married)

# Gráfico sobre la relación entre 'native-country' y 'income'
st.write("### Distribución por País de Origen según Ingreso")
fig_native_country_income = plt.figure(figsize=(12,6))
sns.countplot(data=df, y='native-country', hue='income')
plt.title('Distribución por País de Origen según Ingreso')
st.pyplot(fig_native_country_income)


