from dash import html, dcc
import plotly.express as px
from data_manager import load_data, get_unidades 

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

# grafico de unidades
fig_pie = px.pie(unidades, names=unidades.index, values=unidades.values)

# Ajustando el color de fondo del gráfico y del área de trazado
fig_pie.update_layout({
    'paper_bgcolor': '#f3e8ff',  # Color de fondo de la zona del gráfico (donde no hay datos)
    'plot_bgcolor': '#f3e8ff'  # Color de fondo de la zona de trazado (donde están los datos)
})

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
                dcc.Graph(id='graph2', figure=fig)
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph3', figure=fig)  # Cambiado el id a 'graph3' para evitar duplicados
        ]),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

    html.Div([
        # Segunda fila de boxes
        html.Div(className="graph", children=[
            dcc.Graph(id='graph4', figure=fig)  # Cambiado el id a 'graph4' para evitar duplicados
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph5', figure=fig)  # Cambiado el id a 'graph5' para evitar duplicados
        ]),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),
    
], style={'padding': '10px'})

