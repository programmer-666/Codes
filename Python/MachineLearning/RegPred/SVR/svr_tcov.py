import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import datetime
import time 

veriler = pd.read_csv('BNB-USD.csv').drop('Date', axis = 1)

#for i in range(len(veriler['Date'])):
#    veriler['Date'].loc[i] = time.mktime(datetime.datetime.strptime(veriler['Date'].loc[i], "%Y-%m-%d").timetuple())

x, y = veriler.iloc[:, 1:], veriler.iloc[:, 0:1]
X, Y = x.values, y.values

scs = [StandardScaler(), StandardScaler()]

xs, ys = scs[0].fit_transform(X), scs[1].fit_transform(Y.reshape(-1, 1))

svr = SVR(kernel = 'rbf')
svr.fit(xs, ys)
pred = svr.predict(xs) # y hat

ipred, iys = scs[1].inverse_transform(pred), scs[1].inverse_transform(ys)

plt.plot(ys,pred,color='blue')
