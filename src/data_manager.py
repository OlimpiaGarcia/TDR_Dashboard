import plotly.express as px
import pandas as pd

# Cargamos los datos
def load_data():
    circuitos = pd.read_csv("./data/circuitos.csv")
    return circuitos

''' Pagina de estadistica'''

# Cargamos los datos de unidades
def get_unidades(circuitos):
    unidades = circuitos.groupby(['TipoUnidad'])['Unidad'].nunique()
    return unidades

