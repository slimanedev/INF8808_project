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

    return fig

def area_plot_Power_Loss(data):

    # Plot for area chart viz 7.2
    fig = px.area(data,
        x = "Date",
        y = "tapPowerLossAmp",
        color = 'year',
    )

    # Update axes 
    fig.update_yaxes(range = [0, 1],
        tick0 = 0,
        dtick = 0.1,
        title_text = 'Power Loss',
    )

    fig.update_xaxes(title_text = 'Date in Year')

    return fig
    