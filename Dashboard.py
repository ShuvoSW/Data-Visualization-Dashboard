import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Output, Input

df_csv = pd.read_csv("smoothie sales.csv", parse_dates=["Date"])

df_static = pd.DataFrame(
    {
        "Smoothie": ["Banana", "Mango", "Berry", "Papaya", "Mango", "Banana"],
        "Sales": [150, 200, 180, 90, 220, 170],
        "Day": ["Mon", "Mon", "Mon", "Mon", "Tue", "Tue"]
    }
)

app = Dash(__name__)

app.layout = html.Div(

)

@app.callback(
    Output("csv-sales-over-time", 'figure'),
    Input("csv-smoothie-filter", 'value')
)



if __name__ =='__main__':
    app.run(debug=True)