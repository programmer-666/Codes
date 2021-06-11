import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv("EarthQs.csv")
data2 = pd.read_csv("EarthQs.csv")
print(data.describe())
print(data.isnull().sum()) # checks null cells

print('\n', data.corr()['Buyukluk'].sort_values()) # korelasyon -> data.corr()

y_price = data['Buyukluk'].values
x = data.drop('Buyukluk', axis = 1).values 
xtr,xte,ytr,yte = train_test_split(x, y_price, test_size = 0.3, random_state = 30)

scaler = MinMaxScaler()
xtr = scaler.fit_transform(xtr)
xte = scaler.fit_transform(xte)

model = Sequential()
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(1))

model.compile(optimizer = 'adam', loss = 'mse')
model.fit(x = xtr, y = ytr, validation_data=(xte, yte), epochs = 300, batch_size = 300)
# otomatik xte ve yte karşılaştırması validate_data

""" creating model """
lossData = pd.DataFrame(model.history.history)
#lossData.plot()

predArr = model.predict(xte) 
mae = mean_absolute_error(yte, predArr)
print(mae, mae/data2['Buyukluk'].mean()) # meanabso/meanprice ile yüzdelikli fark bulunur fazlaysa sıkıntı var
plt.scatter(yte, predArr)
predicts = model.predict_classes(xte)
print(confusion_matrix(yte, predicts))