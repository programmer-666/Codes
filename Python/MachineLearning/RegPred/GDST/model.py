# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:46:30 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

train_data = pd.read_csv("trawi.csv").drop(0)
test_data  = pd.read_csv("teswi.csv").drop(0)

test_data.drop([26,26], axis=0, inplace=True)
test_data.drop([27,27], axis=0, inplace=True)

xtr = train_data.iloc[:, 0:7].values
xte = train_data.iloc[:, 7:8].values

ytr = test_data.iloc[:, 0:7].values
yte = test_data.iloc[:, 7:8].values

poreg = PolynomialFeatures(degree = 4) # 4 -> 20%

xpo = poreg.fit_transform(xtr)
xepo = poreg.fit_transform(xte)
ypo = poreg.fit_transform(ytr)
yepo = poreg.fit_transform(yte)

lreg = LinearRegression()
lreg.fit(xpo, xte)

ypred = lreg.predict(ypo).round(1)

# LINEAR REGRESSION #
#reg = LinearRegression()
#reg.fit(xtr, xte)
#ypred = reg.predict(ytr)
#pred = pd.DataFrame(ypred, columns = ['Predict']).values
#y_Te = pd.DataFrame(yte, columns = ['Test']).values
#sn.color_palette("pastel")
#sn.scatterplot(data = pred)
#sn.scatterplot(data = y_Te)
# LINEAR REGRESSION #

""" GRAPH """

plt.plot(range(len(ypred)), ypred, color = 'red')
plt.plot(range(len(yte)), yte, color = 'black')

""" GRAPH """

yp = pd.Series((yte.flatten()-ypred.flatten())**2)
print(1/yp.median())