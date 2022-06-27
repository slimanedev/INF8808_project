import plotly.graph_objects as go
import preprocess, template

def get_monthly_current_plot(data):
    
    data = preprocess.get_monthly_average_current(data)
    year_list = data['year'].unique().tolist()
    
    # Define months dictionary
    month = ['January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    # Plot bar chart for viz 8
    fig = go.Figure()
    for year in year_list:
        data_year = data[data.year==year]
        data_year = data_year.sort_values(by=['month'])
        fig.add_trace(go.Bar(x=data_year.month,
            y=data_year['tapCircCurrAmp'],
            name=year,
            text =data_year['year'],
            hovertemplate =template.get_hover_template_viz8(),
        ),
    )

    # Update axes
    fig.update_xaxes(categoryorder='array',categoryarray= month)
    fig.update_yaxes(title='Average tap circulating current (KA)')

    # Update layout
    fig.update_layout(title="Average tap circulating current over months of the years")

    return fig
