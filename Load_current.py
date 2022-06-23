import pandas as pd
import numpy as np
import datetime as datetime
import plotly.graph_objects as go


def get_transformer_avg_current_plot (data1,data2, year):   
    
    idx1=data1['Date'].dt.year == year
    idx2=data2['Date'].dt.year == year
    
    df1=data1[idx1] ; df2=data2[idx2]

    df1=df1.groupby('Time', as_index=False).mean()
    df2=df2.groupby('Time', as_index=False).mean()

    fig=go.Figure()

    fig = fig.add_trace(go.Scatter(x=df1.Time, y=df1.TrafoLoadCurr,
                        mode='lines',
                        name='Weekdays',
                        marker_color='green',
                        line_shape='spline'))
    
    fig = fig.add_trace(go.Scatter(x=df2.Time, y=df2.TrafoLoadCurr,
                        mode='lines',
                        name='Weekends',
                        marker_color='blue',
                        line_shape='spline'))


    fig.update_layout(title= f'Average Load current on Transformer during hours of the day in year {year}',
                    xaxis_title='hours of the day',
                    yaxis_title= 'Load current (KA)',
                    #height=500, width=800)
    )
    return fig

def get_transformer_max_current_plot (data1,data2, year):   
    
    idx1=data1['Date'].dt.year == year
    idx2=data2['Date'].dt.year == year
    
    df1=data1[idx1] ; df2=data2[idx2]

    df1=df1.groupby('Time', as_index=False).max()
    df2=df2.groupby('Time', as_index=False).max()

    fig=go.Figure()

    fig = fig.add_trace(go.Bar(x=df1.Time, y=df1.TrafoLoadCurr,
                        name='Weekdays',
                        marker_color='green' #'rgb(26, 118, 255)',
                        ))
    
    fig = fig.add_trace(go.Bar(x=df2.Time, y=df2.TrafoLoadCurr,
                        name='Weekends',
                        marker_color= "blue" #'rgb(55, 83, 109)',
                       ))


    fig.update_layout(title= f'Maximum Load current on Transformer during hours of the day in year {year}',
                    xaxis_title='hours of the day',
                    yaxis_title= 'Load current (KA)',
                    height=500, width=1000)

    return fig