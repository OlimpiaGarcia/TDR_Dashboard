import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import category_encoders 
import pulp as pl 
import sklearn

from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression

from category_encoders import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from category_encoders import OneHotEncoder
from sklearn.preprocessing import PowerTransformer
from IPython.core.display import display_html
from scipy.stats import pearsonr, spearmanr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.tsa.seasonal import seasonal_decompose
import scipy.stats as stats
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
import scipy.stats as stats

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import roc_curve, auc
from statsmodels.api import Logit
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from statsmodels.formula.api import logit

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score