# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:59:45 2021

@author: suhar
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

xtr = pd.read_csv('xtr.csv')
xte = pd.read_csv('xte.csv')
ytr = pd.read_csv('ytr.csv')
yte = pd.read_csv('yte.csv')

sc = StandardScaler()

Xtr = sc.fit_transform(xtr)
Xte = sc.fit_transform(xte)

# ölçekleme

# veri önişleme