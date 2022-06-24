'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import datetime as datetime

"""with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)"""
  
def get_traf_wd_data(data):
       
    df=data.copy()
    df['Date']=pd.to_datetime(df['Date'])
    idx=df['Date'].dt.weekday < 5  # sunday=6, saturday=5; for weekends
    wd_data=df.loc[idx, ['Date', 'Time', 'TrafoLoadCurr']] #data for weekdays
    wd_data['Time']= wd_data['Time'].apply(lambda x:datetime.datetime.strptime(x, "%I:%M:%S %p").hour)

    return wd_data

def get_traf_we_data(data):
       
    df=data.copy()
    df['Date']=pd.to_datetime(df['Date'])
    idx=df['Date'].dt.weekday > 4  # sunday=6, saturday=5; for weekends
    we_data=df.loc[idx, ['Date', 'Time', 'TrafoLoadCurr']]  #data for weekends
    we_data['Time']= we_data['Time'].apply(lambda x:datetime.datetime.strptime(x, "%I:%M:%S %p").hour)

    return we_data

def drop_irrelevant_time(data):
    idx = data[(data['Time'].str.contains('AM|PM'))].index
    new_data = data.iloc[idx,:]
    
    return new_data

def get_monthly_average_current (df):

    df1=df[['Date', 'Time', 'TrafoLoadCurr', 'tapCircCurrAmp']]
    df1['year']=df1['Date'].dt.year
    df1['month']=df1['Date'].dt.month_name()

    df2=df1.groupby(['year', 'month'], as_index=False).agg({'tapCircCurrAmp': 'mean'})
    df2=df2.sort_values(['year', 'month'])
    df2.reset_index(drop=True)
    
    return df2


