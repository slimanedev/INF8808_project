import numpy as np
import pandas as pd 
import plotly.graph_objects as go
import datetime
import template

def scatter_recent_history_tap(data, selected_range):
    
    # Define the duration period. 
    # Duration Keys indicate the selected range (past week, past two weeks, ...). 
    # Duration Values determines the number of days in that period.
    Duration = {0: 7, 1: 14, 2: 21, 3: 30}
    
    # Get the data in the desired duration
    duration = Duration[selected_range]
    end = data['Date'].iloc[-1]      # The last data
    start = end - datetime.timedelta(days = duration)    # The start of the desired duration
    recent_data = data.loc[(data['Date'] >= start)& (data['Date'] <= (end))]   # Get the data in the desired range
    

    
    # Plot the scatter plot for the desired duration
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[recent_data["Date"].dt.strftime('%d'),recent_data["Time"]], y=recent_data['tapBefore'], 
                             mode = 'markers',marker = dict(color='blueviolet'),
                             name='Tap Frequency'))
    # Set hover template 
    fig.update_traces(customdata=pd.to_datetime(recent_data['Date']).dt.strftime('%Y-%B-%d'),
                      hovertemplate=template.get_tap_history_hover_template())
    
    # Updating the layout
    fig.update_layout(
            title="Recent history of tap used from '{}' to '{}'".format(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')),
            xaxis=dict(title = 'Day-And-Time',gridcolor='#BDBDBD' ,side = 'bottom', position = 0.01, type='multicategory',
                       tickfont=dict(size=10),ticklabeloverflow = 'hide past domain'),
            yaxis = dict(title = 'Taps',ticks='',tickvals=np.arange(1,20, step=1)),
            plot_bgcolor = 'beige',
            font=dict( color="RebeccaPurple"))
    return fig
