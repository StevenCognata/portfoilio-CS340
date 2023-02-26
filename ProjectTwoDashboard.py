from jupyter_plotly_dash import JupyterDash
import dash
import dash_leaflet as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table as dt
from dash.dependencies import Input, Output, State
import os
import numpy as np
import pandas as pd
from pymongo import MongoClient
from bson.json_util import dumps
import base64

from animalShelter import AnimalShelter

###########################
# Data Manipulation / Model
###########################

username = "aacuser"
password = "password"


shelter = AnimalShelter(username, password)
df = pd.DataFrame.from_records(shelter.read({}))


app = JupyterDash('SimpleExample')

animal_type_options = [{'label': 'All', 'value': 'all'},
                       {'label': 'Cat', 'value': 'Cat'},
                       {'label': 'Dog', 'value': 'Dog'},
                       {'label': 'Rabbit', 'value': 'Rabbit'}]


app.layout = html.Div([
    html.Center(html.B(html.H1('SNHU CS-340 Dashboard'))),
    html.Hr(),
    html.Div(
        id='filter-id',
        className='col s12 m6',
        children=[
            html.Label('Filter by Animal Type'),
            dcc.RadioItems(
                id='animal-type-filter',
                options=animal_type_options,
                value='all'
            )
        ]
    ),
    html.Br(),
    dt.DataTable(
        id='datatable-id',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        sort_action="native",
        filter_action="native",
        page_action="native",
        page_current=0,
        page_size=10
    ),
    html.Br(),
    html.Div(className='row', style={'display': 'flex'},
             children=[
                 html.Div(
                     id='graph-id',
                     className='col s12 m6',
                 ),
                 html.Div(
                     id='map-id',
                     className='col s12 m6',
                 ),
             ]),
])

@app.callback(
    [Output('datatable-id', 'data'),
     Output('datatable-id', 'columns')],
    [Input('animal-type-filter', 'value')])
def update_dashboard(animal_type):

    if animal_type == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['animal_type'] == animal_type]

    columns = [{"name": i, "id": i, "deletable": False, "selectable": True} for i in filtered_df.columns]
    data = filtered_df.to_dict('records')

    return data, columns

@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': '#D2F3FF'
    } for i in selected_columns]

