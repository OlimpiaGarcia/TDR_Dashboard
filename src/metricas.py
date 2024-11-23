from dash import html
from dash import dash_table
import plotly.express as px
from data_manager import load_data, get_unidades 

# Carga los datos desde el archivo CSV
circuitos = load_data()

# hacer un describe
describe = circuitos.describe()



# Página de métricas
metricas_page = html.Div(
    [
        # Primer fila de boxes
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Mean Time to Repair (MTTR)"),
                        dash_table.DataTable(
                            columns=[
                                {"name": "Medida", "id": "Medida"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=describe.to_dict('records'),
                            style_cell={'textAlign': 'left'},
                            style_header={
                                'backgroundColor': 'white',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ]
                        )
                    ],
                ),
                html.Div(
                    [
                        html.H1("Mean Time to Repair (MTTR)"),
                        dash_table.DataTable(
                            columns=[
                                {"name": "Medida", "id": "Medida"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=describe.to_dict('records'),
                            style_cell={'textAlign': 'left'},
                            style_header={
                                'backgroundColor': 'white',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ]
                        )
                    ]
                ),
            ],
            style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}
        ),

        # Segunda fila de boxes
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Mean Time to Repair (MTTR)"),
                        dash_table.DataTable(
                            columns=[
                                {"name": "Medida", "id": "Medida"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=describe.to_dict('records'),
                            style_cell={'textAlign': 'left'},
                            style_header={
                                'backgroundColor': 'white',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ]
                        )
                    ]
                ),
                html.Div(
                    [
                        html.H1("Mean Time to Repair (MTTR)"),
                        dash_table.DataTable(
                            columns=[
                                {"name": "Medida", "id": "Medida"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=describe.to_dict('records'),
                            style_cell={'textAlign': 'left'},
                            style_header={
                                'backgroundColor': 'white',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ]
                        )
                    ]
                ),
            ],
            style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}
        ),

        # Tercera fila de boxes
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Mean Time to Repair (MTTR)"),
                        dash_table.DataTable(
                            columns=[
                                {"name": "Medida", "id": "Medida"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=describe.to_dict('records'),
                            style_cell={'textAlign': 'left'},
                            style_header={
                                'backgroundColor': 'white',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ]
                        )
                    ]
                ),
            ],
            style={'display': 'flex', 'justify-content': 'center', 'margin': '10px 0'}
        ),
    ]
)
