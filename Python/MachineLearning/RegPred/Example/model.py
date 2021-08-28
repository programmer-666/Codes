# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

xtr = pd.read_csv('xtr.csv').values
ytr = pd.read_csv('ytr.csv').values.reshape(len(xtr) ,)

xte = pd.read_csv('xte.csv').values
yte = pd.read_csv('yte.csv').values.reshape(len(xte) ,)
# Dataset Input

rfr = RandomForestRegressor(random_state = 0, n_estimators = 5) # estimator 4
rfr.fit(xtr, ytr)

svr = SVR(kernel = 'rbf')
svr.fit(xtr, ytr)

poreg = PolynomialFeatures(degree = 3) # degree 2
xpo = poreg.fit_transform(xtr)
xtpo = poreg.fit_transform(xte)
lreg = LinearRegression()
lreg.fit(xpo, ytr)
# Model

ypredf = pd.Series(rfr.predict(xte))
ypredf_svr = pd.Series(svr.predict(xte))
ypredf_pol = pd.Series(lreg.predict(xtpo))
ytef = pd.Series(yte)
# Predict

r2s_rf = r2_score(y_true = ytef, y_pred = ypredf)
r2s_svr = r2_score(y_true = ytef, y_pred = ypredf_svr)
r2s_pol = r2_score(y_true = ytef, y_pred = ypredf_pol)
# Evaluates

print(r2s_rf, r2s_svr, r2s_pol)