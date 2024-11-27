from dash import html, dcc
import plotly.express as px
from data_manager import model_multiple, load_data, get_unidades, clean_data_subtotal  

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

'''Data de la pagina'''

# Data 1 Regrssion multiple
results_summary = model_multiple.summary().as_text()
markdown_text = f"""
# 
## {results_summary}
# """

# Data 2 Grficas
clean_data_subtotal = clean_data_subtotal


# Data 3 Conclusiones


'''Graficas de la pagina'''

#grafico 1:
fig1 = px.scatter(
    clean_data_subtotal,
    x='MTTR',
    y='SUBTOTAL',
    title='MTTR vs Costos',
    labels={'MTTR': 'MTTR', 'SUBTOTAL': 'Costos'}
)

# grafica 2
fig2 = px.scatter(
    clean_data_subtotal,
    x='Downtime',
    y='SUBTOTAL',
    title='Downtime vs Costor',
    labels={'Downtime': 'Downtime', 'SUBTOTAL': 'Costos'}
)



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
            dcc.Graph(id='graph1', figure=fig1)
        ]),
        html.Div(className="graph", children=[
            dcc.Graph(id='graph2', figure=fig2)  
        ]),
        ], style={'display': 'flex', 'justify-content': 'space-around', 'margin': '10px 0'}),


        html.Div(
            [
                html.Div(className="text", children=[
                    html.H1("Insights"),
                    html.P("El coeficiente es -23.2649 y es estadísticamente significativo (p = 0.003). Esto sugiere que un mayor tiempo para reparar (MTTR) tiene un efecto negativo sobre los costos de mantenimiento, es decir, a medida que aumenta el MTTR, los costos disminuyen, lo cual puede ser contraintuitivo."),
                    html.P("El coeficiente es 13.2195 y es estadísticamente significativo (p = 0.005). Esto indica que a mayor Downtime, los costos de mantenimiento tienden a aumentar."),
               
                ]), 
            ]
        ),


    ]
)