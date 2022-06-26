import pandas as pd
import plotly.graph_objects as go

def get_monthly_current_plot(df):

    year_list = df['year'].unique().tolist()

    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December']

    fig = go.Figure()
    for year in year_list:
        df_year = df[df.year==year]
        df_year = df_year.sort_values(by=['month'])
        fig.add_trace(go.Bar(x=df_year.month, y=df_year['tapCircCurrAmp'], 
                            name=year))

    fig.update_xaxes(categoryorder='array', categoryarray= month)
    fig.update_yaxes(title='Average tap circulating current (KA)')
    fig.update_layout(title="Average tap circulating current over months of the years")

    return fig
