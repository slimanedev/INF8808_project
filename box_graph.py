import pandas as pd
import preprocess
import plotly.express as px
import plotly.graph_objects as go


'''# Get the data (temporary solution until data are processed)
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

plot_box_chart(oltc_data['tapAfter'], oltc_data['tapOperationTime'])''' # temporary until data are processed. 
                                                                     # function call will be done in app.py file


def plot_box_chart(data):
    
    data['Date']=pd.to_datetime(data['Date'])
    #idx=data['Date'].dt.year == year
    #df=data[idx]

    fig = px.box(data, 
        x = 'tapBefore', 
        y = "tapOperationTime",
        color='tapBefore',
        #category_orders={'tapBefore': ["4", "5", "6", "7", "8", "9", "10", "11"]}
        labels={'tapBefore': 'Tap position'}
        )
    global_average=data['tapOperationTime'].mean().round(3)  #Average commutation time for all the tap positions
    
    fig.add_hline(y=global_average, line_dash="dot",
              annotation_text="All-time average tap operation time", 
              annotation_position="top right",
              annotation_font_size=15,
              annotation_font_color="black"
             )
    
    fig.update_layout(
        title="Box-plot for the tap operation time based on the tap position",
        xaxis_title= "Tap position",
        yaxis_title= 'Tap operation time (ms)'
    )
        
    return fig



