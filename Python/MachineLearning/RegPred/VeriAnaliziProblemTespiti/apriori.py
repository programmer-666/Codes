# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:37:27 2021

@author: suhar
"""
# veri önişleme
import pandas as pd              # veri muhafazası
import numpy as np               # büyük değerlerle işlem
import matplotlib.pyplot as plt  # veri çizdirme
# modüller

data = pd.read_csv('veriler.csv')
boy_kilo = data[['boy', 'kilo']]