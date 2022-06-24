import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



def dumbbell_plot(dataframe,input_year, input_month):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    df = dataframe.loc[dataframe['Date'].dt.year == int(input_year)]
    dff = df.loc[df['Date'].dt.month == int(input_month)]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dff["Time"], y=dff["tapTime_PowLoss"], mode = 'markers', name='Tap PowLoss Time'))
    fig.add_trace(go.Scatter(x=dff["Time"], y=dff["tapOperationTime"], mode = 'markers', name="Tap Operation Time"))
    fig.update_layout(
        title="Tap PowLoss Time and Tap Operation Time for year: {}, Month: {}".format(input_year, input_month),
        xaxis_title="Time",
        xaxis=dict(showgrid=False,showticklabels=False),
        yaxis=dict(showgrid=False),
        hovermode="x unified",
        #plot_bgcolor = 'white',
        font=dict( color="RebeccaPurple"))
    for i in range(dff.shape[0]):
        fig.add_shape(
            type="line",
            layer="below",
            x0=dff['Time'].iloc[i], y0=dff['tapTime_PowLoss'].iloc[i],
            x1=dff['Time'].iloc[i], y1=dff['tapOperationTime'].iloc[i])
    fig.update_layout(legend_title='<b> Time </b>')
    return fig

    