from dash import html
import pandas as pd
import plotly.express as px

# Página de costos
costos_page = html.Div(
    [
        html.H2("Costos", className="page-title"),
        html.P("Contenido de la página de costos."),
    ]
)