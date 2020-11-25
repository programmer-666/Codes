import pandas as ps
import numpy as np
ns = list(range(0,100,10))
ns.append("A")
pns = ps.Series(ns)
#print(ps.Series("Test", ['a',2,'a.a',4]))
dy = {
    "users":{
        "1":"ali",
        "2:":"cem"
    },
    "key":134
}
print(ps.Series(dy))
print(ps.Series(np.random.randint(10,100,3)))
