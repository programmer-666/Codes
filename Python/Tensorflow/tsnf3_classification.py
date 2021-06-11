# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:11:21 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout # overfitting problemlerini çözmek için
from tensorflow.keras.callbacks import EarlyStopping # overfitting problemlerini çözmek için
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_excel('maliciousornot.xlsx')
print(data.corr()['Type'].sort_values())
#sbn.countplot(x = 'Type', data = data)
""" classification datas """
y_type = data['Type'].values
x = data.drop('Type', axis = 1).values
xtr, xte, ytr, yte = train_test_split(x, y_type, test_size = 0.3, random_state = 20)

scaler = MinMaxScaler()
scaler.fit(xtr)
xtr = scaler.transform(xtr)
xte = scaler.transform(xte)

model = Sequential()
model.add(Dense(units = 30, activation = 'relu'))
model.add(Dropout(0.25)) # layer tarafında overfitting önlemek için
model.add(Dense(units = 15, activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(units = 15, activation = 'relu'))
model.add(Dropout(0.25))
model.add(Dense(units = 1 , activation = 'sigmoid')) # sigmoid 1-0 arası değer verir, sınıflandırma için kullanılrbilir
# neden 30?
# sütun sayısı kadar giriş layera nöron eklenir, daha etkili
estp = EarlyStopping(monitor = 'val_loss', mode = 'min', verbose = 1, patience = 25)
""" stop early """
model.compile(loss = 'binary_crossentropy', optimizer = 'adam') # sigmoid olduğundan
model.fit(x = xtr, y = ytr, epochs = 700, validation_data = (xte, yte), verbose = 1, callbacks = estp)

modelLoss = pd.DataFrame(model.history.history)
modelLoss.plot()

predicts = model.predict_classes(xte)

print(classification_report(yte, predicts))
print(confusion_matrix(yte, predicts)) # 5-6 yanlış
""" classification model """