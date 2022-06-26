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

colors = {
    'background': '#000000',
    'text': '#111111'
}

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))
total_power_loss=round(sum(oltc_data['tapPowerLossAmp']),2)
total_circulating_current=round(sum(oltc_data['tapCircCurrAmp']),2)
total_energy_loss=round(sum(oltc_data['tapEnergyLoss']),2)
total_tap_change_time=round(sum(oltc_data['tapOperationTime']),2)

fig=go.Figure()

fig = fig.add_trace(go.Bar(x=oltc_data['tapBefore'], y=oltc_data['tapPowerLossAmp'],
                        marker_color= "blue"))

#fig=px.bar(oltc_data, barmode='group', x='tapBefore',
                #y=['tapPowerLossAmp'],
                #title="Power Loss average per tap (Kw)",
                #labels={'value':'Power(Kw)','tapBefore':'Taps'},

                #)
#fig.update_traces(marker_color='blue')

#fig.update_layout(
#    plot_bgcolor=colors['background'],
 #   paper_bgcolor=colors['background'],
 #   font_color=colors['text']
#)



layout = html.Div(className='content', children=[
        html.Header(children=[
                html.H1('Tap changer performance',style={'textAlign':'center'}),]),

        html.Div(className='viz-container', children=[
                dcc.Graph(id='bargraph',figure=fig,),
        ],style={'padding': 10, 'flex': 1}),

        html.Div(className='content', children=[
                html.Div(children=[
                        html.H4('Total Power Loss (kw)',style={'textAlign':'center'}),
                        html.H4(total_power_loss,style={'textAlign':'center','padding': 10,'textColor':'blue'}),
                        html.Br(),
                        
                        html.H4('Total Circulating Current Amplitude (kA)',style={'textAlign':'center'}),
                        html.H4(total_circulating_current,style={'textAlign':'center','padding': 10}),
                        html.Br(),
                ], style={'padding': 10, 'flex': 1}),

                html.Div(children=[
                        html.H4('Total Energy Loss Quantity (kj)',style={'textAlign':'center'}),
                        html.H4(total_energy_loss,style={'textAlign':'center','padding': 10}),
                        html.Br(),

                        html.H4('Total Tap Change Operation Time (s)',style={'textAlign':'center'}),
                        html.H4(total_tap_change_time,style={'textAlign':'center','padding': 10}),
                        html.Br(),
                        ], style={'padding': 10, 'flex': 1})
        ],style={'display': 'flex', 'flex-direction': 'row'})
])