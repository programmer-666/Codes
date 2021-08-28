# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:46:56 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import random 


a = 0
n = 100 # 20
r = 0
x = []
y = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            a+=1
            x.append((i,j,k))
            y.append(i+j+k)

x = pd.DataFrame(x, columns=['var1', 'var2', 'var3'])
y = pd.DataFrame(y, columns=['res'])

data = pd.concat([x,y], axis = 1)

data.to_csv('synt_tr_data.csv', index=False)


x, y = [], []
for i in range(2000): # 2000
    a,b,c = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
    x.append((a,b,c))
    y.append(a+b+c)
    
x = pd.DataFrame(x, columns = ['var1', 'var2', 'var3'])
y = pd.DataFrame(y, columns = ['res'])

test_data = pd.concat([x,y], axis = 1)

test_data.to_csv('synt_te_data.csv', index=False)