import pathlib, dash
import preprocess, viz1_line_chart, viz2_bar_chart, viz4_box_chart, viz7_area_chart
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# Define Path to get the datas
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))

# Plot line chart - Viz 1
data=preprocess.drop_irrelevant_time(oltc_data)
fig_viz1 = viz1_line_chart.plot_line_chart(data)

# Plot bar chart for viz 2
fig_viz2 = viz2_bar_chart.BarChart(data)
fig_viz2.update_layout(height=600, width=1000)
fig_viz2.update_layout(dragmode=False)

# Plot for box chart - Viz 3
#fig_viz3=viz3_bar_chart.plot_box_chart(data)

# Plot for box chart - Viz 4
fig_viz4=viz4_box_chart.plot_box_chart(data)
fig_viz4.update_layout(height=600, width=1000)
fig_viz4.update_layout(dragmode=False)

# Plot for area chart - Viz 7
df=preprocess.adjust_data_for_viz7(oltc_data)
fig_viz7=viz7_area_chart.area_plot_Energy_Loss(df)


# The page 2 layout
layout =html.Div(children=[
        html.Div([
            #Display the visualization 1
            #html.H3('Transformer load current for different years'),
            dcc.Graph(figure=fig_viz1),
            
            #Display the visualization 2
            #html.H6('Select the year from on the slider below:'),
            dcc.Graph(figure=fig_viz2),
            
            #Display the visualization 3
            #html.H3('Difference between Tap Power Loss Time and Tap Operation Time'),
            #dcc.Graph(figure=fig_viz3),

            #Display the visualization 4
            #html.H3('Variation of average tap circulating current over time'),
            dcc.Graph(figure=fig_viz4),

            #Display the visualization 7
            #html.H3('Variation of average tap circulating current over time'),
            dcc.Graph(figure=fig_viz7),
            
        ]),
],style={'padding': 10, 'flex': 1})
