# -*- coding: utf-8 -*-

import numpy as np

npa1 = np.array([1,2,3,4,5,6,7])
npm = np.array([[1,2,3], [4,5,6], [7,8,9]])
# session 1 end
print(np.arange(0, 10, 1))
print(np.zeros(5))
print(np.zeros((3,3)))
print(np.ones((3,3)))
print(np.linspace(0,20,5))
print(np.eye(3))
# session 2 end
print(np.random.randn(7))
print(np.random.randn(7,7))
print(np.random.randint(0, 7)) # 0, 6 actualy
print(np.random.randint(0, 7, 7))
# session 3 end
npa1 = np.random.randint(0, 1000, 25).reshape(5,5)
print(npa1, npa1.max(), npa1.min())
print(npa1.argmax(), npa1.argmin())
print(npa1.shape, npa1.reshape(25,))
# session 4 end
npa1[3:8] = -1.2443
print(npa1)
# session 5 end
print(npm)
print(npm[1][1] == npm[1,1])
print(npm[0:, 2])
print(npm[[1,2]])
# session 6 end
print(npa1[npa1 > 500]) # elements of bigger than 500
print(np.sqrt(npm))
# session 7 end