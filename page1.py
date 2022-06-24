
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

    
fig6 = viz_six.dumbbell_plot(oltc_data,2015, 5)
oltc_data['Date'] = pd.to_datetime(oltc_data['Date'])
years = (oltc_data['Date'].dt.strftime('%Y')).unique()

layout = html.Div([
    html.Div([
        html.Div([

            html.Label('year'),
            dcc.Dropdown(
                 id = 'years',
                 options = [{
                         'label' : i, 
                         'value' : i
                 } for i in years],
                value = '2015',
                clearable = True

                 ),
                ]),

        html.Div([

            html.Label('month'),
            dcc.Dropdown(
             id = 'months',
             options = [],
             value = '5', 
             clearable = True)
             ,
        ]),
            ]),

    dcc.Graph(id = 'fig-six', figure=fig6)
    ])


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
        fig6 = viz_six.dumbbell_plot(oltc_data,year, month)

    return fig6
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
