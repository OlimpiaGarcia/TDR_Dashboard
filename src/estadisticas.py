from dash import html, dcc
import pandas as pd
import plotly.express as px
from data_manager import load_data, get_unidades,regresion_limpio 

'''data'''

#   Data 1''

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

#     Data 2''

# crosstable de jobode + tipom
cross_tab_jobcode_tipom = pd.crosstab(circuitos['jobcode'], circuitos['TipoM'])

# Cambiando el DataFrame de formato ancho a largo para su uso con Plotly Express
cross_tab_jobcode_tipom = cross_tab_jobcode_tipom.reset_index().melt(id_vars=['jobcode'], var_name='TipoM', value_name='Count')

#   Data 3 ''
# Create a cross-tabulation between 'jobcode' and 'Unidad'
cross_tab_jobcode_unidad = pd.crosstab(circuitos['jobcode'], circuitos['Unidad'])

# Sumar el número de códigos de trabajo para cada unidad y seleccionar las 15 unidades principales
top_units = cross_tab_jobcode_unidad.sum(axis=0).nlargest(15)

# Filtrar la tabla cruzada para incluir solo las 15 unidades principales
filtered_cross_tab = cross_tab_jobcode_unidad[top_units.index]


# Convertir de formato ancho a largo
filtered_cross_tab = filtered_cross_tab.reset_index().melt(id_vars='jobcode', var_name='Unidad', value_name='Count of Job Codes')



#   Data 4 ''   
# Initialize an empty DataFrame to hold the filtered top 5 job codes for each of the top 15 units
filtered_data_complete = pd.DataFrame()

# Loop through each of the top 15 units
for unit in top_units.index:
    # Get the top 5 job codes for this specific unit
    top_jobcodes_unit = cross_tab_jobcode_unidad.loc[:, unit].nlargest(5)
    # Filter the original cross-tabulation data to include only these top job codes for this unit
    filtered_unit_data = cross_tab_jobcode_unidad.loc[top_jobcodes_unit.index, :]
    # Append to the overall DataFrame prepared for plotting
    filtered_data_complete = pd.concat([filtered_data_complete, filtered_unit_data], axis=0)

# Remove duplicates that may arise from overlapping top job codes among the top units
filtered_data_complete = filtered_data_complete.loc[~filtered_data_complete.index.duplicated(keep='first')]

# Select only the columns corresponding to the top 15 units for plotting
filtered_data_final = filtered_data_complete[top_units.index]
print(filtered_data_final)

# Convertir datos de formato ancho a largo para usar con Plotly Express





'''graficos'''

#    Grafico 1 ''

# grafico de unidades
fig_pie = px.pie(unidades, names=unidades.index, values=unidades.values)

# Ajustando el color de fondo del gráfico y del área de trazado
fig_pie.update_layout({
    'paper_bgcolor': '#f3e8ff',  # Color de fondo de la zona del gráfico (donde no hay datos)
    'plot_bgcolor': '#f3e8ff'  # Color de fondo de la zona de trazado (donde están los datos)
})


#    Grafico 2 ''Distribution of Maintenance Types across Job Codes'

# Creando el gráfico de barras apiladas
fig2 = px.bar(
    cross_tab_jobcode_tipom, 
    x='jobcode', 
    y='Count', 
    color='TipoM', 
    title='Distribution of Maintenance Types across Job Codes',
    labels={'Count': 'Count of Maintenance Types'}
)

# Personalizando el gráfico
fig2.update_layout(
    xaxis_title='Job Code',
    yaxis_title='Count of Maintenance Types',
    legend_title='TipoM',
    xaxis={'categoryorder':'total descending'}
)

# Mejorando la legibilidad de las etiquetas en el eje X
fig2.update_xaxes(tickangle=90)

#   Gragfico 3 ''Distribución de los jobcodes en las 15 unidades que más jobcodes tienen'

# Crear el gráfico de barras apiladas 
fig3 = px.bar(
    filtered_cross_tab, 
    x='Unidad', 
    y='Count of Job Codes', 
    color='jobcode',
    title='Distribución de los jobcodes en las 15 unidades que más jobcodes tienen'
)

# Personalizar el gráfico
fig3.update_layout(
    xaxis_title='Unidad ID',
    yaxis_title='Count of Job Codes',
    legend_title='Job Code',
    xaxis=dict(
        tickmode='array',
        tickvals=[1821, 1769, 1732, 1878, 1850, 1829, 1745, 1855, 1825, 1887, 1869, 1865, 1849, 1828, 1879 ],  # Valores específicos donde quieres ticks
        ticktext=['1821', '1769', '1732', '1878', '1850', '1829', '1745', '1855', '1825','1887', '1869', '1865', '1849', '1828', '1879']  # Texto específico para cada tick
    ),
    legend=dict(
        yanchor="top",
        y=1.20,
        xanchor="right",
        x=1.05
    )
)
# Mejorar la legibilidad de las etiquetas en el eje X
fig3.update_xaxes(tickangle=45)


#   Gragfico 4 ''Top 5 Job Codes for the Top 15 Units'

# Crear el gráfico de barras apiladas con Plotly
fig4 = px.bar(
    filtered_data_final,
    x='Unidad',
    y='Count of Job Codes',
    color='jobcode',  # Usa 'jobcode' como la dimensión de color para apilar las barras
    title='Los jobcodes más repetidos en las 15 unidades',
    labels={'Count of Job Codes': 'Cantidad de Job Codes', 'Unidad': 'ID de Unidad', 'jobcode': 'Código de Trabajo'}
)

# Personalizar el gráfico
fig4.update_layout(
    xaxis_title='ID de Unidad',
    yaxis_title='Cantidad de Job Codes',
    legend_title='Código de Trabajo',
    xaxis=dict(
        tickmode='array',
        tickvals=[1821, 1769, 1732, 1878, 1850, 1829, 1745, 1855, 1825, 1887, 1869, 1865, 1849, 1828, 1879 ],  # Valores específicos donde quieres ticks
        ticktext=['1821', '1769', '1732', '1878', '1850', '1829', '1745', '1855', '1825','1887', '1869', '1865', '1849', '1828', '1879']  # Texto específico para cada tick
    ),
    legend=dict(yanchor="top", y=1.20, xanchor="right", x=1)
)

# Mejorar la legibilidad de las etiquetas en el eje X
fig4.update_xaxes(tickangle=45)

# grafico demo
fig = px.bar(unidades, x=unidades.index, y=unidades.values, title="Unidades por Tipo")

# Página de estadísticas
estadisticas_page = html.Div([

    html.Div([
        html.Div([
            html.H2('Tipo de Unidades', style={
                'text-align': 'center', 
                'margin-bottom': '20px', 
                'padding': '50% 0',  # Padding para centrar el título verticalmente
                'font-size': '42px'  # Ajuste del tamaño de la fuente
            })
        ], style={'width': '30%'}),  

        html.Div([
            dcc.Graph(
                id='unidades-graph',
                figure=fig_pie 
            )
        ], style={
            'border': '2px solid black', 
            'margin': '10px', 
            'height': 'auto', 
            'width': '70%',  # Asegura que el gráfico ocupe la mayor parte del contenedor
            'padding': '2%',  # Añade padding para que el gráfico no toque los bordes
            'background-color': '#f3e8ff',  # Fondo 
            'border-radius': '10px'  # Bordes redondeados
        }),
        
    ], style={'display': 'flex', 'justify-content': 'center', 'padding': '10px',  'border-radius': '10px'}),  # Contenedor principal con fondo claro y bordes redondeados
        
    html.Div([
        # Primer fila de boxes
        html.Div(className="graph",
                children=[
                dcc.Graph(id='graph2', figure=fig2)
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph3', figure=fig3)  
        ]),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

    html.Div([
        # Segunda fila de boxes
        html.Div(className="graph", children=[
            dcc.Graph(id='graph4', figure=fig4)  
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph5', figure=fig)  
        ]),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),
    
], style={'padding': '10px'})

