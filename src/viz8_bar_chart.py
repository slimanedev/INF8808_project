import plotly.graph_objects as go
import preprocess, template
import plotly.express as px


def get_monthly_current_plot(data):
    
    data = preprocess.get_monthly_average_current(data)
    
    # Plot line chart for viz 8
    fig = px.line(data,
        x = data['year'],
        y = data['tapCircCurrAmp'],
        color = data['month']
    )

    # Add hover_template 
    fig.update_traces(text = data['month'],
        hovertemplate = template.get_hover_template_viz8()
    )
    
    # Update axes
    fig.update_yaxes(title = 'Average tap circulating current (KA)')

    # Update layout
    fig.update_layout(title = "Average tap circulating current over the years")

    return fig
