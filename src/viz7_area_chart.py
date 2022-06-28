import pandas as pd
import preprocess
import plotly.express as px


def area_plot_Energy_Loss(data):

    # Plot area chart for viz 7.1
    fig = px.area(data,
        x = "Date",
        y = "tapEnergyLoss",
        color = 'year',
    )

    # Update axes 
    fig.update_yaxes(range = [0, .025],
        tick0 = 0,
        dtick = 0.002,
        title_text = 'Energy Loss',
    )

    fig.update_xaxes(title_text = 'Date in Year')
     fig.update_layout(
            title = 'Average of Energy Loss during of Years'
            )

    return fig

def area_plot_Power_Loss(data):
    fig = px.area(data,
        x = "Date",
        y = "tapPowerLossAmp",
    )
    fig.update_xaxes(title_text = 'Date in Year')
    fig.update_yaxes(title_text = 'Power Loss Average Amplitude (kw)')
    fig.update_layout(
            title = 'Average of Power Loss during of Years'
            )
    return fig
    
