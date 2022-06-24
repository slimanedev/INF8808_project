import dash
import preprocess, box_graph, line_graph, current_variation
import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

#Use the preprocess to manage the data. You can add fucntions if it's necessary

with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)
#Use the preprocess to manage the data. You can add fucntions if it's necessary

idx=oltc_data[(oltc_data['Time'].str.contains('AM|PM'))].index
data=oltc_data.iloc[idx,:]

# Plot for box chart
fig=box_graph.plot_box_chart(data)
fig.update_layout(height=600, width=1000)
fig.update_layout(dragmode=False)

# Plot for Line_chart (not finished)
fig2 = line_graph.plot_line_chart(data)

layout = html.Div([
            html.H1('Visualizations on the performance of Tap changer',
                    style={'textAlign':'center'}),
            dcc.Graph(id='boxplot',
                    figure= fig2
                )
        ]
)

# Plot for histogram
fig8_1=current_variation.plot_current_variation(data)

layout = html.Div([
            html.H1('Circulating Current Amplitude',
                    style={'textAlign':'center'}),
            dcc.Graph(id='boxplot',
                    figure= fig8_1
                )
        ]
)
