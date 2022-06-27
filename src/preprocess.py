'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
import datetime as datetime
import numpy as np

def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    # Convert the value of 'Date' in the dataframe to datetime objects
    dataframe['Date'] = pd.to_datetime(dataframe['Date'])
    return dataframe

def filter_by_year_month(dataframe, year, month):
    '''
        Filters the elements of the dataframe by selected year and selected month, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            year: The selected year by user
            month: The selected month by user
        Returns:
            The dataframe filtered by the desired year and month.
    '''
    # TODO : Filter by selected year and selected month
    
    df_year = dataframe.loc[dataframe['Date'].dt.year == int(year)]
    df_year_month = df_year.loc[df_year['Date'].dt.month == int(month)]
    return df_year_month
  
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


def adjust_data_for_viz7(oltc_data):
    oltc_data = drop_irrelevant_time(oltc_data)
    oltc_data['Date'] = pd.to_datetime(oltc_data['Date'])

    oltc_data.sort_values(by='Date')

    df=oltc_data.groupby(pd.PeriodIndex(oltc_data['Date'], freq='M')).agg({'tapPowerLossAmp': (np.mean),
                                                                           'Date':'first','tapEnergyLoss': (np.mean)})
    df['year'] = pd.DatetimeIndex(df['Date']).year
    df.head()
    return df
