# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 02:20:24 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# ilk olarak sınıflandırma problemlerinde kullanılmıştır
# iki sınıfı birbirinden ayırmak için kullanılmıştır
# amaç max margin elde etmek

# regresyon tarafında ise maximum noktayı alabilme problemine dönüşür
# margin aralığına max noktayı almak
# margin dışında kalanlar ise hata olarak kabul edilir.

# doğrusal veya doğrusal olmayan formüller kullanılabilir
# bunun dışında kernel fonksiyonu ile birlikte de kullanılabilir
# bunun için RBF,exp veya polynominal gibi fonksiyonlar mevcuttur

# scaler kullanmak zorunludur (hassas)

veriler = pd.read_csv('maaslar.csv')
# eğitim seviyesi x, maaslar y

x, y = veriler.iloc[:, 1:2], veriler.iloc[:, 2:]
X, Y = x.values, y.values

scs = [StandardScaler(), StandardScaler()]

xs, ys = scs[0].fit_transform(X), scs[1].fit_transform(Y.reshape(-1, 1))

svr = SVR(kernel = 'rbf')
svr.fit(xs, ys)
pred = svr.predict(xs) # y hat

plt.scatter(xs,ys,color='red')
plt.plot(xs,pred,color='blue')