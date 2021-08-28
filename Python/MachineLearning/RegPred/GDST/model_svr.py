import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import SVR

train_data = pd.read_csv("trawi.csv").drop(0)
test_data  = pd.read_csv("teswi.csv").drop(0)
# Dataset
sc = StandardScaler()

test_data.drop([26, 26], axis=0, inplace=True)
test_data.drop([27, 27], axis=0, inplace=True)

xtr = sc.fit_transform(train_data.iloc[:, 0:7].values)
xte = sc.fit_transform(train_data.iloc[:, 7:8].values)

ytr = sc.fit_transform(test_data.iloc[:, 0:7].values)
yte = sc.fit_transform(test_data.iloc[:, 7:8].values)

svr = SVR(kernel = 'poly', C = 1.98) 
# rbf 0.2792973173527777
# linear 0.9
# poly 0.4250459318558905, c = 1.98
# sigmoid 0.06
# 
svr.fit(xtr, xte)
ypred = svr.predict(ytr) # y hat

yp = pd.Series((yte.flatten()-ypred.flatten())**2)
print(yp.median())

plt.plot(range(len(ypred)), ypred, color = 'red')
plt.plot(range(len(yte)), yte, color = 'black')

result = pd.concat([pd.DataFrame(train_data.iloc[:, 0:7]),pd.DataFrame(sc.inverse_transform(ypred)).shift(periods = 1)], axis = 1)
print(result)