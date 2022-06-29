import pandas as pd
import preprocess
import plotly.express as px
import template

def bar_plot_animation_Max_PowerLoss(data):
    '''
        Draws the animated bar chart. 
        This bar chart shows the maximum of power loss during the all years for each hours in day.
        We can also change the number of tap position by the slider.
        Arg:
            data: The data to be displayed
        Returns:
            fig: The figure comprising the animated bar chart
    '''
    
    # Plot bar chart for viz 3
    fig = px.bar(data,
        x = "Time_in_Hours",
        y = "Max_PowerLoss", 
        animation_frame = 'Tap Value', 
        custom_data = ['Max_loadCurr','Max_PowerLoss','Max_EnergyLoss','Max_CircCurr']
    )
    
    # Add hover_template
    fig = fig.update_traces(hovertemplate = template.get_viz3_hover_template())

    # Update layout
    fig.update_layout(
            xaxis = dict(
            tickmode = 'linear',
            tick0 = 0,
            dtick = 1
                ),
            title = 'Maximum of Power Loss during hours of the day with changing tap positions'
            )
    
    # Update axes
    fig.update_yaxes(range = [0, .9],
                     tick0 = 0, 
                     dtick = 0.1,
                     title_text = 'Max Power Loss (Kwt)')
    
    fig.update_xaxes(title_text = 'Hours in Day')
    
    # Set the hover in each frame
    for frame in fig.frames:
        for data in frame.data:
            data.hovertemplate = template.get_viz3_hover_template()
            
    return fig
