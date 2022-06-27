import pandas as pd
import preprocess
import plotly.express as px
import template

def bar_plot_animation_Max_PowerLoss(df1):

    fig = px.bar(df1, x="Time_in_Hours", y="Max_PowerLoss", 
                 animation_frame='Tap Value', 
                 custom_data=['Max_loadCurr','Max_PowerLoss','Max_EnergyLoss','Max_CircCurr'])
    
    fig.update_layout(
            xaxis = dict(
            tickmode = 'linear',
            tick0 = 0,
            dtick = 1
                )
            )
    
    fig.update_yaxes(range=[0, .9],
                     tick0=0, 
                     dtick=0.1,
                     title_text='Max Power Loss (Kwt)')
    
    fig.update_xaxes(title_text='Date in Year')
    
    fig = fig.update_traces(hovertemplate = template.get_viz3_hover_template())

    # Set the hover in each frame
    for frame in fig.frames:
        for data in frame.data:
            data.hovertemplate = template.get_viz3_hover_template()
            
    return fig


#df1 =  preprocess.adjust_data_for_viz3(oltc_data)
#fig = bar_plot_animation_Max_PowerLoss(df1)

#fig.show()
