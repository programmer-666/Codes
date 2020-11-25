import numpy as np
np_array = np.array([1,3,5,7,9])
np_array2 = np.arange(2,10,2)
np_zero = np.zeros(10)#ones
np_l = np.linspace(0,100,5)
np_r = np.random.randint(0,11, 10)
np_ar = np.arange(40)
np_ar_rs = np_ar.reshape(4, 10)
#print(np_ar_rs.sum(axis=1))
#print(np_ar_rs.sum(axis=0))
rnm = np.random.randint(1,100,10)
print(rnm.max(), rnm.argmax())#min