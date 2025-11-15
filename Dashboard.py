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

  def update_csv_time_series(selected_smoothie):
    filtered_df = df_csv[df_csv['Smoothie'] == selected_smoothie]
    fig = px.line(filtered_df, x="Date", y="Sales",
                  title=f"{selected_smoothie} sales over time(csv)")
    
    return fig

@app.callback(
    Output("static-sales-graph", 'figure'),
    Input("static-smoothie-dropdown", 'value')   
)

def update_csv_time_series(selected_smoothie):
    filtered_df = df_static[df_static['Smoothie'] == selected_smoothie]
    fig = px.bar(filtered_df, x="Day", y="Sales",
                  title=f"{selected_smoothie} sales by Day(Static)")
    
    return fig

if __name__ =='__main__':
    app.run(debug=True)