import plotly.express as px
import numpy as np
import pandas as pd 
import datetime
import template

def plot_line_chart(data, selected_range):
    '''
        Draws the line chart.

        Arg:
            data: The data to be displayed
            selected_range: The selected period of time form the slider
        Returns:
            fig: The figure comprising the drawn line plot
    '''
    
    '''
    Define the duration period. 
    Duration Keys indicate the selected range (past week, past two weeks, past three weeks, and past month) 
    Duration Values determines the number of days in that period.
    '''
    Duration = {0:7, 1:14, 2:21, 3:30}
    
    # Get the data in the desired duration
    duration = Duration[selected_range]
    end = data['Date'].iloc[-1]                                                 # The last data
    start = end - datetime.timedelta(days = duration)                           # The start of the desired duration
    recent_data = data.loc[(data['Date'] >= start)& (data['Date'] <= (end))]    # Get the data in the desired range
    
    # Plot the scatter plot for the desired duration
    # Plot line chart for viz 1
    fig = px.line(recent_data,
        x = "Date",
        y = "tapAfter",
        line_shape='vh'
    )
    
    # Set hover template 
    fig.update_traces(hovertemplate = template.get_hover_template_viz1())

    # Updating the layout
    fig.update_layout(
            title = "Line-plot for the tap switching patterns from '{}' to '{}'".format(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')),
            xaxis_title = "Day",
            yaxis = dict(title = 'Taps',
                ticks = '',
                tickvals = np.arange(1,20, step=1)),
            yaxis_title = "Tap number"
        )
        
    return fig
