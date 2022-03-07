#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import plotly.graph_objs as go

DATA = pd.read_csv('/home/nikita/Рабочий стол/Диплом/combine_est.csv', sep=';')

def sort_field(DATA,name):
    mass = []
    for i in range (len(DATA.field)):
        mass.append(DATA[name][i])

    sort_m = []
    for item in mass:
        if item not in sort_m:
            sort_m.append(item)
    return sort_m

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

    ###############################Tern####################################
    term_m = sort_field(DATA,"term")
    print(term_m)

    return field_m,stat_m,model_m,basePeriod_m, region_m, term_m

def read_data(field,model,exp,basePeriod,time,term,region,stat,source):

    data1 = [[]]
    for i in range (len(DATA)):
        # if DATA['stat'][i] == (stat) and DATA['model'][i] == model and DATA['field'][i] == field and DATA['basePeriod'][i] == basePeriod and DATA['timeperiod'][i] == time and DATA['term'][i] == term and DATA['region'][i] == region and DATA['source'][i] == source and DATA['exp'][i] == exp:
        if DATA['stat'][i] == stat and DATA['model'][i] == model and DATA['field'][i] == field and DATA['basePeriod'][i] == basePeriod and DATA['term'][i] == term and DATA['region'][i] == region:
            data1.append([DATA['00'][i],DATA['03'][i],DATA['06'][i],DATA['09'][i],
            DATA['12'][i],DATA['15'][i],DATA['18'][i],DATA['21'][i],DATA['24'][i],
            DATA['27'][i],DATA['30'][i],DATA['33'][i],DATA['36'][i],DATA['39'][i],
            DATA['42'][i],DATA['45'][i],DATA['48'][i]])
    data1.pop(0)

    print(data1)
    fig = go.Figure()

    for i in range (len(data1)):
        fig.add_trace(go.Scatter(x=np.arange(0, len(data1[i])), y = data1[i],name=str(i)))
    fig.write_image("img.png")
    return fig
