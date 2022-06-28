import pandas as pd
import preprocess
import plotly.express as px


def area_plot_Energy_Loss(data):
    fig = px.area(data,
        x = "Date",
        y = "tapEnergyLoss",
    )

    fig.update_xaxes(title_text = 'Date in Year')
    fig.update_yaxes(range = [0, .026], title_text = 'Energy Loss')
    return fig

def area_plot_Power_Loss(data):
    fig = px.area(data,
        x = "Date",
        y = "tapPowerLossAmp",
    )
    fig.update_xaxes(title_text = 'Date in Year')
    fig.update_yaxes(range = [0, 1], title_text = 'Power Loss Average Amplitude (kw)')
    return fig
    
