# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 02:28:25 2021

@author: suhar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('dataset_syn.csv')
test_dataset = pd.read_csv('test_dataset_syn.csv')

print(dataset.corr())
print(test_dataset.corr())

dlen = len(dataset)
serit1 = dataset.iloc[:, 0]
serit2 = dataset.iloc[:, 1]
serit3 = dataset.iloc[:, 2]
seritno = dataset.iloc[:, 3]

test_dlen = len(dataset)
test_serit1 = test_dataset.iloc[:, 0]
test_serit2 = test_dataset.iloc[:, 1]
test_serit3 = test_dataset.iloc[:, 2]
test_seritno = test_dataset.iloc[:, 3]

plt.plot(dataset)
plt.show()
plt.plot(test_dataset)
plt.show()

trainx_data = pd.DataFrame(pd.concat([serit1,serit2,serit3], axis=1))
trainy_data = pd.DataFrame(seritno)

testx_data = pd.DataFrame(pd.concat([test_serit1,test_serit2,test_serit3], axis=1))
testy_data = pd.DataFrame(test_seritno)

trainx_data.to_csv('xtr.csv', index = False)
trainy_data.to_csv('ytr.csv', index = False)
testx_data.to_csv('xte.csv', index = False)
testy_data.to_csv('yte.csv', index = False)