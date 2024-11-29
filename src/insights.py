from dash import html, dcc
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from data_manager import load_data, get_unidades

# Carga los datos desde el archivo CSV
circuitos = load_data()

# Obtiene las unidades agrupadas y cuenta por tipo de unidad
unidades = get_unidades(circuitos)

# Data 1: ARIMA
ts_data = circuitos.copy()
quarterly_costs = ts_data.groupby('Trimestre')['SUBTOTAL'].sum()
quarterly_costs.index = quarterly_costs.index.str.replace(r'(T)(\d)_(\d{4})', r'\3-Q\2', regex=True)
quarterly_costs.index = pd.PeriodIndex(quarterly_costs.index, freq='Q').to_timestamp()
quarterly_costs.sort_index(inplace=True)  # Asegurar que el índice esté ordenado

model_quarterly = ARIMA(quarterly_costs, order=(1, 1, 1), enforce_stationarity=False, enforce_invertibility=False)
arima_result_quarterly = model_quarterly.fit()
forecast_quarterly = arima_result_quarterly.get_forecast(steps=4)
forecast_quarterly_series = forecast_quarterly.predicted_mean
conf_int_quarterly = forecast_quarterly.conf_int()

forecast_dates = pd.date_range(start=quarterly_costs.index[-1] + pd.offsets.QuarterEnd(), periods=5, freq='Q')[1:]
forecast_quarterly_series.index = forecast_dates
conf_int_quarterly.index = forecast_dates

# Gráfico ARIMA
fig = go.Figure()
fig.add_trace(go.Scatter(x=quarterly_costs.index, y=quarterly_costs, mode='lines+markers', name='Actual'))
fig.add_trace(go.Scatter(x=forecast_quarterly_series.index, y=forecast_quarterly_series, mode='lines+markers', name='Forecast'))
fig.add_trace(go.Scatter(
    x=list(forecast_quarterly_series.index) + list(forecast_quarterly_series.index[::-1]),
    y=list(conf_int_quarterly.iloc[:, 1]) + list(conf_int_quarterly.iloc[:, 0][::-1]),
    fill='toself', fillcolor='rgba(255, 192, 203, 0.3)', line=dict(color='rgba(255,255,255,0)'),
    name='Confidence Interval'
))
fig.update_layout(
    title='ARIMA Forecast for Quarterly Costs',
    xaxis_title='Trimestre',
    yaxis_title='Subtotal Cost (millions)',
    legend_title='Legend',
    xaxis=dict(
        tickmode='array',
        tickvals=list(quarterly_costs.index) + list(forecast_quarterly_series.index),
        ticktext=[str(x.strftime('%Y-Q')) + str((x.month - 1) // 3 + 1) for x in list(quarterly_costs.index) + list(forecast_quarterly_series.index)],
        type='category'
    )
)

# Gráfico demo
fig1 = px.bar(unidades, x=unidades.index, y=unidades.values, title="Unidades por Tipo")

# Página de predictivos
insights_page = html.Div([
    html.Div([
        html.Div(className="long-graph", children=[
            dcc.Graph(id='graph', figure=fig)
        ]),
    ]),
    html.Div([
        html.Div(className='text', children=[
            html.H1("Estrategias de Reducción de Costos"),
            html.Table([
                html.Thead(
                    html.Tr([
                        html.Th("Estrategia", style={'padding-bottom': '1rem'}),  # Aplicando estilo al elemento Th
                        html.Th("Descripción", style={'padding-bottom': '1rem'})  # Aplicando estilo al elemento Th
                    ])
            ),  html.Tbody([
                    html.Tr([html.Td("MP vs MC"), html.Td("Fórmula Conocida como “Regla 80/20” (Simpson, 2024)", style={'padding-bottom': '1rem'})]),
                    html.Tr([html.Td("Unidades Alto Costo"), html.Td("Identificar y Sustituir Unidades de Alto Costo cuando sea conveniente. Costo - Beneficio", style={'padding-bottom': '1rem'})]),
                    html.Tr([html.Td("SENSORES IoT Mecánicos"), html.Td("Recopilación de datos en tiempo real. Combinado con la analítica predictiva, se pueden predecir fallas antes de que ocurran y optimizar procesos.", style={'padding-bottom': '1rem'})]),
                    html.Tr([html.Td("Talleres"), html.Td("Asegurar un equipo de mecánicos capacitados, así como herramientas modernas que permitan diagnosticar y reparar fallas con mayor facilidad y rapidez. Considerar Outsourcing", style={'padding-bottom': '1rem'})])

                ])
            ])
        ])
    ]),
    html.Div([
        html.Div(className="text", children=[
            html.H1("Insights"),
            html.P("Los datos históricos muestran un incremento constante en los costos de mantenimiento hasta aproximadamente el cuarto trimestre de 2023. Después de ese punto, parece haber una leve estabilización."),
            html.P("Pero con los datos se proyecta un incremento moderado en los costos durante los próximos 4 trimestres de alrededor de los 2.5 millones, con ligeros aumentos en cada trimestre."),
            html.P("Sin embargo, las bandas de los intervalos de confianza (en rosa) muestran un rango de incertidumbre considerable. Esto sugiere que, aunque la tendencia proyectada es al alza, los costos podrían variar significativamente. Por lo que es posible que los costos reales se mantengan dentro del límite inferior del intervalo de confianza.")
        ])
    ])
])
