import dash
import preprocess, box_graph
import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

#Use the preprocess to manage the data. You can add fucntions if it's necessary

df = pd.read_csv('./fakedata_to_delete.csv')

with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)

layout = html.Div([
            html.H1('Day by day data',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure= box_graph.plot_box_chart(oltc_data['tapAfter'], 
                        oltc_data['tapOperationTime'],
                )
            )
        ]
    )