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
    df_year = dataframe.loc[dataframe['Date'].dt.year == int(year)]
    df_year_month = df_year.loc[df_year['Date'].dt.month == int(month)]
    return df_year_month
  
def get_traf_wd_data(data):
       
    df = data.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    idx = df['Date'].dt.weekday < 5                             # Monday to Friday = 0 to 4
    wd_data = df.loc[idx, ['Date', 'Time', 'TrafoLoadCurr']]    # Saturday = 5 && Sunday = 6
    wd_data['Time'] = wd_data['Time'].apply(lambda x:datetime.datetime.strptime(x, "%I:%M:%S %p").hour)

    return wd_data

def get_traf_we_data(data):
       
    df = data.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    idx = df['Date'].dt.weekday > 4                             # Monday to Friday = 0 to 4
    we_data = df.loc[idx, ['Date', 'Time', 'TrafoLoadCurr']]    # Saturday = 5 && Sunday = 6
    we_data['Time'] = we_data['Time'].apply(lambda x:datetime.datetime.strptime(x, "%I:%M:%S %p").hour)

    return we_data

def drop_irrelevant_time(data):
    idx = data[(data['Time'].str.contains('AM|PM'))].index
    new_data = data.iloc[idx,:]
    
    return new_data

def get_monthly_average_current (df):

    df1 = df[['Date', 'Time', 'TrafoLoadCurr', 'tapCircCurrAmp']]
    df1['year'] = df1['Date'].dt.year
    df1['month'] = df1['Date'].dt.month_name()

    df2 = df1.groupby(['year', 'month'], as_index=False).agg({'tapCircCurrAmp': 'mean'})
    df2 = df2.sort_values(['year', 'month'])
    df2.reset_index(drop=True)
    
    return df2


def adjust_data_for_viz7(oltc_data):
    oltc_data = drop_irrelevant_time(oltc_data)
    oltc_data['Date'] = pd.to_datetime(oltc_data['Date'])

    oltc_data.sort_values(by='Date')

    df = oltc_data.groupby(pd.PeriodIndex(oltc_data['Date'], freq='M')).agg({'tapPowerLossAmp': (np.mean),
                                                                           'Date':'first','tapEnergyLoss': (np.mean)})
    df['year'] = pd.DatetimeIndex(df['Date']).year
    df.head()
    return df


def  adjust_data_for_viz3(oltc_data):
    
    tap = 'tapAfter'
    # Change the time format
    oltc_data['Time'] = oltc_data['Time'].apply(lambda x:datetime.datetime.strptime(x, "%I:%M:%S %p").hour)

    Time_sorted_data = oltc_data.sort_values('Time')
    h = Time_sorted_data['Time']

    # Select the suitable data and create new dataframe
    output_tap = []
    ind0 = 0
    for i in range(24):
        for j in range(np.min(Time_sorted_data[tap]),np.max(Time_sorted_data[tap]+1)):
            ind = np.where(h==i)[0][-1]
            ind1 = np.where(Time_sorted_data[tap][ind0:ind]==j)
            output_tap.append([i,j,np.max(Time_sorted_data['TrafoLoadCurr'][ind1[0]]),
                                 np.max(Time_sorted_data['tapPowerLossAmp'][ind1[0]]),
                                 np.max(Time_sorted_data['tapEnergyLoss'][ind1[0]]),
                                 np.max(Time_sorted_data['tapCircCurrAmp'][ind1[0]])])
        ind0 = ind

    y = np.array(output_tap)
    data = {'Time_in_Hours': y[:,0],
                'Tap Value' : y[:,1],
                'Max_loadCurr': y[:,2],
                'Max_PowerLoss': y[:,3],
                'Max_EnergyLoss': y[:,4],
                'Max_CircCurr': y[:,5]}
    
    df1 = pd.DataFrame(data)

    # Create the exact time
    lst = list(np.int32(df1['Time_in_Hours']))
    df1['Time_in_Hours'] = [datetime.time(hour=x).strftime("%H:%M") for x in lst]
    
    return df1
