# -*- coding: utf-8 -*-
"""
Created on Sat May 22 02:25:47 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = pd.read_csv("CarPrices/merc.csv")
print(data.describe())
print(data.isnull().sum()) # checks null cells

# understanding data
#sbn.distplot(data['price']) # distribution plot
# ortalamayı yükseltecek az sayıda olan pahalı araçlar çıkarılabilir
#sbn.countplot(data['year']) # yıllara göre araç sayısı
print('\n', data.corr()['price'].sort_values()) # korelasyon -> data.corr()
# örneğin mil sayısı fiyatı eksi yönde etkiler

# graphical analysis
#sbn.scatterplot(x = "mileage", y = "price", data = data) # mil arttıkça fiyat düşer
print(data.sort_values("price", ascending = False).head(20)) # en yüksek fiyatı en yukarda getirir (ascending)
# verisetindeki en yüksek fiyatlı arabalar bulunur ve atılır
# araçları bulmak için len(data)*0.01

# most expensive cars
data99 = data.sort_values('price', ascending = False).iloc[131:]
#sbn.distplot(data99['price'])
print(data.groupby('year').mean()['price']) # verileri yılllara göre gruplar ve ortalama fiyatı bulur
data997 = data99[data.year != 1970].groupby('year').mean()['price']
print(data997)
data = data99[data99.year != 1970].drop('transmission', axis = 1)
data2 = data99[data99.year != 1970].drop('transmission', axis = 1)

data2 = data2.drop('model', axis = 1)
data2 = data2.drop('fuelType', axis = 1)
# data cleaning
""" """
y_price = data['price'].values
data = data.drop('price', axis = 1) # drop price, take all
data = data.drop('model', axis = 1) # drop price, take all
x = data.drop('fuelType', axis = 1).values # drop price, take all
xtr,xte,ytr,yte = train_test_split(x, y_price, test_size = 0.3, random_state = 10)

scaler = MinMaxScaler()
xtr = scaler.fit_transform(xtr)
xte = scaler.fit_transform(xte)

model = Sequential()
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(1))

model.compile(optimizer = 'adam', loss = 'mse')
model.fit(x = xtr, y = ytr, validation_data=(xte, yte), epochs = 300, batch_size = 300)
# otomatik xte ve yte karşılaştırması validate_data

""" creating model """
lossData = pd.DataFrame(model.history.history)
#lossData.plot()

predArr = model.predict(xte) 
mae = mean_absolute_error(yte, predArr)
print(mae, mae/data2['price'].mean()) # meanabso/meanprice ile yüzdelikli fark bulunur fazlaysa sıkıntı var
plt.scatter(yte, predArr)

newCarS = data2.drop('price', axis = 1).iloc[2] # get new data without price

newCarS = scaler.transform(newCarS.values.reshape(-1, 5))

print(model.predict(newCarS))
""" evaluate the results """
