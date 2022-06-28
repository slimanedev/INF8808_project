import numpy as np
import pandas as pd 
import plotly.graph_objects as go
import datetime
import hover_template
def scatter_recent_history_tap(data, selected_range):
    
    # Define the duration period. 
    # Duration Keys indicate the selected range (past week, past ten days, and past two weeks) 
    # Duration Values determines the number of days in that period.
    Duration = {'Past Week': 7, 'Past Ten Days': 10, 'Past Two Weeks': 14}
    
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
                      hovertemplate=hover_template.get_tap_history_hover_template())
    #showdividers=False dividerwidth ticklen tickmode = 'array'
    # Updating the layout
    fig.update_layout(
            title="Recent history of tap used from '{}' to '{}'".format(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')),
            xaxis=dict(title = 'Day-And-Time',gridcolor='#BDBDBD' ,side = 'bottom', type='multicategory',
                       tickfont=dict(size=10), tickangle = -45, position = 0.01, 
                       ticklabeloverflow = 'hide past domain'),
            yaxis = dict(title = 'Taps',ticks='',tickvals=np.arange(1,20, step=1)),
            plot_bgcolor = 'beige',
            font=dict( color="RebeccaPurple"))
    return fig
