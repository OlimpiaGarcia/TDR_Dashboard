from dash import html, dcc

# Barra lateral
sidebar = html.Div(
    [
        dcc.Link(
            html.Img(
                src="assets/tdr_logo.png", 
                style={
                    "width": "60%", 
                    "height": "10%",  
                    "display": "block",  
                    "margin-left": "auto",  
                    "margin-right": "auto"  
                }
            ), 
            href="/home"
        ),
        #html.Hr(),
        dcc.Link("Home", href= "/home", className="sidebar-link"),
        #html.Hr(),
        dcc.Link("Estadísticas", href="/estadisticas", className="sidebar-link"),
        #html.Hr(),
        dcc.Link("Costos", href="/costos", className="sidebar-link"),
        #html.Hr(),
        dcc.Link("Métricas", href="/metricas", className="sidebar-link"),
        #html.Hr(),
        dcc.Link("Insights", href="/insights", className="sidebar-link"),
    ],
    className="sidebar",
)