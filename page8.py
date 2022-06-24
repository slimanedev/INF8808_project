def histogram_viz8(df):
    fig = px.histogram(df, x="Date", y="tapCircCurrAmp", title="Circulating Current Amplitude") 
    fig.update_layout(
    yaxis_title="Circulating Current Amplitude(KA)",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)
    return fig

def violin_vis8(df,year,month):
    df2=df
    df2['Date'] = pd.to_datetime(df2['Date'])
    df2 = df2.loc[df2['Date'].dt.year == year]
    df2 = df2.loc[df2['Date'].dt.month == month]
    fig = px.violin(df2, x="Date", y="tapCircCurrAmp", title="Circulating Current Amplitude") 
    fig.update_layout(
    yaxis_title="Circulating Current Amplitude(KA)",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="RebeccaPurple"
    )
)
    return fig  
