import plotly.express as px
import pandas as pd
import collections


def BarChart(df):
        tapAfter=df['tapAfter'].tolist()
        tapBefore=df['tapBefore'].tolist()
        counter=collections.Counter(tapAfter)
        Number=counter.values()
        df2=pd.DataFrame(counter.items() ,columns=['Numbert Of Tap', 'Number of Change'])

        fig = px.bar(df2,x='Numbert Of Tap',y='Number of Change') 

        return fig



