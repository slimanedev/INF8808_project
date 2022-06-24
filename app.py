"""
Commands : 
To install a virtual env : python -m pip install --user virtualenv
To create a virtual env : python -m virtualenv -p python3.8 venv
To activate a virtual env : source venv/bin/activate

"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
#import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import page1, page2, dashboard


# Get the data
with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)

# Preprocess the data (I will use the object "preprocess.py")
df = pd.read_csv('./fakedata_to_delete.csv')

# Initiate the app 
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# sidebar content
sidebar = html.Div(
    [
        html.H2("INF8808", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Transformer Performance", href="/page-1", active="exact"),
                dbc.NavLink("Tap changer Performance", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

########################## Layout of the app  ##########################
app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])

# Callbacks for the main app
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
# Callbacks function
def render_page_content(pathname):
    # Dashboard page
    if pathname == "/":
        return dashboard.layout
    # Lifespan data page
    elif pathname == "/page-1":
        return page1.layout
    # Day by day page
    elif pathname == "/page-2":
        return page2.layout
    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
