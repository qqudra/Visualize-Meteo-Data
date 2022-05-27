#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
from dash import Dash, html, dcc,Input,Output
import meteofunc_new
import main_new
from multiprocessing.pool import Pool
from multiprocessing import Process
import glob

file_name = ""
csv_list = []

def check_csv():
    for filename in glob.glob("*.csv"):
        print (filename)
        csv_list.append(filename)
    return csv_list
check_csv()


app1 = Dash(__name__)

app1.layout = html.Div([
    html.Div([

        html.H3(id='my-output'),

        html.H3("Vizualization"),

        html.Label('Source list'),
        dcc.Dropdown(['Blinov','Bagrov','Bykov','Versus','MET','Data base','Other'],'Blinov',  id='source_list',multi = True),

        html.Div(id='dd-output-container10'),
    
        html.Div(id='container-button-basic',
            children='Select file'),
        
        html.Div(children=[
            dcc.Dropdown(csv_list,str(csv_list[0]) , id='file_id')]),
            html.Div(id='dd-output-container'),

        html.Button('Read data', id='submit_val', n_clicks=0),
        
        html.Hr(),

        html.H3("Verification"),

        html.H6("Таблица файлов в наличии "),

        html.Button('Verification list', id='Verification-val', n_clicks=0),
        html.Button('Calculate', id='Calculate-val', n_clicks=0),

        html.Hr(id = "BBB"),

        html.H3("Matching"),

        html.Hr(),

        html.H3("Data observation"),

        html.Hr(),

        html.H3("Data experiments"),

        html.H6("Link database"),
        html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),

    ],style={'width': '100%', 'display': 'inline-block'}),

], style={'display': 'flex'})

@app1.callback(
    Output('dd-output-container', 'children'),
    Input('file_id', 'value'),
)
def set_file_name(file_id):
    global file_name
    if(file_id != None):
        file_name = file_id
    print(file_name)

@app1.callback(
    Output('my-output', 'children'),
    Input('submit_val', 'n_clicks'),
)
def set_stat(n_clicks):
    ret_str = ""
    if n_clicks>0:
        # meteofunc.set_data(file_name)
        main_new.main(file_name)
        ret_str = "Status: started"
    return f'{ret_str}'


def apps():
    app1.run_server(debug=False, host = "0.0.0.0",port="8050")
   
if __name__ == '__main__':
    proc = Process(target=apps, name='Test')
    proc.start()


