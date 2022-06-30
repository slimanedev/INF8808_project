import pandas as pd
import plotly.express as px

# This function is for the all time data
def plot_box_chart(data, year):
    '''
    Get the box chart for the viz 4
        Args:
            data: The dataframe to process
            year: selected year
        Returns:
            fig: The box chart
    '''
    data['Date'] = pd.to_datetime(data['Date'])
    idx1 = data['Date'].dt.year == year
    df = data[idx1]

    # Plot for the box chart
    fig = px.box(df, 
        x = 'tapBefore', 
        y = "tapOperationTime",
        labels = {'tapBefore': 'Tap position'}
        )
    
    # Get Average commutation time for all the tap positions
    global_average = data['tapOperationTime'].mean().round(3)
    
    # Add mean time period to switch tap as an horizontal-dotted-black-line
    fig.add_hline(y = global_average,
        line_dash = "dot",
        annotation_text = "All-time average", 
        annotation_position = "bottom left",
        annotation_font_size = 12,
        annotation_font_color = "black"
    )
    
    # Define critical value as time period of half a cycle (t_critical = 1/(2 * 50Hz))
    critical_value = 1/(50*2) 

    # Add critical time period as an horizontal-dashed-red-line 
    fig.add_hline(y = critical_value,
        line_dash = 'dot',
        line_color = 'red',
        annotation_text = "Critical value (not to reach)",
        annotation_position = "top left",
        annotation_font_size = 12,
        annotation_font_color = "red",
    )
    
    # Update layout
    fig.update_layout(
        title = f"Box-plot for the tap operation time based on the tap position in year {year}",
        xaxis_title = "Tap position",
        yaxis_title = 'Tap operation time (second)'
    )
        
    return fig
