import dash, pathlib, preprocess
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import tap_history_dashboard, preprocess

# Define Path to get the datas
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))
total_power_loss=round(sum(oltc_data['tapPowerLossAmp']),2)
total_circulating_current=round(sum(oltc_data['tapCircCurrAmp']),2)
total_energy_loss=round(sum(oltc_data['tapEnergyLoss']),2)
total_tap_change_time=round(sum(oltc_data['tapOperationTime']),2)

# Preprocess the data
oltc_data = preprocess.convert_dates(oltc_data)
oltc_data = preprocess.drop_irrelevant_time(oltc_data)

#Get the main figure
fig=go.Figure(go.Bar(x=oltc_data['tapBefore'], y=oltc_data['tapPowerLossAmp']))
fig.update_traces(marker_color='blue', marker_line_color='blue',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title= 'Power Loss Average per Tap (kw)',
                    xaxis_title='Taps',)

# Get tap recent history plot
fig1 = tap_history_dashboard.scatter_recent_history_tap(oltc_data, selected_range = 0)

#The layout of the dashboard
layout = html.Div(className='content', children=[
        html.Header(children=[html.H1('Recent Tap KPIs',style={'textAlign':'center'}),],style={'padding':0}),
        
        html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
        
        html.Div(children=[html.Label('Use slider below to change the duration'),
                 #style={'color': '#68228B', 'fontSize': 16}),
                dcc.Slider(0,3,step=None,id='slider-duration',value=0,marks={0: {'label': 'Past Week'},1: {'label': 'Past Two Weeks'},2: {'label': 'Past Three Weeks'},3: {'label': 'Past Month'}})]),
        
        html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
        
        html.Div(className='content', children=[
                html.Div(children=[
                        html.H4('Total Power Loss (kw)',style={'textAlign':'center'}),
                        html.H4(total_power_loss,style={'textAlign':'center','padding': 10,'color': 'blue'}),
                        html.Br(),
                        
                        html.H4('Total Circulating Current Amplitude (kA)',style={'textAlign':'center'}),
                        html.H4(total_circulating_current,style={'textAlign':'center','padding': 10,'color': 'blue'}),
                        html.Br(),
                ], style={'padding': 10, 'flex': 1}),

                html.Div(children=[
                        html.H4('Total Energy Loss Quantity (kj)',style={'textAlign':'center'}),
                        html.H4(total_energy_loss,style={'textAlign':'center','padding': 10,'color': 'blue'}),
                        html.Br(),

                        html.H4('Total Tap Change Operation Time (s)',style={'textAlign':'center'}),
                        html.H4(total_tap_change_time,style={'textAlign':'center','padding': 10,'color': 'blue'}),
                        html.Br(),
                        ], style={'padding': 10, 'flex': 1})
        ],style={'display': 'flex', 'flex-direction': 'row','padding':20}),

        html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),

        html.Div(children=[html.Div([#html.H3('Recent history of tap used', 
                                                          #style={'color': '#68228B', 'fontSize': 32,'textAlign': 'center'}),
                                                dcc.Graph(id='tap-frequency',figure=fig1),],)],style={'padding':20}),
        
        html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),

        html.Div(className='viz-container', children=[dcc.Graph(id='bargraph',figure=fig,),]),

],style={'padding':5})


@dash.callback(
    Output('tap-frequency', 'figure'),
    [Input('slider-duration', 'value')])
def update_viz(value):
    fig1 = tap_history_dashboard.scatter_recent_history_tap(oltc_data, selected_range = value)
    return fig1 
