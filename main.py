#!/usr/bin/python3
# -*- coding: utf-8 -*-

# #Сюда подставляете свой токен

from ast import Div
import pandas as pd
from dash import Dash, html, dcc,Input,Output,State
import meteofunc
import plotly.graph_objs as go
import numpy as np


field = 't2m'
model = 'cm01msk'
exp = 'oper'
basePeriod = 'obs'
time = '2021020100-2021022821'
term = '0'
region = '125_ETR+'
stat = 'rmse_05'
source = 'Blinov'

field_m,stat_m,model_m,basePeriod_m, region_m, term_m = meteofunc.create_data()


app = Dash(__name__)

app.layout = html.Div([
    html.Div([

        html.Div(children=[
            html.Label('Stat'),
            dcc.Dropdown(stat_m,  id='stat_id')]),

        html.Div(children=[
            html.Label('Model'),
            dcc.Dropdown(model_m,  id='model_id')]),

        html.Div(children=[
            html.Label('Field'),
            dcc.Dropdown(field_m,  id='field_id')]),

        html.Div(children=[
            html.Label('Region'),
            dcc.Dropdown(region_m, id='region_id')]),

        html.Div(children=[
            html.Label('Term'),
            dcc.Dropdown(term_m, id='term_id')]),

        html.Div([ dcc.Graph(id = "graph"),
            #    dcc.Slider(min = 0, max = 48, step = 3, id = "sliders",
            #    value = 48)

    ], style={'padding': 10, 'flex': 1}),    
    ],style={'width': '100%', 'display': 'inline-block'}),

], style={'display': 'flex'})

@app.callback(
    Output('graph', 'figure'),
    Input('stat_id', 'value'),
    Input('model_id', 'value'),
    Input('field_id', 'value'),
    Input('region_id', 'value'),
    Input('term_id', 'value'),
    # Input('sliders', 'value'),
)
def g1(stat_id,model_id,field_id,region_id,term_id):
    global stat,model,field,region,term
    
    stat = stat_id
    model = model_id
    field = field_id
    region = region_id
    term = term_id

    print(field,model,exp,basePeriod,time,term,region,stat,source)
    fig = meteofunc.read_data(field,model,exp,basePeriod,time,term,region,stat,source)
    return fig  

if __name__ == '__main__':
    app.run_server(debug=True)