import numpy as np
n = np.random.randint(10,100,6)
n2 = np.random.randint(10,100,6)
nn2 = n+n2
x = n.reshape(2,3)
y = n.reshape(2,3)
z = np.vstack((x,y))#dikey birleştirme, hstack horizontal yatay
print(x > 3)