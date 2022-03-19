#!/usr/bin/python3
# -*- coding: utf-8 -*-

# #Сюда подставляете свой токен

from dash import Dash, html, dcc,Input,Output
import meteofunc


field = 't2m'
model = 'cm01msk'
exp = 'oper'
basePeriod = 'obs'
time = '2021020100-2021022821'
term = '0'
region = '125_ETR+'
stat = 'rmse_05'
source = 'Blinov'

stat1 = []
model1 = []
field1 = []
region1 = []
term1 = []

stat_c = 0
model_c = 0
field_c = 0
region_c = 0
term_c = 0

field_m,stat_m,model_m,basePeriod_m, region_m, term_m = meteofunc.create_data()


app = Dash(__name__)

app.layout = html.Div([
    html.Div([

        html.Button('Submit', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic',
             children='Enter a value and press submit'),

        html.Div(children=[
            html.Label('Stat'),
            dcc.Dropdown(stat_m,  id='stat_id',multi = True)]),
            html.Div(id='dd-output-container'),
        
        html.Div(children=[
            html.Label('Model'),
            dcc.Dropdown(model_m,  id='model_id',multi = True)]),
            html.Div(id='dd-output-container1'),

        html.Div(children=[
            html.Label('Field'),
            dcc.Dropdown(field_m,  id='field_id',multi = True)]),
            html.Div(id='dd-output-container2'),

        html.Div(children=[
            html.Label('Region'),
            dcc.Dropdown(region_m, id='region_id',multi = True)]),
            html.Div(id='dd-output-container3'),


        html.Div(children=[
            html.Label('Term'),
            dcc.Dropdown(term_m, id='term_id',multi = True)]),
            html.Div(id='dd-output-container4'),


        html.Div([ dcc.Graph(id = "graph"),

    ], style={'padding': 10, 'flex': 1}),    
    ],style={'width': '100%', 'display': 'inline-block'}),

], style={'display': 'flex'})


@app.callback(
    Output('dd-output-container', 'children'),
    Input('stat_id', 'value'),
)
def set_stat(stat_id):
    global stat_c
    stat1.append(stat_id[stat_c])
    stat_c+=1

@app.callback(
    Output('dd-output-container1', 'children'),
    Input('model_id', 'value'),
)
def set_model(model_id):
    global model_c
    model1.append(model_id[model_c])
    model_c+=1
@app.callback(
    Output('dd-output-container2', 'children'),
    Input('field_id', 'value'),
)
def set_field(field_id):
    global field_c
    field1.append(field_id[field_c])
    field_c+=1

@app.callback(
    Output('dd-output-container3', 'children'),
    Input('region_id', 'value'),
)
def set_region(region_id):
    global region_c
    region1.append(region_id[region_c])
    region_c+=1

@app.callback(
    Output('dd-output-container4', 'children'),
    Input('term_id', 'value'),
)
def set_term(term_id):
    global term_c
    term1.append(term_id[term_c])
    term_c+=1

@app.callback(
    Output('graph', 'figure'),
    Input('submit-val', 'n_clicks'),
)

def bb(n_clicks):
    global stat1,field1,model1,region1,term1

    # print(stat1)
    # print(field1)
    # print(model1)
    # print(region1)
    # print(term1)

    fig = meteofunc.read_data(field1,model1,exp,basePeriod,time,term1,region1,stat1,source)
    return fig

if __name__ == '__main__':
    # app.run_server(host= '0.0.0.0',debug=False)
    app.run_server(debug=True)