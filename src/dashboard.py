import dash, pathlib
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
total_power_loss = round(sum(oltc_data['tapPowerLossAmp']),2)
total_circulating_current = round(sum(oltc_data['tapCircCurrAmp']),2)
total_energy_loss = round(sum(oltc_data['tapEnergyLoss']),2)
total_tap_change_time = round(sum(oltc_data['tapOperationTime']),2)

# Preprocess the data
oltc_data = preprocess.convert_dates(oltc_data)
oltc_data = preprocess.drop_irrelevant_time(oltc_data)

oltc_data2 = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))
oltc_data2 = preprocess.convert_dates(oltc_data2)
oltc_data2 = preprocess.drop_irrelevant_time(oltc_data2)

# Get the main figure
df=oltc_data.groupby('tapBefore', as_index=False).agg({'tapPowerLossAmp': 'mean', 'tapEnergyLoss': 'mean'})

fig = go.Figure(data=[
    go.Bar(name='Average power loss', x=df.tapBefore, y=df.tapPowerLossAmp,hovertemplate = '<b>Tap position: %{x} <br><b>Average power loss: %{y} (KW)<extra></extra>'),
    go.Bar(name='Average energy loss', x=df.tapBefore,y=df.tapEnergyLoss,hovertemplate = '<b>Tap position: %{x} <br><b>Average Energy loss: %{y} (KJ)<extra></extra>')
])
# Change the bar mode
fig.update_layout(title= 'Average power loss and energy loss per each tap position',
                  xaxis_title='Tap position',
                  barmode='stack')


'''fig = go.Figure(go.Bar(x = oltc_data['tapBefore'],
        y = oltc_data['tapPowerLossAmp']
        )
)
fig.update_traces(marker_color = 'blue',
        marker_line_color = 'blue',
        marker_line_width = 1.5,
        opacity = 0.6
)
fig.update_layout(title = 'Power Loss Average per Tap (kw)',
                    xaxis_title = 'Taps')'''

# Get tap recent history plot
fig1 = tap_history_dashboard.scatter_recent_history_tap(oltc_data, selected_range = 'Past Week')

# The layout of the dashboard
layout = html.Div(className='content', children=[
        html.Header(children=[html.H1('Recent Tap KPIs',style={'textAlign':'center'}),],style={'padding':0}),
                
        html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
        
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

        html.Label('Use dropdown below to change the duration'),
        dcc.Dropdown(['Past Week', 'Past Ten Days', 'Past Two Weeks'],'Past Week', id='tap-frequency-dropdown',style={'borderWidth': "0.3vh", "width": "55%", "color": "balck"}),
        
        html.Div(children=[html.Div([dcc.Graph(id='tap-frequency',figure=fig1),],)],style={'padding':20}),
        
        html.Hr(style={'borderWidth': "0.3vh", "width": "75%", "color": "balck",'margin-left': "auto",'margin-right': "auto"}),
        
        html.Div(className='viz-container', children=[dcc.Graph(id='bargraph',figure=fig),]),

],style={'padding':5})



# Callback for tap frequency:
@dash.callback(
    Output('tap-frequency', 'figure'),
    [Input('tap-frequency-dropdown', 'value')])

def update_viz(value):
    fig = tap_history_dashboard.scatter_recent_history_tap(oltc_data, selected_range = value)
    return fig
