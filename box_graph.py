import pandas as pd
import preprocess
import plotly.express as px


# Get the data (temporary solution until data are processed)
with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)

data_time = oltc_data['tapOperationTime']

def plot_box_chart(tap_nbr, tap_operation_time):
    fig = px.box(tap_operation_time, 
        x = tap_nbr, 
        y = tap_operation_time,
        labels = {'Tap number', 'Time - [sec]'},
        range_x=[0,19],
        )
    return fig

plot_box_chart(oltc_data['tapAfter'], oltc_data['tapOperationTime']) # temporary until data are processed. 
                                                                     # function call will be done in app.py file




