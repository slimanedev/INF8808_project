
import dash
import preprocess
import dash_html_components as html
#import dash_core_components as dcc
from dash import Dash, dcc, html, Input, Output
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import preprocess
import Load_current


app = Dash(__name__)

with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)
#Use the preprocess to manage the data. You can add fucntions if it's necessary

idx=oltc_data[(oltc_data['Time'].str.contains('AM|PM'))].index
data=oltc_data.iloc[idx,:]

wd_data = preprocess.get_traf_wd_data(data)
we_data= preprocess.get_traf_we_data(data)

fig1=Load_current.get_transformer_avg_current_plot(wd_data,we_data, 2015)
fig1.update_layout(height=600, width=1000)
fig1.update_layout(dragmode=False)

fig2=Load_current.get_transformer_max_current_plot(wd_data,we_data, 2015)
fig2.update_layout(height=600, width=1000)
fig2.update_layout(dragmode=False)


layout =html.Div(children=[
        html.Div([
            html.H3('Transformer load current for different years'),
            
            html.H6('Select the year from the dropdown below:'),
            dcc.Dropdown(
                [2015,2016,2017,2018,2019,2020],
                2015,
                id='year'
            ),
            dcc.Graph(id='linegraph',
                      figure=fig1
                )
            ]
        ),
        html.Div([
                #html.H3('Transformer Maximum Load current over hours of the day'),
                dcc.Graph(id='bargraph',
                      figure=fig2
                )
            ]
        )
])

@app.callback([
    Output('linegraph', 'figure'),
    Output('bargraph', 'figure')],
    [Input('year', 'value')])
def update_graph(year):
     wd_data = preprocess.get_traf_wd_data(data)
     we_data= preprocess.get_traf_we_data(data)
     fig1=Load_current.get_transformer_avg_current_plot(wd_data,we_data, year)
     fig2=Load_current.get_transformer_max_current_plot(wd_data,we_data, year)
     return fig1,fig2  


if __name__ == '__main__':
    app.run_server(debug=True)
    
'''layout = html.Div([
            html.H1('Lifespan data',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=px.bar(df, barmode='group', x='Years',
                    y=['Attribut1', 'Attribut2']))
                ]
    )
'''
