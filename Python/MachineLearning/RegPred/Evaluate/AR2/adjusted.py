# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 00:44:40 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import statsmodels.api as sm

"""
r2 = 1-(topla(yte-pred)^2/topla(y-yort)^2)

r2 oran olarak çıktı veriri, değer ne kadar büyükse o kadar doğru tahmin
r2 bazen yanlış değer çıktısı verebilir, alternatil olarak adjusted sürümü kullanılır
"""

yte = pd.read_csv('synt_yte.csv')
pred = pd.read_csv('synt_pred.csv')
# random forest data

r2s = r2_score(y_true = yte, y_pred = pred)
smo = sm.OLS(pred, yte).fit().summary()

