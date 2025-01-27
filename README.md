# Dashboard Interactivo - Análisis de Ingresos >50K

Este proyecto utiliza Python y Streamlit para crear un dashboard interactivo que analiza un dataset de adultos según sus ingresos.

# **Información general del conjunto de datos: Ingreso anual basado en el Censo de 1994**
Este conjunto de datos, extraído por Barry Becker del Censo de 1994, se utiliza para clasificar si una persona tiene un ingreso anual mayor o menor a $50,000. Incluye información demográfica, educativa y laboral de individuos mayores de 16 años, que trabajaron al menos una hora por semana y cumplen con ciertas condiciones de ingreso y relevancia estadística.

Atributos principales: Edad, clase laboral, educación, ocupación, relación, raza, sexo, horas trabajadas, ganancia/pérdida de capital y país de origen.

## Estructura del Proyecto

- `adult_cleaned.xlsx`: Dataset limpio para análisis.
- `adul_cleaned.py`: Código Python para ejecutar el dashboard.

## Requisitos

Instalar las siguientes dependencias:
```bash
pip install streamlit pandas matplotlib seaborn


` Contenido

 Para obtener más información, consulte la fuente original en UCI Machine Learning Repository.

 Variables de entrada (atributos):

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
* País de origen ( native-country): País de nacimiento (Estados Unidos, India, México, etc.).`