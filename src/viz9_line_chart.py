import plotly.graph_objects as go
import template

def get_transformer_avg_current_plot (data1,data2, year):   
    
    idx1 = data1['Date'].dt.year == year
    idx2 = data2['Date'].dt.year == year
    
    df1 = data1[idx1] ; df2=data2[idx2]

    df1 = df1.groupby('Time', as_index=False).mean().round(3)
    df2 = df2.groupby('Time', as_index=False).mean().round(3)

    # Plot line chart for viz 9.1
    fig = go.Figure()
    fig = fig.add_trace(go.Scatter(x=df1.Time,
        y = df1.TrafoLoadCurr,
        mode = 'lines',
        name = 'Weekdays',
        marker_color = 'green',
        line_shape = 'spline',
        hovertemplate = template.get_hover_template_viz9_linechart(),
        ),
    )
    fig = fig.add_trace(go.Scatter(x=df2.Time,
        y = df2.TrafoLoadCurr,
        mode = 'lines',
        name = 'Weekends',
        marker_color = 'blue',
        line_shape = 'spline',
        hovertemplate = template.get_hover_template_viz9_linechart(),
        ),
    )

    # Update layout
    fig.update_layout(title = f'Average Load current on Transformer during hours of the day in year {year}',
        xaxis_title = 'hour of the day',
        yaxis_title = 'Load current (KA)',
    )

    return fig

def get_transformer_max_current_plot (data1,data2, year):   
    
    idx1 = data1['Date'].dt.year == year
    idx2 = data2['Date'].dt.year == year
    
    df1 = data1[idx1] ; df2=data2[idx2]

    df1 = df1.groupby('Time', as_index=False).max().round(3)
    df2 = df2.groupby('Time', as_index=False).max().round(3)

    # Plot bar chart for viz 9.2
    fig = go.Figure()
    fig = fig.add_trace(go.Bar(x = df1.Time,
        y = df1.TrafoLoadCurr,
        name = 'Weekdays',
        marker_color = 'green',
        hovertemplate = template.get_hover_template_viz9_barchart(),
        ),
    )
    fig = fig.add_trace(go.Bar(x = df2.Time,
        y = df2.TrafoLoadCurr,
        name = 'Weekends',
        marker_color = "blue",
        hovertemplate = template.get_hover_template_viz9_barchart(),
        ),
    )

    # Update layout
    fig.update_layout(title = f'Maximum Load current on Transformer during hours of the day in year {year}',
        xaxis_title = 'hour of the day',
        yaxis_title = 'Load current (KA)',
    )

    return fig
    