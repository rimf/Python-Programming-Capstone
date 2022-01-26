import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output


########### Import and clean data

data = pd.read_csv("AnnualTicketSales.csv")

########### Define Variables
sourceurl = 'https://www.kaggle.com/johnharshith/hollywood-theatrical-market-synopsis-1995-to-2021'
githublink = 'https://github.com/rimf/Python-Programming-Capstone'

########### Set up the layout

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Film Analytics"


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🍿", className="header-emoji"),
                html.H1(
                    children="26 Years of Films", className="header-title"
                ),
                html.P(
                    children="Analyze Hollywood's theatrical release market"
                    "against movie ticket prices and sales"
                    "from 1995 to 2021",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["YEAR"],
                                    "y": data["AVERAGE TICKET PRICE"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Movie Ticket Price per Year",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#7e1653"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        config={"displayModeBar": False},
                                figure={
                                    "data": [
                                        {
                                            "x": data["YEAR"],
                                            "y": data["TICKETS SOLD"],
                                            "type": "lines",
                                        },
                                    ],
                                    "layout": {
                                        "title": {
                                            "text": "Movie Tickets Sold Per Year",
                                        },
                                        "xaxis": {"fixedrange": False},
                                        "yaxis": {"fixedrange": False},
                                        "colorway": ["#16537E"],
                                    },
                                },
                            ),
                            className="card",
                        ),
                    ],
                    className="wrapper",
                ),
            ]
        )
############ Deploy

if __name__ == "__main__":
    app.run_server(debug=True)
