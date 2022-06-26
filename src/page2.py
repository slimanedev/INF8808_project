import pathlib, dash
import preprocess, viz1_line_chart, viz2_bar_chart, viz4_box_chart, viz8_bar_chart 
import dash_html_components as html
import dash_bootstrap_components as dbc
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
#Use the preprocess to manage the data. You can add fucntions if it's necessary

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# Get the data
oltc_data = pd.read_csv(DATA_PATH.joinpath("OLTCresults.csv"))

#idx=oltc_data[(oltc_data['Time'].str.contains('AM|PM'))].index
#data=oltc_data.iloc[idx,:]
data=preprocess.drop_irrelevant_time(oltc_data)

# Plot for Line_chart (not finished)
#fig_viz1 = viz1_line_chart.plot_line_chart(data)

# Plot bar chart for viz 2
fig_viz2 = viz2_bar_chart.BarChart(data)
fig_viz2.update_layout(height=600, width=1000)
fig_viz2.update_layout(dragmode=False)

# Plot for box chart for viz 4
fig_viz4=viz4_box_chart.plot_box_chart(data)
fig_viz4.update_layout(height=600, width=1000)
fig_viz4.update_layout(dragmode=False)

# Plot for Barchart
data2=preprocess.get_monthly_average_current(data)
fig_viz8=viz8_bar_chart.get_monthly_current_plot(data2)

layout = html.Div([
            html.H1(' Variation of circulating current amplitude over time',
                    style={'textAlign':'center'}),
            dcc.Graph(id='boxplot',
                    figure= fig_viz8
                )
        ]
)

layout = html.Div(children=[
            html.Div([
                # html.H3('Visualizations on the performance of Tap changer',
                # style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                    figure= fig_viz2
                )
            ]
        ),
        html.Div([
                dcc.Graph(id='boxplot',
                        figure=fig_viz4
                )
            ]
        )
])
