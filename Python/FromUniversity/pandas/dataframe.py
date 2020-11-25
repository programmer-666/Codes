import pandas as ps
#seri1+seri2 = s1s2Dataframe
df = ps.DataFrame(dict(s1d = ps.Series([1,2,3]), s2d = ps.Series([30,22,11])))
print(df)