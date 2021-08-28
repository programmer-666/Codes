 # -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 02:26:50 2021

@author: suhar
"""

# birden fazla değişkenle çalışılacağı için hangilerinin işe yarar olduğunu öğrenmeliyiz

#p_value hata değeri

# değişken seçimi
# bütün değişkenleri dahil etme, korelasyon
# geri doğru eleme: eleme ile ilerleme 
    # sl seçilir (0.005)
    # bütün değişkenler kullanılarak model yapılır
    # en yüksek pval değerive sahip olan değişken ele alınır ve şayet
        # pval>sl ise en yüksek pval değerine sahip değişken atılır
        # modelden sonraya geri dönülür pval<sl olana kadar döngü devam eder.
# ileri doğru eleme: az değişkenle başlanır, arttırılarak gider
    # sl seçilir (0.005)
    # bütün değişkenler kullanılarak model yapılır
    # en düşük plav değerine sahip değişken seçilir
    # bu aşamada 3.adımda seçilen değişken sabit tutularak yeni bir değişken daha seilir ve sisteme eklenir
    # makine öğrenmesi güncellenir ve 3.adıma geri dönülür, şayet en düşük
        # pval değere sahip değişken için p<sl ise 3.adıma gidilir değilse biter
# çift yönlü eleme: ileri-geri birleşimidir
    # sl = 0.05
    # bütün değişkenlerle bir model yapılır
    # en düşük pval değerine sahip değişken ele alınır
    # bu aşamada 3.adımda seçilen değişken sabit tutularak diğer bütün değikenler sisteme dahil edilir 
    #ve en düşük pval değerine sahip değişken sistemde kalır
    # sl değerinin altında olan değişkenler sistemde aklır ve eski değişkenlerden hiçbiri sisteme çıkarılmaz
# skor tabanlı
    # bir başarı kriteri belirlenir
    # bütün olası regresyon modelleri inşa edilir (ikili seçim olur)
    # başta belirlenen kriterleri en iyi sağlayan yöntem seçilir
    # makine öğrenmesi sonlandırılır

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
c[:,-1] = le.fit_transform(data.iloc[:,-1])
ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()

res = pd.DataFrame(data = ulke, index = range(22), columns = ['fr', 'tr', 'us'])
res2 = pd.DataFrame(data = yas, index = range(22), columns = ['boy', 'kilo', 'yas'])
res3 = pd.DataFrame(data = c[:, :1], index = range(22), columns = ['cinsiyet'])

rr2c = pd.concat([res, res2], axis = 1)
rr2cr3 = pd.concat([rr2c, res3], axis = 1)
xtr, xte, ytr, yte = train_test_split(rr2cr3, res3, test_size = 0.33, random_state=0)


# VERI HAZIRLIGI

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(xtr, ytr)

ypred = reg.predict(xte)

# MODEL OLUSTURMA
boy = rr2cr3.iloc[:,3:4].values
sol = rr2cr3.iloc[:, :3]
sag = rr2cr3.iloc[:, 4:]
tdf = pd.concat([sol, sag], axis = 1)

xtr, xte, ytr, yte = train_test_split(tdf, boy, test_size = 0.33, random_state=0)

reg = LinearRegression()
reg.fit(xtr, ytr)

ypred = reg.predict(xte)
# boy tahmini
import statsmodels.api as sm

X = np.append(arr = np.ones((22, 1)).astype(int), values = tdf, axis = 1)
xl = tdf.iloc[:, [0,1,2,3,5]].values
xl = np.array(xl, dtype=float)
m = sm.OLS(boy, xl).fit()
print(m.summary())
# Geri Eleme # Backward El.