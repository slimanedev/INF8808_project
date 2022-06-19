import dash
import preprocess
import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

#Use the preprocess to manage the data. You can add fucntions if it's necessary

df = pd.read_csv('./fakedata_to_delete.csv')

layout = html.Div([
            html.H1('Day by day data',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=px.bar(df, barmode='group', x='Years',
                    y=['Attribut1', 'Attribut2']))
                ]
    )