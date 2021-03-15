import pandas as pd
import numpy as np
rstglvr = np.random.RandomState(42)
rstglsr = pd.Series(rstglvr.randint(0, 20, 5))
rstgldf = pd.DataFrame(rstglvr.randint(0, 20, (4, 5)),columns=['A', 'B', 'C', 'D', 'E'])

A = rstglvr.randint(20, size=(4, 5))
dfA = pd.DataFrame(A, columns=list('XYZTW'))
#print(dfA - dfA.iloc[0])

# axis0 sütun için

# apply: herhangi bir metodu tüm çerçeveye uygular

#print(dfA.apply(np.cumsum))

# girilmeyen veriler

# nan: nan ile yapılan her işlem sonuç döndürür

veri2 = {
    'ogrno' : ['08','16','32','74'],
    'odev' : [56, 72, 60, 84], 
    'proje' : [70, 43, 57, 71]
}
ders2 = pd.DataFrame(veri2)
ders2 = ders2.append(pd.DataFrame({'ogrno' : 18, 'proje' : 37}, index=[4]), sort=True)

#print(pd.isna(ders2)) # null değerleri true gösterir

#print(ders2.dropna(subset=['odev'])) # içinde boş değer olan satırları siler
#print(ders2.dropna()) # boş olan satırları siler
#print(ders2.dropna(axis=1)) # boş olan sütunları siler
#print(ders2)
#print(ders2.dropna(how='any')) # en az bir değeri nan olansiler, all ise satır ve sütununlarla hepsini siler 

#print(ders2.fillna(0)) # method parametresi ile 'bfill' bir önceki 'ffill' bir sonraki değer ile değiştirir
#print(ders2.fillna(0, axis=1))