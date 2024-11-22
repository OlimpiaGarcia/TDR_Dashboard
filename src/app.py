from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from topbar import topbar
from sidebar import sidebar
from dashboard import main_page
from costos import costos_page
from predictivos import predictivos_page
from metricas import metricas_page 
from estadisticas import estadisticas_page

'''Inicializamos la aplicacion'''
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=["./assets/style.css"])
app.title = "Dashboard"

# layout
app.layout = html.Div(
    [
        dcc.Location(id="url"),
        sidebar,
        html.Div(id="page-content", className="content"),
    ],
    className="main-layout",
)

# Callback para actualizar el contenido del título dinámico en la barra superior
@app.callback(
    Output("topbar-title", "children"),
    [Input("url", "pathname")]
)

def update_top_bar(pathname):
    if pathname == "/costos":
        return "Costos"
    elif pathname == "/predictivos":
        return "Predictivos"
    elif pathname == "/metricas":
        return "Métricas"
    elif pathname == "/estadisticas":
        return "Estadísticas"
    elif pathname == "/home":
        return "Dashboard"
    elif pathname == "/":
        return "Dashboard"
    else:
        return "Error, página no encontrada"

# Callback para la navegacion
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def display_page(pathname):
    if pathname == "/costos":
        return html.Div([topbar, costos_page], className="page-layout")
    elif pathname == "/predictivos":
        return html.Div([topbar, predictivos_page], className="page-layout") 
    elif pathname == "/metricas":
        return html.Div([topbar, metricas_page], className="page-layout")
    elif pathname == "/estadisticas":
        return html.Div([topbar, estadisticas_page], className="page-layout")
    elif pathname == "/home":
        return html.Div([topbar, main_page], className="page-layout")
    else:
        return html.Div([topbar, main_page], className="page-layout")

# Corre la app
if __name__ == "__main__":
    app.run_server(debug=True)