import pandas as ps
data = [['a',1], ['b',11], ['c',111]]
df = ps.DataFrame(data, index = [1,2,3], dtype=float, columns=['str', 'num'])
print(df)