import pandas as pd
import preprocess
import plotly.express as px
import template

def area_plot_Energy_Loss(data):
    '''
        Draws the area chart. 
        This area chart shows the average energy loss in each month of the year.
        Arg:
            data: The data to be displayed
        Returns:
            fig: The figure comprising the area chart
    '''
    # Plot area chart for viz 7.1
    fig = px.area(data,
        x = "Date",
        y = "tapEnergyLoss",
    )
    
    fig = fig.update_traces(hovertemplate = template.get_viz7_1_hover_template())
    
    # Update axes
    fig.update_xaxes(title_text = 'Date in Year')
    fig.update_yaxes(range = [0, .026], title_text = 'Energy Loss')

    return fig

def area_plot_Power_Loss(data):
    '''
        Draws the area chart. 
        This area chart shows the average power loss in each month of the year.
        Arg:
            data: The data to be displayed
        Returns:
            fig: The figure comprising the area chart
    '''
    # Plot area chart for viz 7.2
    fig = px.area(data,
        x = "Date",
        y = "tapPowerLossAmp",
    )
    
    fig = fig.update_traces(hovertemplate = template.get_viz7_2_hover_template())
    
    # Update axes
    fig.update_xaxes(title_text = 'Date in Year')
    fig.update_yaxes(range = [0, 1], title_text = 'Power Loss Average Amplitude (kw)')
    return fig
    
