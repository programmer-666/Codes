# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 02:15:10 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# eksik veriler ortalama ile doldurulabilir
# sklearn kullanılır
data = pd.read_csv('eksikveriler.csv')
ival = (1,4)
nar = data.iloc[:, ival[0]:ival[1]].values

def mean_imputer(nar, ival = (1,4)):
    ipt = SimpleImputer(missing_values = np.nan, strategy = 'mean') # np.nan tipini, ortalama ile değiştir
    nar_i = ipt.fit(nar[:, ival[0]:ival[1]]) # öğren
    nar[:, ival[0]:ival[1]] = nar_i.transform(nar[:, ival[0]:ival[1]]) # uygula
    return nar

print(mean_imputer(nar))