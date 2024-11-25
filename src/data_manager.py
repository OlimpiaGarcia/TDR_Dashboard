import plotly.express as px
import pandas as pd
import numpy as np

# Cargamos los datos
def load_data():
    circuitos = pd.read_csv("./data/circuitos.csv")
    return circuitos


# Cargamos los datos de unidades
def get_unidades(circuitos):
    unidades = circuitos.groupby(['TipoUnidad'])['Unidad'].nunique()
    return unidades

# creamos circuitos
circuitos = load_data()

# cragamos el csv de TOT
TOT = pd.read_excel('./data/TOT.xlsx')

# Crear etiquetas para cada trimestre
etiquetas_trimestres = [
    'T1_2022', 'T2_2022', 'T3_2022', 'T4_2022',
    'T1_2023', 'T2_2023', 'T3_2023', 'T4_2023',
    'T1_2024', 'T2_2024', 'T3_2024']


""" Crear Horas fuera de operación (Downtime) por unidad, Total de incidentes, Tiempo medio entre fallos (MTBF) y Tiempo medio para reparar (MTTR)"""
# copia de circuitos
lagdias_per_unit = circuitos.copy()

# Asegúrate de que la columna 'Trimestre' esté en el orden definido
lagdias_per_unit['Trimestre'] = pd.Categorical(lagdias_per_unit['Trimestre'], categories=etiquetas_trimestres, ordered=True)

# Agrupar por unidad y trimestre, y calcular el promedio de 'lagdias', agregar 0
mean_lagdias_by_unit_trimester = lagdias_per_unit.groupby(['Unidad', 'Trimestre'])['lagdias'].mean().round(2).reset_index(name='Downtime')

# Ordenar por 'T_UNITNUMBER' y 'Trimestre' siguiendo el orden de trimestres
mean_lagdias_sorted = mean_lagdias_by_unit_trimester.sort_values(by=['Unidad', 'Trimestre'])

# Agregar 0 a las columnas vacias
mean_lagdias_sorted['Downtime'] = mean_lagdias_sorted['Downtime'].fillna(0)

# incidentes
incidentes = circuitos.copy()

# Asegúrate de que la columna 'Trimestre' esté en el orden definido
incidentes['Trimestre'] = pd.Categorical(incidentes['Trimestre'], categories=etiquetas_trimestres, ordered=True)

#Agrupar por unidad y trimwstre y calcular cuantos orderid unicos hay
incidentes_by_unit_trimester = incidentes.groupby(['Unidad', 'Trimestre'])['Orderid'].nunique().reset_index(name='No.incidentes')

# Ordenar por 'T_UNITNUMBER' y 'Trimestre' siguiendo el orden de trimestres
incidentes_sorted = incidentes_by_unit_trimester.sort_values(by=['Unidad', 'Trimestre'])

# Agregar 0 a las columnas vacias
incidentes_sorted['No.incidentes'] = incidentes_sorted['No.incidentes'].fillna(0)

# juntar DF incidentes_sorted y  mean_lagdias_sorted
fix_metrics = incidentes_sorted.merge(mean_lagdias_sorted, on=['Unidad', 'Trimestre'])

# convertir columna unidad en numero entero
fix_metrics['Unidad'] = fix_metrics['Unidad'].astype(int)

"""Hacvemos calculos con el archivo TOT"""	

# renombrar columna 'T_UNITNUMBER' a 'Unidad'
TOT = TOT.rename(columns={'T_UNITNUMBER': 'Unidad', 'days': 'TOT'})

# pasar trimestre a category
TOT['Trimestre'] = pd.Categorical(TOT['Trimestre'], categories=etiquetas_trimestres, ordered=True)

# hacer unidad index
TOT = TOT.set_index('Unidad')

# drop Unnamed: 0
TOT = TOT.drop(columns=['Unnamed: 0'])

# juntar DF de MTBF y TOT
fix_metrics = fix_metrics.merge(TOT, on=['Unidad', 'Trimestre'])

#Eliminar columnas vacias
fix_metrics = fix_metrics.dropna()

# # Asegúrate de que la columna 'Trimestre' esté en el orden definido
fix_metrics['Trimestre'] = pd.Categorical(fix_metrics['Trimestre'], categories=etiquetas_trimestres, ordered=True)

# calcular MTBF
fix_metrics['MTBF'] = (fix_metrics['TOT'] / fix_metrics['No.incidentes']).round(2)

# si mtbf es inf rellenar con TOT
fix_metrics['MTBF'] = fix_metrics['MTBF'].replace(np.inf, np.nan)
fix_metrics['MTBF'] = fix_metrics['MTBF'].fillna(fix_metrics['TOT'])

# calcular mttr
fix_metrics['MTTR'] = (fix_metrics['Downtime'] / fix_metrics['No.incidentes']).round(2)

# si mttr es inf rellenat con 0
fix_metrics['MTTR'] = fix_metrics['MTTR'].replace(np.inf, np.nan)
fix_metrics['MTTR'] = fix_metrics['MTTR'].fillna(0)

# Ordenar por trimestre
fix_metrics_sorted = fix_metrics.sort_values(by=['Unidad', 'Trimestre'])

"""hacemos archivo de regresion"""
regresion = circuitos.copy()
regresion['Trimestre'] = pd.Categorical(regresion['Trimestre'], categories=etiquetas_trimestres, ordered=True)
regresion['Unidad'] = regresion['Unidad'].astype(int)
regresion = regresion.merge(fix_metrics_sorted, on=['Unidad', 'Trimestre'])
regresion_limpio = regresion[regresion['opened'] != regresion['closed']]
clean_data_subtotal = regresion_limpio[['MTBF', 'MTTR', 'Downtime', 'SUBTOTAL']].dropna() 


""""Cargamos los df necesarios para las estadisticas:"""

costos_por_tipo_unidad = circuitos.groupby('TipoUnidad')['SUBTOTAL'].sum()
costos_por_unidad = circuitos.groupby('Unidad')['SUBTOTAL'].sum().sort_values(ascending=False)
costos_por_año_tipo_unidad = circuitos.groupby(['aniocomplete', 'TipoUnidad'])['SUBTOTAL'].sum()
costos_por_año_unidad = circuitos.groupby(['aniounidad', 'Unidad'])['SUBTOTAL'].sum()
costos_por_añodeunidad = circuitos.groupby(['aniounidad'])['SUBTOTAL'].sum()
costo_por_jobcode = circuitos.groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
costo_por_TipoM = circuitos.groupby('TipoM')['SUBTOTAL'].sum().sort_values(ascending=False)
costo_por_jobcode = circuitos.groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
costo_por_jobcode_unplanned = circuitos[circuitos['TipoM'].isin(['Correctivo', 'Otro'])].groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
costo_por_jobcode_planned=circuitos[circuitos['TipoM'] == 'Preventivo'].groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
df_TipoAB=circuitos[circuitos['jobcode'].str.contains('preventivo A|preventivo B', na=False)]
df_TipoAB=df_TipoAB[df_TipoAB['jobcode'] != '000074 - Derivado de preventivo Arrastre']
cantidad_por_TipoAB=df_TipoAB.groupby('jobcode')['Orderid'].count().sort_values(ascending=False)
costo_por_TipoAB=df_TipoAB.groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
df_TipoM123=circuitos[circuitos['jobcode'].str.contains('M1|M2|M3', na=False)]
cantidad_por_TipoM123=df_TipoM123.groupby('jobcode')['Orderid'].count()
costo_por_TipoM123=df_TipoM123.groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
df_TipoSH12=circuitos[circuitos['jobcode'].str.contains('SH 1|SH 2', na=False)]
cantidad_por_TipoSH12=df_TipoSH12.groupby('jobcode')['Orderid'].count()
costo_por_TipoSH12=df_TipoSH12.groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
df_Tipollantas=circuitos[circuitos['jobcode'].str.contains('llanta|Llantas|Llanta', na=False)]
cantidad_por_Tipollantas=df_Tipollantas.groupby('jobcode')['Orderid'].count()
costo_por_Tipollantas=df_Tipollantas.groupby('jobcode')['SUBTOTAL'].sum().sort_values(ascending=False)
regresion_limpio_tractor = regresion_limpio[regresion_limpio['TipoUnidad'] == 'TRACTOR']
regresion_limpio_tractor = regresion_limpio_tractor.dropna(subset=['Kilometraje'])
regresion_limpio_trailer = regresion_limpio[regresion_limpio['TipoUnidad'] == 'TRAILER']
correct_data = regresion_limpio.copy()
selected_features = correct_data[['MTBF', 'MTTR', 'Downtime', 'lagdias', 'No.incidentes']].copy()
selected_features = selected_features.dropna()
