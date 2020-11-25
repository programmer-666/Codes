import pandas as ps
import numpy as np
seri = ps.Series(list(range(0,10,2)))
print(seri, "\n" ,seri[0])# key 'a' değerleri de kabul eder
print(seri[[1,2]])
print(seri.ndim)
print(seri.dtype)
print(seri.shape)
print(seri.sum())#max, min,  
print(seri*2)  
print(seri+(seri+1.1/seri+2.2))  
print(np.sqrt(seri))
print(seri <= 2)