import numpy as np
ls = [[1,2,3],[4,5,6],[7,8,9]]

array = np.array(ls)
may = array.reshape(3,3)
print(may, may.ndim, may.shape)