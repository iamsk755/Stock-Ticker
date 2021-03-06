# -*- coding: utf-8 -*-
"""Stock Ticker Dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r-en_Hsmzzl-WCKowjA5ah-lFOQ0ClOA

https://colab.research.google.com/

https://www.nasdaq.com/market-activity/stocks/screener
"""

from google.colab import files

files.upload()

import pandas

dataframe = pandas.read_csv("Nasdaq.csv")

print(dataframe)

dataframe.head()

dataframe.info()

dataframe.describe()

!pip install jupyter-dash
!pip install dash

from jupyter_dash import JupyterDash

import dash

import dash_html_components as html

import dash_core_components as dcc

from datetime import datetime

app = JupyterDash(__name__)

options = []

for element in dataframe.index:

  options.append({"label": dataframe["Name"][element],
                  "value": dataframe["Symbol"][element]
                  })

app.layout = html.Div([
                       html.H1("Stock Ticker Web App"),
                       html.Div([
                                 html.H2("Select a stock:"),
                                 dcc.Dropdown(
                                     id = "dropdown",
                                     options = options,
                                     value = ["GOOG"],
                                     multi = True
                                 )
                       ]),
                       html.Div([
                                 html.H2("Select Date"),
                                 dcc.DatePickerRange(
                                     id = "datepicker",
                                     min_date_allowed = datetime(2017, 
                                                                 1, 
                                                                 1),
                                     max_date_allowed = datetime.today(),
                                     start_date = datetime(2020, 1, 1),
                                     end_date = datetime.today()
                                 )
                       ]),
                       html.Div([
                                 html.Button(
                                     id = "submit-button",
                                     n_clicks = 0,
                                     children = "Submit"
                                 )
                       ]),
                       dcc.Graph(
                           id = "stock-graph"
                       )
])

app.run_server(port = 3030)