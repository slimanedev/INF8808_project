import pathlib, dash
import preprocess, box_graph, line_graph, current_variation, bar_chart_viz2
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

# Plot for box chart
fig1=box_graph.plot_box_chart(data)
fig1.update_layout(height=600, width=1000)
fig1.update_layout(dragmode=False)

# Plot for Line_chart (not finished)
#fig2 = line_graph.plot_line_chart(data)

fig2= bar_chart_viz2.BarChart(data)
fig2.update_layout(height=600, width=1000)
fig2.update_layout(dragmode=False)
layout = html.Div([
            html.H3('Visualizations on the performance of Tap changer',
                    style={'textAlign':'center'}),
            dcc.Graph(id='boxplot',
                    figure= fig1
                ),

            dcc.Graph(id='boxplot',
                    figure= fig2
                )
        ]
)

# Plot for histogram
'''fig8_1=current_variation.get_monthly_current_plot(data)

layout = html.Div([
            html.H1(' Variation of circulating current amplitude over time',
                    style={'textAlign':'center'}),
            dcc.Graph(id='boxplot',
                    figure= fig8_1
                )
        ]
)'''
# Plot bar chart tracking number of tap changes
fig2_1= bar_chart_viz2.BarChart(data)
layout = html.Div([
            html.H1('Change of Tap',
                    style={'textAlign':'center'}),
            dcc.Graph(id='boxplot',
                    figure= fig2_1
                )
        ]
)

