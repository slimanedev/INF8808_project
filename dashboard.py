import dash
import preprocess
import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

#Use the preprocess to manage the data. You can add fucntions if it's necessary

df = pd.read_csv('./OLTCresults.csv')

print(df.head(5))


fig=px.bar(df, barmode='group', x='tapBefore',
                y=['tapPowerLossAmp'],
                title="Power Loss average per tap (Kw)",
                labels={'value':'Power(Kw)','tapBefore':'Taps'},

                )
fig.update_traces(marker_color='blue')


layout = html.Div([
            html.H1('Tap changer performance',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=fig,
                    )
                ]
)

