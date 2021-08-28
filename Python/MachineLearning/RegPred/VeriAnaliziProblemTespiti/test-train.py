# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:16:51 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

data = pd.read_csv('eksikveriler.csv')
ulke = data.iloc[:, 0:1].values

le = preprocessing.LabelEncoder()
ulke[:, 0] = le.fit_transform(data.iloc[:, 0])

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

res = pd.DataFrame(data = ulke, index = range(22), columns = ['fr', 'tr', 'us'])


ival = (1,4)
nar = data.iloc[:, ival[0]:ival[1]].values

def mean_imputer(nar, ival = (1,4)):
    ipt = SimpleImputer(missing_values = np.nan, strategy = 'mean') # np.nan tipini, ortalama ile değiştir
    nar_i = ipt.fit(nar[:, ival[0]:ival[1]]) # öğren
    nar[:, ival[0]:ival[1]] = nar_i.transform(nar[:, ival[0]:ival[1]]) # uygula
    return nar

res2 = pd.DataFrame(data = mean_imputer(nar), index = range(22), columns = ['boy', 'kilo', 'yas'])

res3 = pd.DataFrame(data = data.iloc[:, -1].values, index = range(22), columns = ['cinsiyet'])

rr = pd.concat([res, res2], axis = 1)
rr2 = pd.concat([res, res3], axis = 1)
# birleştirme

from sklearn.model_selection import train_test_split

xtr, xte, ytr, yte = train_test_split(rr, res3, test_size = 0.33, random_state=0)

xtr.to_csv('xtr.csv')
xte.to_csv('xte.csv')
ytr.to_csv('ytr.csv')
yte.to_csv('yte.csv')