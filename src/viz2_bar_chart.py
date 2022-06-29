import plotly.express as px
import pandas as pd
import datetime as datetime
import collections
import template


def BarChart(data, date_range):
        
        Duration = {0:[7,'Last 7-days'], 1:[30, 'Last 30-days'], 2:'All_time_data'}

# Get the data for the selected duration
        if date_range==2: selected_data=data
        else:
                duration = Duration[date_range][0]
                end = data['Date'].iloc[-1]                                               
                start = end - datetime.timedelta(days = duration)                      
                selected_data = data.loc[(data['Date'] >= start)& (data['Date'] <= (end))] 
                
        tapAfter = selected_data['tapAfter'].tolist()
        counter = collections.Counter(tapAfter)
        
# Creating the dataframe for the selected date
        df = pd.DataFrame(counter.items(),
                columns=['Tap position', 'Number of Change'])
        df=df.sort_values('Tap position')
        
        # Plot bar chart for viz 2
        fig = px.bar(df,
                x = 'Number of Change',
                y = 'Tap position',
                orientation = 'h',
        )

        # Add hover_template 
        fig.update_traces(hovertemplate = template.get_hover_template_viz2())

        # Update layout
        fig.update_layout(title="The number of tap changes per each tap position for the selected timeframe",
                          yaxis_type='category')


        return fig