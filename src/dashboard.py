import dash, pathlib, preprocess
import dash_bootstrap_components as dbc
import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))

print(oltc_data.head(5))


fig=px.bar(oltc_data, barmode='group', x='tapBefore',
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

