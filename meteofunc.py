#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import plotly.graph_objs as go

DATA = ""
# DATA = pd.read_csv('../combine_est_t2m.csv', sep=';')

def set_data(path):
    global DATA
    DATA = pd.read_csv(path, sep=';')

def sort_field(DATA,name):
    mass = []
    for i in range (len(DATA.field)):
        mass.append(DATA[name][i])

    sort_m = []
    for item in mass:
        if item not in sort_m:
            sort_m.append(item)
    return sort_m

def base_data():

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(0, 10), y = np.arange(0, 10),name="base graph"))

    return fig

def create_data():
    
    ###############################field#####################################
    field_m = sort_field(DATA,"field")
    ###############################stat######################################
    stat_m = sort_field(DATA,"stat")

    ###############################model#####################################
    model_m = sort_field(DATA,"model")

    ###############################basePeriod################################
    basePeriod_m = sort_field(DATA,"basePeriod")

    ###############################Region####################################
    region_m = sort_field(DATA,"region")

    ###############################Term######################################
    term_m = sort_field(DATA,"term")

    ###############################Time######################################
    timeperiod_m = sort_field(DATA,"timeperiod")

    ###############################Source######################################
    source_m = sort_field(DATA,"source")

    ###############################Experiment######################################
    exp_m = sort_field(DATA,"experiment")

    return field_m,stat_m,model_m,basePeriod_m, region_m, term_m, timeperiod_m,source_m,exp_m

def read_data(field,model,exp,basePeriod,timeperiod,term,region,stat,source):

    data1 = [[]]
    name1 = []

    lead_time_name = []
    lt = []
    param_name = []
    
    for i in DATA.columns:
        try:
            x = int(i)

            lead_time_name.append(i)
            lt.append(i)
        except ValueError:
            param_name.append(i)

    for i in lt:
        if(np.isnan(DATA[i][0])):
            lead_time_name.remove(i)

    for i in range(len(DATA)):
        if (DATA['stat'][i] in stat) and (DATA['model'][i] in model) and (DATA['field'][i] in field) and (DATA['basePeriod'][i] in basePeriod) and (DATA['term'][i] in term) and (DATA['region'][i] in region) and (DATA['timeperiod'][i] in timeperiod) and (DATA['source'][i] in source) and (DATA['experiment'][i] in exp):
            time_data = []

            for j in lead_time_name:
                time_data.append(DATA[j][i])
            data1.append(time_data)

            name1.append(
            str(DATA['stat'][i])+" "+
            str(DATA['model'][i])+" "+
            str(DATA['field'][i])+" "+
            str(DATA['basePeriod'][i])+" "+
            str(DATA['term'][i])+" "+
            str(DATA['region'][i])+" "+
            str(DATA['timeperiod'][i])+" "+
            str(DATA['source'][i])+" "+
            str(DATA['experiment'][i])
            )

    data1.pop(0)
    fig = go.Figure()
    for i in range (len(data1)):
        fig.add_trace(go.Scatter(x=np.arange(0, len(data1[i])), y = data1[i],name=name1[i]))
    fig.write_image("img.png")
    return fig
