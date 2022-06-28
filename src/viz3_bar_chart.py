import pandas as pd
import preprocess
import plotly.express as px
import template

def bar_plot_animation_Max_PowerLoss(data):

    # Plot bar chart for viz 3
    fig = px.bar(data,
        x = "Time_in_Hours",
        y = "Max_PowerLoss", 
        animation_frame = 'Tap Value', 
        custom_data = ['Max_loadCurr','Max_PowerLoss','Max_EnergyLoss','Max_CircCurr']
    )
    
    # Add hover_template
    fig = fig.update_traces(hovertemplate = template.get_viz3_hover_template())

    # Update layout
    fig.update_layout(
            xaxis = dict(
            tickmode = 'linear',
            tick0 = 0,
            dtick = 1
                )
            )
    
    # Update axes
    fig.update_yaxes(range = [0, .9],
                     tick0 = 0, 
                     dtick = 0.1,
                     title_text = 'Max Power Loss (Kwt)')
    
    fig.update_xaxes(title_text = 'Date in Year')
    
    # Set the hover in each frame
    for frame in fig.frames:
        for data in frame.data:
            data.hovertemplate = template.get_viz3_hover_template()
            
    return fig


#df  = preprocess.drop_irrelevant_time(oltc_data)
#df1 =  preprocess.adjust_data_for_viz3(df)
#fig = bar_plot_animation_Max_PowerLoss(df1)

#fig.show()
