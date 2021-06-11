# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dict_local = {"idx":3, "idy":4, "idz":5}
ps = pd.Series(dict_local)
ps2 = pd.Series(data=[1,2,3], index=['x', 'y', 'z'])
# series
ps2['x']
ps2p = ps2+ps2
# series properties
data = np.random.randn(3,3)
df = pd.DataFrame(data, index = ['x', 'y', 'z'], columns=('a', 'b', 'c'))
print(df['a'])
print(df[['a', 'c']])
print(df.loc["x"])
print(df.loc["x"]['a'])
print(df.iloc[0]) # loc with index
print()
# dataframes
df['d'] = df['c']+df['a']+df['b']
print(df)
df = df.drop('d', axis=1) # axis 0 is horizontal, inplace=true -> equals
print(df)
print(df < 0)
print(df[df < 0])
print(df[df['a'] < 0])
print()
# dataframes indexes
print(df.reset_index())
nix = ['cx', 'cyz', 'cxa']
df.index = nix # the same goes for the columns
df['d'] = [1,2,3]
df = df.set_index('d')
print(df) 
# change index
"""
parents = ['a Class', 'a Class', 'b Class', 'b Class']
childs = ['xseries', 'xseries', 'yseries', 'yseries']
concated = list(zip(parents, childs))
dfm = pd.MultiIndex.from_tuples(concated)
npa = np.array([[10, 'a'], [10, 'b'], [30, 'c'], [10, 'd']])
dfm = pd.DataFrame(concated, index = [[10, 'a'], [10, 'b'], [30, 'c'], [10, 'd']], columns = ['x', 'y'])
"""
# multi index
mdf = df[df < 0]
print(mdf.dropna()) # deletes all nan rows, axis = 1 drops cols, thresh = 2 -> if cell have 2 nan
mdf = mdf.fillna('x')
# missing datas
deps = {"Departman":["Yazilim", "Yazilim", "Siber Güvenlik"],
        "Gorevli":["Ahmet", "Veli", "Cezve"],
        "Maas":[100, 200 , 300]}
depm = pd.DataFrame(deps)
print()
print(depm.groupby("Departman").count()) # employers
print(depm.groupby("Departman").mean())
print(depm.groupby("Departman").describe())
# group
d1 = {"name":["lorem", "ipsum","dolor","sit"],
      "type":[12,22,13,14],
      "code":[1,11,111,1111]}
d2 = {"name":["pixar", "pras","tuya","fexer"],
      "type":[13,52,53,24],
      "code":[2,22,222,2222]}
cdf1 = pd.DataFrame(d1, index = [0,1,2,3])
cdf2 = pd.DataFrame(d2, index = [0,1,2,3])
print()
print(pd.concat([cdf1,cdf2],ignore_index=True)) 
# concat
d1 = {"name":["lorem", "ipsum","dolor","sit"],
      "code":[1,11,111,1111],
      "xkey":[44,13,22,1]}
d2 = {"name":["lorem", "ipsum","dolor","sit"],
      "xkey":[44,13,22,1]}
ddf1 = pd.DataFrame(d1, index = [0,1,2,3])
ddf2 = pd.DataFrame(d2, index = [0,1,2,3])
print(pd.merge(ddf1, ddf2, on = "name"))
# merge
print(cdf1['name'].unique(), cdf1['name'].nunique())
print(cdf1['name'].value_counts())
def p1f(col):
    # plus 1 function
    return col+1
print(cdf1['code'].apply(p1f))
print(cdf1.isnull())
# advanced
dataex = pd.read_excel("dataex.xlsx")
print(dataex)
dataex['test'] = [1,23,34]
dataex.to_excel("ToExcel.xlsx")
# working with excel