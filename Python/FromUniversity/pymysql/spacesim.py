"""
?
2 boyutlu yapı
Uzay kare şeklinde olacak
node denilen cisimlerin kütlesi olacak ve boşlukta yer kaplayacaklar (özkütle aynı, boyuta göre hacim değişir)
"""
import random
x = 1000
y = 1000
space = [x,y]#1km, 1km
node1 = [random.randint(0,1001), random.randint(0,1001)]
node1h = node1[0]*node1[1]
print(node1h, x*y)