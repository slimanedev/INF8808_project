import pandas as pd
import preprocess
import plotly.express as px
import datetime as dt


def area_plot_Energy_Loss(df):
    fig = px.area(df, x="Date", y="tapEnergyLoss",color = 'year')
    fig.update_yaxes(range=[0, .025],tick0=0, dtick=0.002,title_text='Energy Loss')
    fig.update_xaxes(title_text='Date in Year')
    return fig

def area_plot_Power_Loss(df):
    fig = px.area(df, x="Date", y="tapPowerLossAmp",color = 'year')
    fig.update_yaxes(range=[0, 1],tick0=0, dtick=0.1,title_text='Power Loss')
    fig.update_xaxes(title_text='Date in Year')
    return fig

