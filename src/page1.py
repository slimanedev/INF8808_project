import pathlib, dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import preprocess,  viz6_dumbbell_chart, viz9_line_chart, viz8_bar_chart

# Define Path to get the datas
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))

# Preprocess the data
oltc_data = preprocess.convert_dates(oltc_data)
oltc_data = preprocess.drop_irrelevant_time(oltc_data)
wd_data = preprocess.get_traf_wd_data(oltc_data)
we_data= preprocess.get_traf_we_data(oltc_data)

# Get the figures for Viz 9
fig91 = viz9_line_chart.get_transformer_avg_current_plot(wd_data,we_data, 2015)
fig91.update_layout(height = 600, width = 1000)
fig91.update_layout(dragmode = False)

fig92 = viz9_line_chart.get_transformer_max_current_plot(wd_data,we_data, 2015)
fig92.update_layout(height = 600, width = 1000)
fig92.update_layout(dragmode = False)

# Get the figure for Viz 6
fig6 = viz6_dumbbell_chart.dumbbell_plot(oltc_data,2015, 5)
years = (oltc_data['Date'].dt.strftime('%Y')).unique()

# Get the figure for Viz 8
fig8 = viz8_bar_chart.get_monthly_current_plot(oltc_data)

# The page 1 layout
layout = html.Div(children=[
        html.Div([
            html.H3('Transformer load current for different years'),
            
            #Display the visualization 9.1
            dcc.Graph(id = 'linegraph',
                figure = fig91),
            html.H6('Use slider below to change the year'),
            dcc.Slider(
                        2015,
                        2020,
                        step = None,
                        id = 'sliderYear1',
                        value = 2020,
                        marks = {str(year): str(year) for year in [2015,2016,2017,2018,2019,2020]},),
            
            #Display the visualization 9.2
            dcc.Graph(id = 'bargraph',
                figure = fig92),
            html.H6('Use slider below to change the year'),
            dcc.Slider(
                        2015,
                        2020,
                        step = None,
                        id = 'sliderYear2',
                        value = 2020,
                        marks = {str(year): str(year) for year in [2015,2016,2017,2018,2019,2020]},),
            
            #Display the visualization 6
            html.H3('Difference between Tap Power Loss Time and Tap Operation Time'),
            html.Label('Select the year:'),
            dcc.Dropdown(
                        id = 'years',
                        options = [{
                                'label' : i, 
                                'value' : i
                        } for i in years],
                        value = '2015',
                        clearable = True),
            html.Label('Select the month:'),
            dcc.Dropdown(
                        id = 'months',
                        options = [],
                        value = '5',
                        clearable = True),
            dcc.Graph(id = 'fig-six',
                figure = fig6),

            #Display the visualization 8
            html.H3('Variation of average tap circulating current over time'),
            dcc.Graph(figure = fig8),
            
        ]),
],style={'padding': 10, 'flex': 1})


#Callbacks for Viz 9
@dash.callback(
    Output('linegraph', 'figure'),
    [Input('sliderYear1', 'value')])

def update_viz91_viz92(value):
    wd_data = preprocess.get_traf_wd_data(oltc_data)
    we_data = preprocess.get_traf_we_data(oltc_data)
    fig91 = viz9_line_chart.get_transformer_avg_current_plot(wd_data,we_data, value)
    
    return fig91  

@dash.callback(
    Output('bargraph', 'figure'),
    [Input('sliderYear2', 'value')])

def update_viz92(value):
    wd_data = preprocess.get_traf_wd_data(oltc_data)
    we_data = preprocess.get_traf_we_data(oltc_data)
    fig92 = viz9_line_chart.get_transformer_max_current_plot(wd_data,we_data, value)
    return fig92    


#Callbacks for Viz 6
@dash.callback(
    Output('months', 'options'),
    [Input('years', 'value')]
)
def set_month_options(year):
    d_year = oltc_data[(oltc_data['Date'].dt.strftime('%Y') == year)]
    return [{'label': i, 'value': i} for i in (d_year['Date'].dt.strftime('%m')).unique()]

@dash.callback(
    Output('fig-six', 'figure'),
    [Input('years', 'value'),
    Input('months', 'value')]
)
def update_viz6(year, month):
    if (year == None) or (month == None):
        return dash.no_update
    else:
        fig6 = viz6_dumbbell_chart.dumbbell_plot(oltc_data,year, month)
    return fig6        
