#app.py

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('data/sample_data.csv')

# Create app
app = dash.Dash(_name_)

# Layout
app.layout = html.Div([
    html.H1("Sample Dashboard"),
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": col, "value": col} for col in df.columns if df[col].dtype != 'object'],
        value=df.columns[1]
    ),
    dcc.Graph(id="line-chart")
])

# Callback
@app.callback(
    dash.dependencies.Output("line-chart", "figure"),
    [dash.dependencies.Input("dropdown", "value")]
)
def update_chart(selected_col):
    fig = px.line(df, y=selected_col, title=f"{selected_col} Over Time")
    return fig

if _name_ == "_main_":
    app.run_server(debug=True)


