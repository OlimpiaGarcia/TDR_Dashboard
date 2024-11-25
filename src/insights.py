from dash import html, dcc
import plotly.express as px
from data_manager import model_multiple, load_data, get_unidades 

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

'''Data de la pagina'''
results_summary = model_multiple.summary().as_text()
markdown_text = f"""
# 
## {results_summary}
# """


'''Graficas de la pagina'''
# grafico demo
fig = px.bar(unidades, x=unidades.index, y=unidades.values, title="Unidades por Tipo")



# Página de predictivos
insights_page = html.Div(
    [
        html.Div([
            html.Div(className="text", children=[
            dcc.Markdown(markdown_text),
            ]),
        ]),

        html.Div([
        html.Div(className="graph", children=[
            dcc.Graph(id='graph2', figure=fig)
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph3', figure=fig)  
        ]),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),


        html.Div(
            [
                html.Div(className="text", children=[
                    html.H1("Insights"),
                    html.P("En esta página se presentan los resultados de los análisis realizados."),
                    html.P("Se presentan los resultados de los análisis realizados."),                
                ]), 
            ]
        ),


    ]
)