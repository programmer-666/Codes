import pandas as pd
import numpy as np
import random

x = 10**3
price = [random.randint(1000, 30000) for i in range(x)]
price = np.array(price)
p1 = [random.randint(100, 201) for i in range(x)]
p1 = np.array(p1)
p2 = [random.randint(300, 401) for i in range(x)]
p2 = np.array(p2)

df = pd.DataFrame({"price":price, "prop1":p1, "prop2":p2})
df.to_csv("data.csv", index=False)