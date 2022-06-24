import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff



df = pd.read_csv('OLTCresults.csv')

def Histogram(df):
    fig = px.histogram(df, x="Date", y="tapCircCurrAmp", title="Circulating Current Amplitude") 
    fig.update_layout(
    xaxis_title="Date(Year)",
    yaxis_title="Circulating Current Amplitude(KA)",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)
