import numpy as np
# numpy bilimsel hesaplamalarda kullanilir
"""
py_l = [0, 1, 2]
np_l = np.array([0,1,2])

print(np_l.dtype, np.array((0,1.2,1,2)).dtype) # dtype ile tip doner
print(np.array(((1,2),(3,4))).ndim) # ndim dizi boyutu
print(np.array((((1,2,3),(4,5,6), (7,8,9)),((1,2,3),(4,5,6), (7,8,9)))))
print(np.array((((1,2,3),(4,5,6), (7,8,9)),((1,2,3),(4,5,6), (7,8,9)))).shape)
print(np.array(((1,2),(3,4))).shape) # matris sayısı, sütun ve satır sayısı

print(np.array([0,1,2,3,4,5]).reshape(2,3)) # matrisi tekrar boyutlandır
print(np.arange(0,10).reshape(2,5)) # arange başlangıç,bitiş,artış miktarı parametrelerine bağlı olarak değer üretir

np_l2 = np_l.copy() # dizi kopylar
print(np_l,np_l2)

print(np.random.random((3,3))) # 3x3 rastgele değerli matris
print(np.random.randint(10, size = 6)) # 0-9 arası 6 rastgele tam sayı
"""
r = np.arange(1,11)
r = r.reshape(2,5)
r2 = np.arange(11,22)
r2 = r.reshape(5,2)
"""
rR1 = r[0] # 1.satır
rR2 = r[1]

rC1 = r[:, 0] # 1.sütun
rC2 = r[:, 1]

print(rR1, rR2, '\n',r[0:2])
print(rC1,rC2) 
print(r[0,0]) # 1.eleman (satır, sütun)
"""
"""
r = r[::-1] # ters çevrim
print(r+r[::-1])
z = np.zeros((3,3)) # 3x3 0 olan matris
o = np.ones((3,3)) # 3x3 1 olan matris
z2 = np.zeros((3,3,3)) # 3 adet 3x3 0 olan matris
print(z,'\n- - - -')
print(z2,'\n- - - -')
print(o)
print(np.eye(3)) # 3x3 matris olusturur, 3 adet 1 içerir
"""
"""
print(np.concatenate([r,r2], axis=1)) # axis0 alt alta birleştirir
print(r.max()) # max en büyük değer min en küçük
print(r.sum()) # matristeki tüm değerleri toplar
print(r.sum(axis=1)) # matristeki satırları toplar
print(r.sum(axis=0)) # matristeki sütunları toplar
print(r.mean()) # ortalama
print(r.mean(axis=1)) # satır ortalama
print(r.mean(axis=0)) # sütun ortalama
print(r.var()) # varyans
print(r.var()**(1/2), r.std()) # standart sapma
"""
"""
#print(r+r2) # matrisin elemanları toplanır *-/%** için aynı- +1 veya -5 gibi değerler ile işlem yapılırsa her bir elemanı o değerde işler
print(np.sin(r)) # elemanların sinüsünü verir- cos
print(np.sqrt(r)) # elemanların karekökü
print(np.exp(r)) # elemanları e^ olarak işler
print(np.log(r)) # elemanların 10 tabanında logunu alur,
"""
#print(np.dot(r,r2)) # matrisleri çarpar (2,3) => (3,2) olmalıdır
#print(r.T) # transpoz

#print(r[r > 5]) # dizinin elemanlarının 5 ten büyük mü diye kontrol eder r[] ifadesi kaldırılırsa boolean tipte gösterim olur

#np.save("npStest", r) # veri yazar

#print(np.load('npStest.npy')) # veri okur

#np.genfromtxt('test.csv', delimiter=',', names=True) # csv veri okur