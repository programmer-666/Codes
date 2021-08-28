# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 02:40:00 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

data = pd.read_csv('eksikveriler.csv')
ulke = data.iloc[:, 0:1].values

le = preprocessing.LabelEncoder()
ulke[:, 0] = le.fit_transform(data.iloc[:, 0])

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
