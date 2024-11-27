from dash import html, dcc
import pandas as pd
import plotly.express as px
from data_manager import load_data, get_unidades, costo_por_TipoM, costo_por_TipoM123, costo_por_jobcode

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

'''data'''
''#Data 1''
costo_por_TipoM = costo_por_TipoM.reset_index()

#   '''data 2'''
# Costos por Trimestre y Tipo de Mantenimiento
filtro_datos = circuitos[circuitos['TipoM'].isin(['Preventivo', 'Correctivo'])]
costos_por_trimestre = filtro_datos.groupby(['Trimestre', 'TipoM'])['SUBTOTAL'].sum().reset_index() # Reset index to use 'Trimestre' as a column

#     '''data 3'''
costo_por_TipoM123 = pd.DataFrame(costo_por_TipoM123).reset_index()

#    '''data 4'''
unidad_edad = circuitos.copy()

unidad_edad['EdadUnidad'] = pd.to_datetime('now').year - unidad_edad['aniounidad']
regresion_preventivo = unidad_edad[unidad_edad['TipoM'] == 'Preventivo']

# Agrupar por Tipo de Unidad y Edad de la Unidad, calcular el costo promedio de mantenimiento preventivo
costos_por_tipo_y_edad = regresion_preventivo.groupby(['TipoUnidad', 'EdadUnidad'])['SUBTOTAL'].mean().reset_index()

# Ordenar los resultados para mejor visualización
costos_por_tipo_y_edad = costos_por_tipo_y_edad.sort_values(by=['TipoUnidad', 'EdadUnidad'])

#    '''data 5'''
costo_por_jobcode = costo_por_jobcode.reset_index()



'''graficos'''
''      # Gragfico 1  costo por tipo de mantenimiento'''
fig1 = px.bar(
    costo_por_TipoM, 
    x='TipoM',
    y='SUBTOTAL',
    color='TipoM',
    color_discrete_sequence=['#F58D2A', '#0D3372', '#F7BE31', '#CBD7ED', '#FBE1B0'],  # Colores personalizados
    title='Costos por Tipo de Mantenimiento'
)

# Personalizar el diseño del gráfico
fig1.update_layout(
    xaxis_title='Tipo de Mantenimiento',
    yaxis_title='Costo Total',
    title_x=0.5,  # Centrar el título
    plot_bgcolor='white',  # Fondo blanco
    paper_bgcolor='white'  # Fondo blanco para toda el área del gráfico
)


''#     Gragfico 2  Costos por Trimestre y Tipo de Mantenimiento'''
fig2 = px.bar(
    costos_por_trimestre,  
    x='Trimestre',  # Usar 'Trimestre' en el eje X
    y='SUBTOTAL',  # Usar 'SUBTOTAL' en el eje Y
    color='TipoM',  # Diferenciar por 'TipoM'
    barmode='group',  # Agrupar barras por 'TipoM' dentro de cada trimestre
    color_discrete_sequence=['#F58D2A', '#0D3372'],  # Colores personalizados
    title='Costos por Trimestre y Tipo de Mantenimiento'
)

# Personalizar el diseño del gráfico
fig2.update_layout(
    xaxis_title='Trimestre',
    yaxis_title='Costo Total',
    title_x=0.5,  # Centrar el título
    plot_bgcolor='white',  # Fondo blanco
    paper_bgcolor='white'  # Fondo blanco para toda el área del gráfico
)



#     Gragfico 3 ''
fig3 = px.bar(
    costo_por_TipoM123,  # Aseguramos que los índices estén como columnas
    x='jobcode',  # Job codes en el eje X
    y='SUBTOTAL',  # Costos totales en el eje Y
    color='jobcode',  # Diferenciar por Job Code
    color_discrete_sequence=['#F58D2A', '#0D3372', '#F7BE31', '#CBD7ED', '#FBE1B0'],  # Colores personalizados
    title='Costos por Job Code (M1, M2, M3)'
)

# Personalizar el diseño
fig3.update_layout(
    xaxis_title='Job Code',
    yaxis_title='Costo Total',
    title_x=0.5,  # Centrar el título
    xaxis=dict(
        categoryorder='total descending'  # Ordenar los valores descendente según el total
    ),
    plot_bgcolor='white',  # Fondo blanco para el gráfico
    paper_bgcolor='white'  # Fondo blanco para el área general
)

#     Gragfico  4 Costos por Tipo de Unidad y Edad de la Unidad''
fig4 = px.bar(
    costos_por_tipo_y_edad,
    x='EdadUnidad',
    y='SUBTOTAL',
    color='TipoUnidad',  # Agrupar por Tipo de Unidad
    barmode='group',  # Mostrar barras agrupadas
    title='Costo Promedio de Mantenimiento Preventivo por Tipo de Unidad y Edad',
    labels={
        'EdadUnidad': 'Edad de la Unidad (años)',
        'SUBTOTAL': 'Costo Promedio de Mantenimiento Preventivo ($)',
        'TipoUnidad': 'Tipo de Unidad'
    }
)

fig4.update_layout(
    xaxis_title='Edad de la Unidad (años)',
    yaxis_title='Costo Promedio de Mantenimiento Preventivo ($)',
    legend_title='Tipo de Unidad',
    title_x=0.5,  # Centrar el título
    xaxis=dict(
        tickmode = 'linear',
        type='category'  
    ),
    plot_bgcolor='white',  # Fondo blanco para el área de trazado
    paper_bgcolor='white'  # Fondo blanco para todo el gráfico
)

fig4.update_xaxes(tickangle=0)

#     Gragfico  5 ''
fig5 = px.bar(
    costo_por_jobcode,
    x='jobcode',
    y='SUBTOTAL',
    color='jobcode',
    color_discrete_sequence=['#F58D2A', '#0D3372', '#F7BE31', '#CBD7ED', '#FBE1B0']
)

fig5.update_layout(
    title='Costos por Job Code',
    xaxis_title='Job Code',
    yaxis_title='Costo Total',
    title_x=0.5
)



# grafico demo
fig = px.bar(unidades, x=unidades.index, y=unidades.values, title="Unidades por Tipo")


# Página de costos
costos_page = html.Div(
    [
        html.Div([
        # Primer fila de boxes
        html.Div(className="graph", children=[
            dcc.Graph(id='graph', figure=fig1)
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph2', figure=fig2)  
        ]),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

        html.Div([
            # Segunda fila de boxes
            html.Div(className="graph", children=[
                dcc.Graph(id='graph3', figure=fig3)  
            ]),
            html.Div(className="graph", children=[
                dcc.Graph(id='graph4', figure=fig4)  
            ]),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

        html.Div([
            # Primer fila de boxes
            html.Div(className="graph", children=[
                dcc.Graph(id='graph6', figure=fig5)
            ]),
            
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

    ]
)