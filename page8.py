import plotly.express as px
import pandas as pd


df = pd.read_csv('OLTCresults.csv')


def histogram_viz8(df):
    fig = px.histogram(df, x="Date", y="tapCircCurrAmp", title="Circulating Current Amplitude") 
    fig.update_layout(

        yaxis_title="Circulating Current Amplitude (kA)",
        yaxis = dict( tickfont = dict(size=20),title_font_size=20,range=[0, 1.6]),
        xaxis = dict( tickfont = dict(size=20),title_font_size=20)


        )


    return fig

