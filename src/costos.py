from dash import html, dcc
import pandas as pd
import plotly.express as px
from data_manager import load_data, get_unidades 

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

'''data'''
''#Data 1''


'''graficos'''
''# Gragfico 1 ''



''# Gragfico 2 ''



# grafico demo
fig = px.bar(unidades, x=unidades.index, y=unidades.values, title="Unidades por Tipo")


# Página de costos
costos_page = html.Div(
    [
        html.Div([
        # Primer fila de boxes
        html.Div(className="graph", children=[
            dcc.Graph(id='graph', figure=fig)
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph3', figure=fig)  
        ]),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

        html.Div([
            # Segunda fila de boxes
            html.Div(className="graph", children=[
                dcc.Graph(id='graph4', figure=fig)  
            ]),
            html.Div(className="graph", children=[
                dcc.Graph(id='graph5', figure=fig)  
            ]),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

        html.Div([
            # Primer fila de boxes
            html.Div(className="graph", children=[
                dcc.Graph(id='graph6', figure=fig)
            ]),
            
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),

    ]
)