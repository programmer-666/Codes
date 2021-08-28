# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 16:05:37 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   random import randint

serit_len = 1500

def rand_seritno_gen():
    global serit_len
    n = randint(1, 3)
    nar = []
    for i in range(serit_len):
        if n == 2:
            n = randint(1, 3)
            nar.append(n)
        elif n == 1:
            n = randint(1, 2)
            nar.append(n)
        elif n == 3:
            n = randint(2, 3)
            nar.append(n)
    return nar

def create(datasetname = 'dataset_syn.csv'):
    global serit_len

    serit1 = pd.Series([randint(0, 1)  for i in range(serit_len)])
    serit2 = pd.Series([randint(0, 1)  for i in range(serit_len)])
    serit3 = pd.Series([randint(0, 1)  for i in range(serit_len)])
    seritno = pd.Series(rand_seritno_gen())

    seritler = pd.DataFrame(pd.concat([serit1, serit2, serit3], axis = 1))

    seritler.iloc[:, 0] = serit1
    seritler.iloc[:, 1] = serit2
    seritler.iloc[:, 2] = serit3

    dataset = pd.DataFrame(pd.concat([seritler, seritno], axis = 1))

    for i in range(serit_len): # making path
        dataset.iloc[i, seritno.loc[i]-1] = 0

    dataset.columns = ['serit1', 'serit2', 'serit3', 'seritno']

    dataset.to_csv(datasetname, index = False)
    
create()
create('test_dataset_syn.csv')