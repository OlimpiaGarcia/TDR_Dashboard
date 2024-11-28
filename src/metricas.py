from dash import html
from dash import dash_table
import pandas as pd
import plotly.express as px
from data_manager import circuitos, fix_metrics

# Describe de Mttr:
mttr_desc = fix_metrics['MTTR'].describe().round(2)
mttr_desc = pd.DataFrame(mttr_desc)
mttr = [
    {"Estadística": index, "Valor": row['MTTR']}
    for index, row in mttr_desc.iterrows()
]

# Describe de Mtbf:
mtbf_desc = fix_metrics['MTBF'].describe().round(2)
mtbf_desc = pd.DataFrame(mtbf_desc)
mtbf = [
    {"Estadística": index, "Valor": row['MTBF']}
    for index, row in mtbf_desc.iterrows()
]

# Describe de Downtime:
downtime_desc = fix_metrics['Downtime'].describe().round(2)
downtime_desc = pd.DataFrame(downtime_desc)
downtime = [
    {"Estadística": index, "Valor": row['Downtime']}
    for index, row in downtime_desc.iterrows()
]

# Describe de failure rate:
failure_rate_desc = circuitos['lagdias'].describe().round(2)
failure_rate_desc = pd.DataFrame(failure_rate_desc)
failure_rate = [
    {"Estadística": index, "Valor": row['lagdias']}
    for index, row in failure_rate_desc.iterrows()
]

# Describe de Matenimineto:
costos_mtto_desc = circuitos[['Unidad', 'SUBTOTAL']].describe()
costos_mtto_desc = pd.DataFrame(costos_mtto_desc['SUBTOTAL'].round(2))
mtto = [
    {"Estadística": index, "Valor": row['SUBTOTAL']}
    for index, row in costos_mtto_desc.iterrows()
]


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
                               {"name": "Estadística", "id": "Estadística"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=mttr,
                            style_cell={'textAlign': 'center'},
                            style_header={
                                'backgroundColor': '#b6c7e5ff',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ],
                            style_table={'width': '350px', 'height': '400px'},  # Tamaño consistente
                        )
                    ], style={'textAlign': 'center'}  # Centrar todo el bloque
                ),
                html.Div(
                    [
                        html.H1("Mean Time Between Failures (MTBF)"),
                        dash_table.DataTable(
                            columns=[
                               {"name": "Estadística", "id": "Estadística"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=mtbf,
                            style_cell={'textAlign': 'center'},
                            style_header={
                                'backgroundColor': '#fbe1b0ff',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ],
                            style_table={'width': '350px', 'height': '400px'},  # Tamaño consistente
                        )
                    ], style={'textAlign': 'center'}  # Centrar todo el bloque
                ),
                html.Div(
                    [
                        html.H1("Downtime"),
                        dash_table.DataTable(
                            columns=[
                               {"name": "Estadística", "id": "Estadística"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=downtime,
                            style_cell={'textAlign': 'center'},
                            style_header={
                                'backgroundColor': '#b6c7e5ff',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ],
                            style_table={'width': '350px', 'height': '400px'},  # Tamaño consistente
                        )
                    ], style={'textAlign': 'center'}  # Centrar todo el bloque
                ),

            ],
            style={'display': 'flex', 'justify-content': 'space-around', 'margin': '1px 0'}
        ),

        # Segunda fila de boxes
        html.Div(
            [
                html.Div(
                    [
                        html.H1("Failure Rate"),
                        dash_table.DataTable(
                            columns=[
                                {"name": "Estadística", "id": "Estadística"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=failure_rate,
                            style_cell={'textAlign': 'center'},
                            style_header={
                                'backgroundColor': '#f68d2bff',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ],
                            style_table={'width': '350px', 'height': '400px'},  # Tamaño consistente
                        )
                    ], style={'textAlign': 'center'}  # Centrar todo el bloque
                ),
                html.Div(
                    [
                        html.H1("Costos de Mantenimiento"),
                        dash_table.DataTable(
                            columns=[
                               {"name": "Estadística", "id": "Estadística"},
                                {"name": "Valor", "id": "Valor"}
                            ],
                            data=mtto,
                            style_cell={'textAlign': 'center'},
                            style_header={
                                'backgroundColor': '#b6c7e5ff',
                                'fontWeight': 'bold'
                            },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248, 248, 248)'},
                                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'}
                            ],
                            style_table={'width': '350px', 'height': '400px'},  # Tamaño consistente
                        )
                    ], style={'textAlign': 'center'}  # Centrar todo el bloque
                ),
            ],
            style={'display': 'flex', 'justify-content': 'space-around', 'margin': '1px 0'}
        ),

    ]
)
