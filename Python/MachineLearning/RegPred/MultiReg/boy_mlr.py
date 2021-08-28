 # -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 02:26:50 2021

@author: suhar
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

data = pd.read_csv('eksikveriler.csv')

ulke = data.iloc[:, 0:1].values

le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(data.iloc[:,0])
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

yas = data.iloc[:,1:4].values

c = data.iloc[:, -1:].values
le = preprocessing.LabelEncoder()
boyc[:,-1] = le.fit_transform(data.iloc[:,-1])
ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()

res = pd.DataFrame(data = ulke, index = range(22), columns = ['fr', 'tr', 'us'])
res2 = pd.DataFrame(data = yas, index = range(22), columns = ['kilo', 'yas', 'cinsiyet'])
res3 = pd.DataFrame(data = c[:, :1], index = range(22), columns = ['cinsiyetboy'])

rr2c = pd.concat([res, res2], axis = 1)
rr2cr3 = pd.concat([rr2c, res3], axis = 1)

xtr, xte, ytr, yte = train_test_split(rr2c, res3, test_size = 0.33, random_state=0)

# VERI HAZIRLIGI

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(xtr, ytr)

ypred = reg.predict(xte)

