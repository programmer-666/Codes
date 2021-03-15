import pandas as pd
notlar = pd.read_csv('ders_notlar.csv', index_col='ad', skipinitialspace=True)
# indekslenen sutun
#print(notlar.index)
# tüm sutunlar
#print(notlar.columns)
# Herhangi bir ogrencinin butun notlari
#print(notlar.loc['ogrenci28'])
# Tum arasinav notlari
#print(notlar['arasinav'])
#print(notlar["durum"].value_counts())

notlar['durum'].value_counts().plot(kind='bar')

notlar['final'].plot()