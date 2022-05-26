#!/usr/bin/python3
# -*- coding: utf-8 -*-

from dash import Dash, html, dcc,Input,Output
import meteofunc
from multiprocessing import Process

exp = 'oper'
basePeriod = 'obs'

app = Dash(__name__)

stat = []
model = []
field = []
region = []
term = []
source = []
timeperiod = []

exp_m = []
field_m =[]
stat_m =[]
model_m =[]
basePeriod_m =[]
region_m =[]
term_m =[]
timeperiod_m =[]
source_m = []

def set_layout(field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m):
    print(field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m)

    app.layout = html.Div([
        html.Div([
            dcc.RadioItems(['Lead time','Time period'],"Lead time"),
            
            html.Button('Submit', id='submit-val', n_clicks=0),
            html.Hr(),

            html.Div(id='container-button-basic',
                children='Enter a value and press submit'),

            html.Div(children=[
                html.Label('Model'),
                dcc.Dropdown(model_m,  id='model_id',multi = True)]),
                html.Div(id='dd-output-container1'),
            
            html.Div(children=[
                html.Label('Field'),
                dcc.Dropdown(field_m,  id='field_id',multi = True)]),
                html.Div(id='dd-output-container2'),

            html.Div(children=[
                html.Label('Term'),
                dcc.Dropdown(term_m, id='term_id',multi = True)]),
                html.Div(id='dd-output-container4'),

            html.Div(children=[
                html.Label('Region'),
                dcc.Dropdown(region_m, id='region_id',multi = True)]),
                html.Div(id='dd-output-container3'),

            html.Div(children=[
                html.Label('Time Period'),
                dcc.Dropdown(timeperiod_m,  id='timeperiod_id',multi = True)]),
                html.Div(id='dd-output-container5'),

            html.Div(children=[
                html.Label('Stat'),
                dcc.Dropdown(stat_m,  id='stat_id',multi = True)]),
                html.Div(id='dd-output-container'),

            html.Div(children=[
                html.Label('Source'),
                dcc.Dropdown(source_m, id='source_id',multi = True)]),
                html.Div(id='dd-output-container6'),

            html.Div(children=[
                html.Label('Experiment'),
                dcc.Dropdown(exp_m, id='exp_id',multi = True)]),
                html.Div(id='dd-output-container7'),
            
            html.Div([ dcc.Graph(id = "graph"),

        ], style={'padding': 10, 'flex': 1}),    
        ],style={'width': '100%', 'display': 'inline-block'}),

    ], style={'display': 'flex'})


@app.callback(
    Output('dd-output-container7', 'children'),
    Input('exp_id', 'value')
)
def set_source(exp_id):
    global exp
    exp = exp_id

@app.callback(
    Output('dd-output-container6', 'children'),
    Input('source_id', 'value')
)
def set_source(source_id):
    global source
    source = source_id

@app.callback(
    Output('dd-output-container', 'children'),
    Input('stat_id', 'value'),
)
def set_stat(stat_id):
    global stat
    stat = stat_id
@app.callback(
    Output('dd-output-container1', 'children'),
    Input('model_id', 'value'),
)
def set_model(model_id):
    global model
    model = model_id
@app.callback(
    Output('dd-output-container2', 'children'),
    Input('field_id', 'value'),
)
def set_field(field_id):
    global field
    field = field_id

@app.callback(
    Output('dd-output-container3', 'children'),
    Input('region_id', 'value'),
)
def set_region(region_id):
    global region
    region = region_id

@app.callback(
    Output('dd-output-container4', 'children'),
    Input('term_id', 'value')
)
def set_term(term_id):
    global term
    term = term_id

@app.callback(
    Output('dd-output-container5', 'children'),
    Input('timeperiod_id', 'value')
)

def set_timeperiod(timeperiod_id):
    global timeperiod
    timeperiod = timeperiod_id

@app.callback(
    Output('graph', 'figure'),
    Input('submit-val', 'n_clicks'),
)

def bb(n_clicks):
    # global stat,field,model,region,term,timeperiod,source,exp
    print(stat)
    print(field)
    print(model)
    print(region)
    print(term)
    print(timeperiod)
    print(source)
    print(exp)
    if (field != None) and (timeperiod != None) and (model != None) and (term != None) and (region != None) and (stat!=None) and (source!=None) and (exp!=None):
        fig = meteofunc.read_data(field,model,exp,basePeriod,timeperiod,term,region,stat,source)
    else:
        fig = meteofunc.base_data()
    return fig
def set_values():
    global field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m

    field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m = meteofunc.create_data()
def runer(field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m,path):
    meteofunc.set_data(path)

    set_layout(field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m)
    app.run_server(debug=False,host = "0.0.0.0",port= "8051")

def main(path):
    meteofunc.set_data(path)
    set_values()

    proc1 = Process(target=runer, args = (field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m,path))
    proc1.start()
