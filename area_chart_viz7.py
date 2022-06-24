import pandas as pd
import preprocess
import plotly.express as px
import datetime as dt
import numpy as np

# Get the data (temporary solution until data are processed)
with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)
   
oltc_data = preprocess.drop_irrelevant_time(oltc_data)
oltc_data['Date'] = pd.to_datetime(oltc_data['Date'])

oltc_data.sort_values(by='Date')

df=oltc_data.groupby(pd.PeriodIndex(oltc_data['Date'], freq='M')).agg({'tapPowerLossAmp': (np.mean),
                                                                       'Date':'first','tapEnergyLoss': (np.mean)})
df['year'] = pd.DatetimeIndex(df['Date']).year
df.head()

def area_plot_Energy_Loss(df):
    fig = px.area(df, x="Date", y="tapEnergyLoss",color = 'year')
    fig.update_yaxes(range=[0, .025],tick0=0, dtick=0.002,title_text='Energy Loss')
    fig.update_xaxes(title_text='Date in Year')
    return fig

def area_plot_Power_Loss(df):
    fig = px.area(df, x="Date", y="tapPowerLossAmp",color = 'year')
    fig.update_yaxes(range=[0, 1],tick0=0, dtick=0.1,title_text='Power Loss')
    fig.update_xaxes(title_text='Date in Year')
    return fig

fig = area_plot_Power_Loss(df)
fig.show()
#df
