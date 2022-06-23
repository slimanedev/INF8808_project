
import dash
import preprocess
import dash_html_components as html
#import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import Load_current

#Use the preprocess to manage the data. You can add fucntions if it's necessary

with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)
 
#I will add the following to the processor file later 
    
data=oltc_data.copy()
data['Date']=pd.to_datetime(data['Date'])
idx=data['Date'].dt.weekday > 4  # sunday=6, saturday=5; for weekends
we_data=data.loc[idx, ['Date', 'Time', 'TrafoLoadCurr']]  #data for weekends
wd_data=data.loc[~idx, ['Date', 'Time', 'TrafoLoadCurr']] #data for weekdays

wd_data['Time']=wd_data['Time'].astype(str)
wd_data['Time']=wd_data['Time'].apply(lambda x: x[:2])
we_data['Time']=we_data['Time'].astype(str)
we_data['Time']=we_data['Time'].apply(lambda x: x[:2])

fig=Load_current.get_transformer_avg_current_plot(wd_data,we_data, 2018)


layout = html.Div([
            html.H1('Transformer Load current over the ours of the day',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=fig
                )
            ]
    )


'''layout = html.Div([
            html.H1('Lifespan data',
                    style={'textAlign':'center'}),
            dcc.Graph(id='bargraph',
                    figure=px.bar(df, barmode='group', x='Years',
                    y=['Attribut1', 'Attribut2']))
                ]
    )
'''
