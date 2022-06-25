import numpy as np
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import preprocess


def dumbbell_plot(dataframe,input_year, input_month):
    
    #Filter the dataframe by selected year and selected month, making sure they fall in the desired range.
    dff = preprocess.filter_by_year_month(dataframe, input_year, input_month)

    #plot the dumbbell plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dff["Time"], y=dff["tapTime_PowLoss"], mode = 'markers', name='Tap Power Loss Time'))
    fig.add_trace(go.Scatter(x=dff["Time"], y=dff["tapOperationTime"], mode = 'markers', name="Tap Operation Time"))
    
    #updating the layout to set title, hover mode,...
    fig.update_layout(
        title="Tap Power Loss Time and Tap Operation Time for year: {}, Month: {}".format(input_year, input_month),
        xaxis_title="Time",
        xaxis=dict(showgrid=False,showticklabels=False),
        yaxis=dict(showgrid=False),
        hovermode="x unified",
        legend_title='<b> Time </b>',
        font=dict( color="RebeccaPurple"))
    
    #adding the vertical lines to the dumbbell plot
    for i in range(dff.shape[0]):
        fig.add_shape(
            type="line",
            layer="below",
            x0=dff['Time'].iloc[i], y0=dff['tapTime_PowLoss'].iloc[i],
            x1=dff['Time'].iloc[i], y1=dff['tapOperationTime'].iloc[i])
    return fig

    
