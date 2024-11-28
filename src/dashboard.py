from dash import html, dcc

# Página principal
main_page = html.Div(
    className="main-page",
    children=[
        html.Div(
            className="main-grid",
            children=[
                dcc.Link(
                    href="/estadisticas",
                    children=html.Div([
                        html.Img(
                            src="/assets/images/estadisticas.jpg",
                            style={'width': '100%', 'height': 'auto'}
                        ),
                        html.Div("Estadísticas", style={'textAlign': 'center', 'padding': '10px'})
                    ]),
                    className="dashboard-image"
                ),
                dcc.Link(
                    href="/costos",
                    children=html.Div([
                        html.Img(
                            src="/assets/images/costos.jpg",
                            style={'width': '100%', 'height': 'auto'}
                        ),
                        html.Div("Costos", style={'textAlign': 'center', 'padding': '10px'})
                    ]),
                    className="dashboard-image"
                ),
                dcc.Link(
                    href="/metricas",
                    children=html.Div([
                        html.Img(
                            src="/assets/images/metricas.jpg",
                            style={'width': '100%', 'height': 'auto'}
                        ),
                        html.Div("Métricas", style={'textAlign': 'center', 'padding': '10px'})
                    ]),
                    className="dashboard-image"
                ),
                dcc.Link(
                    href="/insights",
                    children=html.Div([
                        html.Img(
                            src="/assets/images/insights.jpg",
                            style={'width': '100%', 'height': 'auto'}
                        ),
                        html.Div("Insights", style={'textAlign': 'center', 'padding': '10px'})
                    ]),
                    className="dashboard-image"
                )
            ]
        )
    ],
    style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'}
)