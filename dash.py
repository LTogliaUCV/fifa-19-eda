import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from prettytable import PrettyTable

# Título principal del dashboard
st.title("Análisis del salario de los jugadores de FIFA 19")

# Define las opciones de la barra lateral
options = ['Estadísticas del salario', 'Percentiles del salario',
           'Porteros vs altura', 'Laterales y pase largo',
           'Mediocampistas y sus intercepciones', 'Delanteros y valoraciones',
           'Centrocampistas vs Vision']

# Agrega la barra lateral al dashboard
choice = st.sidebar.selectbox("Seleccione una opción", options)

# Muestra las estadísticas del salario semanal
if choice == 'Estadísticas del salario':
    # Carga el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("kl.csv", encoding='latin-1')
    # Elimina los caracteres no numéricos de la columna "Wage"
    df['Wage'] = df['Wage'].str.replace('K', '').str.replace('\x80', '')
    # Convierte la columna "Wage" a un tipo numérico
    df['Wage'] = pd.to_numeric(df['Wage'])

    # Calcula la media y desviación estándar del salario semanal
    mean_wage = df['Wage'].mean()
    std_wage = df['Wage'].std()

    # Calcula los percentiles del salario semanal
    percentiles_wage = df['Wage'].quantile([0.25, 0.5, 0.75])
    percentiles_wage = percentiles_wage.round(2)

    # Identifica los jugadores cuyo salario semanal está a más de 2 desviaciones estándar de la media
    outliers_wage = df[(df['Wage'] > mean_wage + 2 * std_wage) | (df['Wage'] < mean_wage - 2 * std_wage)]

    # Crea una tabla para mostrar las estadísticas del salario semanal
    table = PrettyTable()
    table.field_names = ["Estadísticas del salario semanal", ""]
    table.add_row(["Media", f"{mean_wage:.2f}"])
    table.add_row(["Desviación estándar", f"{std_wage:.2f}"])
    table.add_row(["Percentiles", f"{percentiles_wage}"])

    # Muestra la tabla
    st.write(table)

# Muestra los percentiles del salario semanal
elif choice == 'Percentiles del salario':
    # Carga el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("kl.csv", encoding='latin-1')
    # Elimina los caracteres no numéricos de la columna "Wage"
    df['Wage'] = df['Wage'].str.replace('K', '').str.replace('\x80', '')
    # Convierte la columna "Wage" a un tipo numérico
    df['Wage'] = pd.to_numeric(df['Wage'])

    # Calcula los percentiles del salario semanal
    percentiles_wage = df['Wage'].quantile([0.25, 0.5, 0.75])

    # Crea un gráfico de barras para mostrar los percentiles del salario semanal
    fig, ax = plt.subplots()
    ax.bar(percentiles_wage.index, percentiles_wage.values)
    ax.set_title("Percentiles del salario semanal")
    ax.set_xticks(percentiles_wage.index)
    ax.set_xticklabels([f'{p * 100}%' for p in percentiles_wage.index])
    ax.set_xlabel("Percentiles")
    ax.set_ylabel("Salario semanal")
    st.pyplot(fig)
    st.text("Este gráfico muestra los percentiles del salario semanal de los jugadores.")

# Muestra el top 10 de jugadores con mejores salarios
elif choice == 'Top 10 jugadores':
    # Carga el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("kl.csv", encoding='latin-1')
    # Elimina los caracteres no numéricos de la columna "Wage"
    df['Wage'] = df['Wage'].str.replace('K', '').str.replace('\x80', '')
    # Convierte la columna "Wage"a un tipo numérico
    df['Wage'] = pd.to_numeric(df['Wage'])

    # Ordena el DataFrame por salario semanal y toma los primeros 10 jugadores
    top_10 =  df.sort_values(by='Wage', ascending=False).head(10)

elif choice == 'Laterales y pase largo':
    # Carga el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("kl.csv", encoding='latin-1')

    # Filtrar los laterales
    full_backs = df[(df['Position'] == 'RB') | (df['Position'] == 'LB')]

    # Calcular estadísticas descriptivas de la velocidad de los laterales
    mean_long_passing_fb = full_backs['LongPassing'].mean()
    median_long_passing_fb = full_backs['LongPassing'].median()
    std_long_passing_fb = full_backs['LongPassing'].std()

    # Crear un histograma de la distribución de la altura de los laterales
    fig, ax = plt.subplots()
    sns.histplot(data=full_backs, x='Height')
    ax.set_title("Distribución de altura de los laterales")
    ax.set_xlabel("Altura")
    ax.set_ylabel("Número de jugadores")
    st.pyplot(fig)

    # Crear un gráfico de caja y bigotes para la longitud de pase largo de los laterales
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=full_backs, x='LongPassing')
    ax2.set_title("Longitud de pase largo de los laterales")
    ax2.set_xlabel("Longitud de pase largo")
    st.pyplot(fig2)

    # Muestra las estadísticas descriptivas de la longitud de pase largo de los laterales
    st.write(f"La media de la longitud de pase largo de los laterales es de {mean_long_passing_fb:.2f}.")
    st.write(f"La mediana de la longitud de pase largo de los laterales es de {median_long_passing_fb:.2f}.")
    st.write(f"La desviación estándar de la longitud de pase largo de los laterales es de {std_long_passing_fb:.2f}.")

    # Muestra una tabla con los 10 laterales con la longitud de pase largo más alta
    top_long_passing_fb = full_backs.sort_values(by='LongPassing', ascending=False).head(10)
    st.write("Los 10 laterales con la longitud de pase largo más alta son:")
    st.write(top_long_passing_fb[['Name', 'Club', 'Nationality', 'LongPassing']])

# Muestra la distribución de altura de los porteros
elif choice == 'Porteros vs altura':
    # Carga el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("kl.csv", encoding='latin-1')

    # Filtra los jugadores que tienen la posición "GK" (portero)
    keep_columns = ['Name', 'Club', 'Nationality', 'Age', 'Overall', 'Potential', 'Value', 'Wage', 'Special', 'Position']
    gk_df = df[df['Position'] == 'GK'][keep_columns]

    # Crea un histograma para mostrar la distribución de altura de los porteros
    fig, ax = plt.subplots()
    ax.hist(gk_df['Overall'], bins=10)
    ax.set_title("Distribución de altura de los porteros")
    ax.set_xlabel("Overall")
    ax.set_ylabel("Número de jugadores")
    st.pyplot(fig)
    st.text("Este gráfico muestra la distribución de altura de los porteros.")

elif choice == 'Mediocampistas y sus intercepciones':
    # Carga el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv("kl.csv", encoding='latin-1')
    # Filtrar los mediocampistas
    midfielders = df[df['Position'].isin(['CAM', 'CDM', 'CM'])]
    # Crear un histograma de las intercepciones de los mediocampistas
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.histplot(data=midfielders, x='Interceptions')
    plt.title('Intercepciones de los mediocampistas')
    plt.xlabel('Intercepciones')
    plt.ylabel('Cantidad de jugadores')
    st.pyplot()

# Muestra la valoración general promedio por posición para los delanteros
elif choice == 'Delanteros y valoraciones':
    data = pd.read_csv("kl.csv", encoding='latin-1')
    # Filtrar los delanteros
    forwards = data[(data['Position'] == 'ST') | (data['Position'] == 'CF') | (data['Position'] == 'LF') | (data['Position'] == 'RF')]

    # Calcular la valoración general promedio por posición para los delanteros
    grouped_ovr_fw = forwards.groupby("Position")["Overall"].mean()

    # Crear un gráfico de barras de la valoración general promedio por posición para los delanteros
    fig, ax = plt.subplots()
    ax = sns.barplot(x=grouped_ovr_fw.index, y=grouped_ovr_fw.values)
    ax.set_title("Valoración general promedio por posición para los delanteros")
    ax.set_xlabel("Posición")
    ax.set_ylabel("Valoración general promedio")
    st.pyplot(fig)
    st.text("Este gráfico muestra la valoración general promedio por posición para los delanteros.")

# Muestra la estadística de defensa de los centrocampistas defensivos
elif choice == 'Centrocampistas vs Vision':
    # Filtrar los centrocampistas defensivos
    data = pd.read_csv("kl.csv", encoding='latin-1')
    defensive_mids = data[data['Position'] == 'CDM']

    # Crear un histograma de la estadística de defensa de los centrocampistas defensivos
    fig, ax = plt.subplots()
    ax = sns.histplot(data=defensive_mids, x='Vision')
    ax.set_title("Estadística de defensa de los centrocampistas defensivos")
    ax.set_xlabel("Visión")
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)
    st.text("Este gráfico muestra la estadística de defensa de los centrocampistas defensivos.")