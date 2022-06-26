import plotly.express as px
import pandas as pd
import collections


def BarChart(df):
        tapAfter=df['tapAfter'].tolist()
        counter=collections.Counter(tapAfter)
        Number=counter.values()
        df2=pd.DataFrame(counter.items() ,columns=['Tap position', 'Number of Change'])

        fig = px.bar(df2,x='Number of Change',y='Tap position', orientation='h') 

        fig.update_layout(
        title="The number of tap changes of each tap position")
        return fig



