from dash import html

# Página principal
main_page = html.Div(
    [
        html.Div(
            [
                html.Div(className="box", children="Estadística"),
                html.Div(className="box", children="Costos"),
                html.Div(className="box", children="Predictivos"),
                html.Div(className="box", children="Métricas"),
            ],
            className="main-grid",
        ),
    ],
    className="main-page",
)