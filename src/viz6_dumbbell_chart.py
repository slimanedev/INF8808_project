import plotly.graph_objects as go
import preprocess, template
<<<<<<< HEAD
import numpy 
=======
import numpy
>>>>>>> a2e4f581a62f0eed87ad10ac7d2dcd26729598a1
import pandas as pd

def dumbbell_plot(data,input_year, input_month):
    
    #Filter the dataframe by selected year and selected month, making sure they fall in the desired range.
    df = preprocess.filter_by_year_month(data, input_year, input_month)

    df['sdate'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%B-%d')
    custom_data=list(df[['sdate','tapOperationTime','tapTime_PowLoss']].to_numpy())
    
    # The dumbbell plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = [df["Date"].dt.day,df["Time"]],
        y = df["tapTime_PowLoss"], 
        mode = 'markers',
        marker = dict(color = '#483D8B'),
        name = 'Tap Power Loss Time',
        ),
    )

    fig.add_trace(go.Scatter(x = [df["Date"].dt.day,df["Time"]],
        y = df["tapOperationTime"], 
        mode = 'markers',
        marker = dict(color = '#FF6EB4'),
        name = "Tap Operation Time",
        ),
    )
    
    # Add vertical lines for dumbbell plot
    for i in range(df.shape[0]):
        fig.add_shape(
            type = "line",
            line = dict(color='#282828'),
            layer ="below",
            x0 = i,
            y0 = df['tapTime_PowLoss'].iloc[i],
            x1 = i,
            y1 = df['tapOperationTime'].iloc[i],
        )
    
    # Set hover template for bumbbell plot
    fig.update_traces(customdata=custom_data,
                hovertemplate=template.get_dumbbell_hover_template())
    
    # Updating the layout
    fig.update_layout(
        title = "Tap Power Loss Time and Tap Operation Time for year: {}, Month: {}".format(input_year, input_month),
        xaxis_title = "Time",
        xaxis = dict(title = 'Day-And-Time',
            gridcolor = '#BDBDBD',
            side = 'bottom',
            position = 0.01,
            type = 'multicategory',
            tickfont = dict(size=10),
            tickangle = -45,
            ticklabeloverflow = 'hide past domain'),
        yaxis = dict(showgrid=False),
        legend_title ='<b> Time </b>',
        width = 1500
    )

    return fig   
