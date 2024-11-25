from dash import html, dcc

# Página principal
main_page = html.Div(
    [
        html.Div(
            [
                dcc.Link(className="box", children="Estadística", href="/estadisticas"),
                dcc.Link(className="box", children="Costos", href="/costos"),
                dcc.Link(className="box", children="Insights", href="/insights"),	
                dcc.Link(className="box", children="Métricas", href="/metricas"),
            ],
            className="main-grid",
        ),
    ],
    className="main-page",
)