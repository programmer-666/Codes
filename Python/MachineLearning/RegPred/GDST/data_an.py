import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import StandardScaler

train_data = pd.read_csv("gtr.csv")
test_data = pd.read_csv("gte.csv")

train_data_wi = pd.read_csv("gtr.csv").drop(['iter', 'cell'], axis = 1) # without iter
test_data_wi = pd.read_csv("gte.csv").drop(['iter', 'cell'], axis = 1) # without iter
# iter değişkeni problem olabilir, y değişkenini büyük ölçüde etkiliyor gibi (train için)
""" VERILERIN DAHIL EDILMESI """

print(train_data.corr())
print(train_data_wi.corr())
# iter ile iter değişkeni olmayan arasındaki fark (train)

print(test_data.corr())
print(test_data_wi.corr())
# iter ile iter değişkeni olmayan arasındaki fark (test) [iter etkiliyor]

print(train_data_wi.describe())
print(test_data_wi.describe())

""" KORELASYON """

sn.lineplot(data = train_data_wi['y'])
sn.lineplot(data = test_data_wi['y'])
#plt.show()

# Birinci grafik eğitim verisetindeki hareket
# İkinci grafik eğitim verisetindeki hareket

""" GRAFIKLER """

#sc = StandardScaler()
#train_data_wi = sc.fit_transform(train_data_wi)
#test_data_data_wi = sc.fit_transform(test_data_wi)

""" SCALING """

train_data_wi.to_csv("trawi.csv")
test_data_wi.to_csv("teswi.csv")