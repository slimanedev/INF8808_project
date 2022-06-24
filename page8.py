import plotly.express as px
import pandas as pd


df = pd.read_csv('OLTCresults.csv')


def histogram_viz8(df):
    fig = px.histogram(df, x="Date", y="tapCircCurrAmp", title="Circulating Current Amplitude") 
    fig.update_layout(
    yaxis_title="Circulating Current Amplitude(KA)",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)
    return fig

