# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:21:49 2021

@author: suhar
"""

# Regresyon genelde tahmindir,
# x bağımsız, y bağımlı

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('satislar.csv')

aylar = data[['Aylar']]
satislar = data[['Satislar']]

xtr, xte, ytr, yte = train_test_split(aylar, satislar, test_size = 0.33, random_state = 0)
sc = StandardScaler()

Xtr = sc.fit_transform(xtr)
Xte = sc.fit_transform(xte)
Ytr = sc.fit_transform(ytr)
Yte = sc.fit_transform(yte)

lr = LinearRegression()
lr.fit(Xtr, Ytr)
preds = lr.predict(Xte)

rp = sc.inverse_transform(preds) # ters scaling
xtr =  xtr.sort_index()
ytr =  ytr.sort_index()

plt.scatter(xtr, ytr)
plt.scatter(xte, rp)