import plotly.express as px
import pandas as pd
import collections



df = pd.read_csv('OLTCresults.csv')

def BarChart(df)
        tapAfter=df['tapAfter'].tolist()
        tapBefore=df['tapBefore'].tolist()
        counter=collections.Counter(tapAfter)
        Number=counter.values()
        df2=pd.DataFrame(counter.items() ,columns=['Numbert Of Tap', 'Number of Change per Year'])

        fig = px.bar(df2,x='Numbert Of Tap',y='Number of Change per Year') 

        return fig



