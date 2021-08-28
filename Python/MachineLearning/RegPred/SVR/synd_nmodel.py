# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:02:48 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

trdata, tedata = pd.read_csv('synt_tr_data.csv'), pd.read_csv('synt_te_data.csv')
# importing data

xtr, xte = trdata.iloc[:, :3], tedata.iloc[:, :3]
ytr, yte = trdata.iloc[:, 3:], tedata.iloc[:, 3:]
# data proccessing

sc = MinMaxScaler()
xtr, xte = sc.fit_transform(xtr), sc.fit_transform(xte)
ytr, yte = sc.fit_transform(ytr), sc.fit_transform(yte)
# scaling

svr = SVR(kernel = 'rbf')
svr.fit(xtr, ytr)

ypred = svr.predict(xte).reshape(-1 ,1)
# model

i_ypred = sc.inverse_transform(ypred)
i_yte   = sc.inverse_transform(yte)

i_ypredf = pd.DataFrame(i_ypred)
i_ytef   = pd.DataFrame(i_yte)

plt.scatter(range(len(i_ypred)), i_ypred, color='red')
plt.scatter(range(len(i_yte)), i_yte, color='blue')

mae = mean_absolute_error(i_yte, i_ypred)
mse = mean_squared_error(i_yte, i_ypred)
me = i_ytef.median()-i_ypredf.median()

print(mae, mse, me)
# * 7.479202134915928 90.67651886689399 0    2.272267
# * lin 9.599021333333328 139.71514079288877 0    2.5
# analysis