import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import MinMaxScaler

# tahmin için kullanılmakla birlikte ilk olarak sınıflandırmada kullnılmıştır
# grafik farklı uzaylara bölünerek karar ağaçları oluşturulur
# mesela boyu 145 büyük ve kilo 75 küçük olanlar gibi
# basittir

trdata, tedata = pd.read_csv('synt_tr_data.csv'), pd.read_csv('synt_te_data.csv')
# importing data

xtr, xte = trdata.iloc[:, :3], tedata.iloc[:, :3]
ytr, yte = trdata.iloc[:, 3:], tedata.iloc[:, 3:]
# data proccessing

sc = MinMaxScaler()
xtr, xte = sc.fit_transform(xtr), sc.fit_transform(xte)
ytr, yte = sc.fit_transform(ytr), sc.fit_transform(yte)
# scaling

dtr = DecisionTreeRegressor(random_state=0)

dtr.fit(xtr, ytr)
pred = dtr.predict(xte).reshape(-1, 1)

ipred = sc.inverse_transform(pred)
iyte = sc.inverse_transform(yte)

plt.plot(xtr, ytr)
plt.plot(xte, pred)