from dash import html, dcc
import plotly.express as px
from data_manager import load_data, get_unidades 

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

# grafico de unidades
fig_pie = px.pie(unidades, names=unidades.index, values=unidades.values, title= 'Tipo de Unidades')

# grafico demo
fig = px.bar(unidades, x=unidades.index, y=unidades.values, title="Unidades por Tipo")


# Página de estadisticas
estadisticas_page = html.Div([

    html.Div([
        dcc.Graph(
            id='unidades-graph',
            figure=fig_pie 
        ),
    ], style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}),

    html.Div([
        # Primer fila de boxes
        html.Div([dcc.Graph(id='graph2', figure=fig)], style={'border': '2px solid black', 'margin': '10px', 'height': 'auto', 'width': 'auto'}),
        html.Div([dcc.Graph(id='graph3', figure=fig)], style={'border': '2px solid black', 'margin': '10px', 'height': 'auto', 'width': 'auto'}),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

    html.Div([
        # Segunda fila de boxes
        html.Div([dcc.Graph(id='graph4', figure=fig)], style={'border': '2px solid black', 'margin': '10px', 'height': 'auto', 'width': 'auto'}),
        html.Div([dcc.Graph(id='graph5', figure=fig)], style={'border': '2px solid black', 'margin': '10px', 'height': 'auto', 'width': 'auto'}),
    ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),
    
], style={'padding': '10px'})


