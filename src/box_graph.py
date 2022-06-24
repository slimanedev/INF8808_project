import pandas as pd
import preprocess
import plotly.express as px

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
    
    critical_value= 1/(50*2) # Critical value not to reach (half a cycle)

    fig.add_hline(y= critical_value,
        line_dash= 'dash',
        line_color= 'red',
        annotation_text="Critical value not to reach",
        annotation_position="top right",
        annotation_font_size=15,
        annotation_font_color="black",
    )
    
    fig.update_layout(
        title="Box-plot for the tap operation time based on the tap position",
        xaxis_title= "Tap position",
        yaxis_title= 'Tap operation time (second)'
    )
        
    return fig



