import pandas as pd
import numpy as np

#seriler
gk = pd.Series([0.33, 4.87, 5.97, 0.643], index=['merkur', 'venus', 'dunya', 'mars'], name='Kutle') # pandas serisi
ps = pd.Series(np.random.randn(5)*7) # indexsiz seri
ds = pd.Series(({'merkur':0.33,'venus':4.87})) # dict 
ds2 = pd.Series(({'merkur':0.33,'venus':4.87}), index=['venus', 'merkur']) # farklı sıralamalı sözlük

# serilerde işlemler
#print(gk[:2]);print()
#print(gk[::2]);print()
#print(gk > gk['merkur']);print()
#print(gk[gk > gk['merkur']]);print()
#print(gk[:-1]);print() # sondan bir eksik
#print(gk.median());print() # dizinin orta değeri
#print('Betelgeuse' in gk)
#print(gk.mean(), gk.std(), gk.mean()-gk.std()) # ortalama ve standart sapma
#print(gk**2) # dizideki tüm değerlerin karesi
#print(gk/3.14159**3)

a = pd.Series(np.random.randn(10)*3.14159)
b = pd.Series(np.random.randn(10)*3.14159)
ab = pd.Series((a*b))
#print(ab,ab.name)

# serilere veri ekleme
ex = pd.Series(({'alpha':1, 'beta':2}))
ex = ex.append(pd.Series({'gama':3}))

print(ex)