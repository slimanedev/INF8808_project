import pandas as pd
import preprocess
import plotly.express as px
import datetime as datetime

def plot_line_chart(data):

    # data['Date'] = pd.to_datetime(data['Date'])
    # data = data.loc[(data['Date'] >= ('%d-01-01' % 2020))& (data['Date'] <= ('%d-12-31' % 2020))]
    data['Time']= data['Time'].apply(lambda x:datetime.datetime.strptime(x, "%I:%M:%S %p")).hour

    fig = px.line(data,
        x = 'Time',
        y = "tapBefore",
        # color = "Date"
        line_shape='vh'
        )
    fig.update_layout(title="Line-plot for the tap switching paterns",
        xaxis_title= "Day time",
        yaxis_title= 'Tap number'
    )

    return fig