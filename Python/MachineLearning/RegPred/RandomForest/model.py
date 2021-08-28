# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 00:55:38 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

# ensemble learning
"""
birden fazla sınıflandırma veya regresyon algoritması kullanılarak
daha başarılı bir sonucun çıkartıldığı algoritma çeşidi.

kollektif öğrenme de denir

random forest birden fazla karar ağcının aynı problem üzerinde
çalıştığı bir modeldir. (forest)

majority vote: çoğunluğun oyu
    sınıflandırma problemlerinde en çok kim oy verirse o
    regresyonda ise ağaçların ortalamaları sonucu veririr

!!!
karar ormanlarında veri artarsa başarı düşer

dallanma overfittinge girer
çok fazla dala odaklanma sonucu hesaplama zamanı uzar
!!!
"""
trdata = pd.read_csv('synt_tr_data.csv')
tedata = pd.read_csv('synt_te_data.csv')

xtr, xte = trdata.iloc[:, :3], tedata.iloc[:, :3]
ytr, yte = trdata.iloc[:, 3:], tedata.iloc[:, 3:]

sc = MinMaxScaler()
xtr, xte = sc.fit_transform(xtr), sc.fit_transform(xte)
ytr, yte = sc.fit_transform(ytr), sc.fit_transform(yte)

rfr = RandomForestRegressor(random_state = 0, n_estimators = 10) # estimater sayısı, çizilecek karar ağacı sayısı
# verinin 10 farklı parçasıyla 
rfr.fit(xtr, ytr.ravel())

ypred = rfr.predict(xte).reshape(-1, 1)
iypred = sc.inverse_transform(ypred)
iyte = tedata.iloc[:, 3:]
iytef, iypredf = pd.DataFrame(iyte), pd.DataFrame(iypred)

mae = mean_absolute_error(iyte, iypred)
mse = mean_squared_error(iyte, iypred)
me = float(iytef.median())-float(iypredf.median())

print(mae, mse, me)

# 3.282844107744115  16.433192585563898 1.0                -> estimator 5
# 3.2774966329966393 16.382737203913496 1.1404040404040643 -> estimator 10

iypredf.to_csv('synt_pred.csv', index=False)
iytef.to_csv('synt_yte.csv', index=False)