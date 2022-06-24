import plotly.express as px
import pandas as pd


def plot_current_variation(df):
    fig = px.histogram(df, x="Date", y="tapCircCurrAmp") 
    fig.update_layout(

        yaxis_title="Current Amplitude (kA)",
        yaxis = dict( tickfont = dict(size=20),title_font_size=20,range=[0, 1.6]),
        xaxis = dict( tickfont = dict(size=20),title_font_size=20)


        )


    return fig

