import pandas as pd
import numpy as np

# 1 boyutlu listeler, sözlükler, seriler
# 2 boyutlu numpy dizileri

gzgn_kutleler = pd.Series([0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102], index=['merkur', 'venus', 'dunya','mars','jupiter', 'saturn', 'uranus', 'neptun'], name="Kutle(10^24 kg)")

gezegenler = {'Mg' : gzgn_kutleler,
              'Rg' : pd.Series([2439.5, 6052., 6378., 1737.5, 3396., 71492., 60268., 25559., 24764.,  1185.],\
                    index=['merkur','venus','dunya', 'ay', 'mars', 'jupiter', 'saturn', 'uranus', 'neptun','pluto']),\
            'Prot' : pd.Series([1407.6, -5832.5, 23.9, 655.7, 24.6, 9.9, 10.7, -17.2, 16.1, -153.3],\
                    index=['merkur','venus','dunya', 'ay', 'mars', 'jupiter', 'saturn', 'uranus', 'neptun','pluto']),\
            'Porb' : pd.Series([88.0, 224.7, 365.2, 27.3, 687.0, 4331, 10747, 30589, 59800, 90560], \
                    index=['merkur','venus','dunya', 'ay', 'mars', 'jupiter', 'saturn', 'uranus', 'neptun','pluto'])}
gunes_sistemi = pd.DataFrame(gezegenler)

veri = {
    'x': [3.11,4.15,5.0042],
    'y': [0.525,1.11,1.11],
    'z': [2.,2.01,2.02]
}
#print(pd.DataFrame(veri))

veriL = [
    [0.1,0.23,0.003],
    [23,4,5],
    [1,2,3]
]
# pd.DataFrame(data=veriL, columns=['x','y','z'])

# Numpy dizileri uzerinden veri cercevesi olusturma
tarihler = pd.date_range('20200219', periods=5)
df = pd.DataFrame(np.random.randn(5, 4), index=tarihler, columns=list('ABCD'))

# Birden fazla nesne turu kullanarak veri cercevesi olusturma
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20190219'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["AST413", "AST415", "AST416", "AST515"]),
                    'F': 'Asterosismoloji'})

#print(gunes_sistemi.head()) # ilk 5, parametre ile sayı değişir
#print(gunes_sistemi.tail()) # son 5, parametre ile sayı değişir
#print(gunes_sistemi['Mg'],'[[',gunes_sistemi['Prot']['dunya'])
#print(gunes_sistemi.columns) # sütunlar
#print(gunes_sistemi.describe()) # istatistiksel veriler
#print(gunes_sistemi.sort_values(by='Rg')) # verileri verilen değere göre sıralar
#print(gunes_sistemi['Rg']) # ilgili sütundaki seri
#print(gunes_sistemi.loc['ay']) # ilgili satırdaki seri
#print(gunes_sistemi.iloc[0]) # ilgili satırdaki seri (index ile)
#print(gunes_sistemi[:1]) # koşul
#print(gunes_sistemi[-1:0:-2])
#print(gunes_sistemi['jupiter':'pluto']) # değerler arası verileri seçer

seri_tamindeks = pd.Series(['merkur', 'dunya', 'jupiter'], index=[1, 3, 5])

#print(seri_tamindeks[1]) # 0 girilirse hata dönecektir
#print(seri_tamindeks[0:2])
#print(seri_tamindeks.loc[5]) # kullanıcı tarafından girilen indexler için

# dilimleme kullanıcı tanımlı indisler üzerinden gerçekleşir
#print(gunes_sistemi.loc['jupiter':'merkur', ['Mg', 'Rg']]) # çerçevedeki bir bölüm
#print(gunes_sistemi.loc['ay', ['Prot','Porb']])
#print(gunes_sistemi.iloc[1])
#print(gunes_sistemi.iloc[0:2])
#print(gunes_sistemi.sort_values('Porb').iloc[3])

#print(gunes_sistemi.sort_values('Porb').iloc[1:5,2:4])
#print(gunes_sistemi.sort_values('Porb'))
#print(gunes_sistemi)

#print(gunes_sistemi.iloc[[4,3,0],-1])

#print(gunes_sistemi.loc['venus','Rg']) # belirli bir değer gösterir
#print(gunes_sistemi.iloc[-1, -1]) # belirli bir değer gösterir
#print(gunes_sistemi.at['venus','Rg'])

#print(gunes_sistemi['Rg'] > 3000) # koşul
#print(gunes_sistemi[gunes_sistemi['Mg'] > 10.00]['Rg'])
#print(gunes_sistemi[gunes_sistemi['Mg'] > 10.00])

#print(gunes_sistemi.loc[gunes_sistemi['Prot'] < 24.0])

#gunes_sistemi[gunes_sistemi['Porb'].isin([365.2, 88.00])] # herhangi bir değerin sütunda olup olmadığını kontrol eder

# veri değiştirme [sütun]
df['NEW'] = [1,22,333,4444,55555]

df['E'] = pd.Series([1,2,3,4,5], index=tarihler)

gunes_sistemi['V'] = gunes_sistemi['Mg']*1e27 / (4./3*np.pi*(gunes_sistemi['Rg']*1e5)**3)
gunes_sistemi['e'] = pd.Series([0.205, 0.007, 0.017, 0.055, 0.094, 0.049, 0.057, 0.046, 0.011, 0.244], \
                              index = ['merkur','venus', 'dunya', 'ay', 'mars', 'jupiter', 'saturn', 'uranus', 'neptun', 'pluto'])

# veri değiştirme [satır]
ceres =  {'Prot' : pd.Series([9.1], index=['ceres']),\
         'Rg' : pd.Series([0.074*gunes_sistemi.at['dunya','Rg']], index=['ceres']),\
         'Mg': pd.Series([0.94e-3], index=['ceres'])}
gunes_sistemi = gunes_sistemi.append(pd.DataFrame(ceres), sort=True)

iki_buyuk_uydu = [{'Mg':134.6e-3, 'Rg':2575, 'Prot':382.7, 'e': 0.029}, \
            {'Rg':1352.5, 'Prot':-141.0, 'e':0.000, 'Mg':21.5e-3}]
gunes_sistemi = gunes_sistemi.append(pd.DataFrame(iki_buyuk_uydu, \
                                                  index=['titan','triton']), sort=True)

# satır yada sütun silmek


del df['A']
print(df)

df = df.drop(tarihler[1:3], axis=0)
print(df)
