import pathlib, dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import preprocess,  viz6_dumbbell_chart, viz9_line_chart

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))

#Preprocess the data
oltc_data = preprocess.convert_dates(oltc_data)
oltc_data = preprocess.drop_irrelevant_time(oltc_data)
wd_data = preprocess.get_traf_wd_data(oltc_data)
we_data= preprocess.get_traf_we_data(oltc_data)

# Initiate the app 
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Declare server for Heroku deployment
server = app.server

# Get the figures
fig1=viz9_line_chart.get_transformer_avg_current_plot(wd_data,we_data, 2015)
fig1.update_layout(height=600, width=1000)
fig1.update_layout(dragmode=False)

fig2=viz9_line_chart.get_transformer_max_current_plot(wd_data,we_data, 2015)
fig2.update_layout(height=600, width=1000)
fig2.update_layout(dragmode=False)


# The page 1 layout
layout =html.Div(children=[
        html.Div([
            html.H3('Transformer load current for different years'),
            html.H6('Select the year from the dropdown below:'),

            #Display the visualization 9.1
            dcc.Dropdown(id='dropdownYear',options=[2015,2016,2017,2018,2019,2020],value=2015),
            dcc.Graph(id='linegraph',figure=fig1),
            
            #Display the visualization 9.2
            dcc.Slider(
                        2015,
                        2020,
                        step=None,
                        id='year--slider',
                        value=2020,
                        marks={str(year): str(year) for year in [2015,2016,2017,2018,2019,2020]},),
            dcc.Graph(id='bargraph',figure=fig2),
            ]
        ),
])

"""@app.callback([
    Output('linegraph', 'figure'),
    Output('bargraph', 'figure')],
    [Input('year--slider', 'value')],
    [State('linegraph', 'figure'),
    State('bargraph', 'figure')])"""

@dash.callback(
    Output('linegraph', 'figure'),
    [Input('dropdownYear', 'value')])

def update_graph(value):
    print(value)
    wd_data = preprocess.get_traf_wd_data(oltc_data)
    we_data= preprocess.get_traf_we_data(oltc_data)
    fig1=viz9_line_chart.get_transformer_avg_current_plot(wd_data,we_data, value)
    #fig2=viz9_line_chart.get_transformer_max_current_plot(wd_data,we_data, year)
    return fig1  

    

"""    
fig6 = viz6_dumbbell_chart.dumbbell_plot(oltc_data,2015, 5)
years = (oltc_data['Date'].dt.strftime('%Y')).unique()


#layout = html.Div(children=[
#    html.H3('Difference between Tap Power Loss Time and Tap Operation Time'),
#    html.Div([
#        html.Div([
#            html.Label('Select the year:'),
#            dcc.Dropdown(
#                 id = 'years',
#                 options = [{
#                         'label' : i, 
#                         'value' : i
#                 } for i in years],
#                value = '2015',
#                clearable = True),], style=dict(width='50%')),
#        html.Div([
#            html.Label('Select the month:'),
#            dcc.Dropdown(
#            id = 'months',
#            options = [],
#            value = '5',
#            clearable = True)], 
#            style=dict(width='50%'))], style=dict(display='flex')),
#    dcc.Graph(id = 'fig-six', figure=fig6),
#])


@app.callback(
    Output('months', 'options'),
    Input('years', 'value')
)
def set_month_options(year):
    d_year = oltc_data[(oltc_data['Date'].dt.strftime('%Y') == year)]
    return [{'label': i, 'value': i} for i in (d_year['Date'].dt.strftime('%m')).unique()]

@app.callback(
    Output('fig-six', 'figure'),
    Input('years', 'value'),
    Input('months', 'value')
)
def update_graph(year, month):

    if (year == None) or (month == None):
        return dash.no_update
    else:
        fig6 = viz6_dumbbell_chart.dumbbell_plot(oltc_data,year, month)

    return fig6        
"""     
'''layout = html.Div([
            html.H1('Lifespan data',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=px.bar(df, barmode='group', x='Years',
                    y=['Attribut1', 'Attribut2']))
                ]
    )
'''
