from dash import html

# Top Bar
topbar = html.Div(
    [
        html.Div(id="topbar-title", className="topbar-left"), 
        html.Div("Circuitos", className="topbar-right"),  
    ],
    className="topbar",
)