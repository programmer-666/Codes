# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:10:23 2021

@author: suhar
"""

# değişkenlerin aralarında doğrusal olmayan bağıntılar varsa tercih edilir.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv('maaslar.csv')
# eğitim seviyesi x, maaslar y

x, y = veriler.iloc[:, 1:2], veriler.iloc[:, 2:]
xv, yv = x.values, y.values

""" SIRADAN LINEER REGRESYON """
from sklearn.linear_model import LinearRegression

lreg = LinearRegression()
lreg.fit(xv,yv) # lineer olmayan verilerde lineer regresyon

plt.scatter(xv,yv) # gerçek veri
plt.plot(x, lreg.predict(xv), color = 'red') # tahmin
plt.show()
""" SIRADAN LINEER REGRESYON """

from sklearn.preprocessing import PolynomialFeatures
# herhangi bir seriyi polinomsal ifadede kullanılır

poreg = PolynomialFeatures(degree = 5) # 2.dereceden bir polinom objesi
# poreg ile birlikte regresyon yapılabilir

xpo = poreg.fit_transform(xv) # veriler önce polinom tipine çevrilir
# sonra lineer regresyon için tekrardan bir dönüşüm yapılmalıdır

lreg2 = LinearRegression()
lreg2.fit(xpo, yv) # üç kolonun çarpanlarını öğrenen sistem

plt.scatter(xv,yv)
plt.plot(xv, lreg2.predict(xpo))