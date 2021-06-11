import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import tensorflow as wtf
from tensorflow.keras.models import Sequential # çalışılacak katmanları belirtir
from tensorflow.keras.layers import Dense # modele katmanları eklemek için
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error # hata değerleri, gerçek hatayı görmek için
from tensorflow.keras.models import load_model # model load etmek için
data = pd.read_csv('btk_data.csv')
#sb.pairplot(data)

# data import
y_price = data['price'].values
xps = data[['prop1', 'prop2']].values

xtr, xte, ytr, yte = train_test_split(xps, y_price, test_size=0.33)
# create test side

scaler = MinMaxScaler()
scaler.fit(xtr)

xtr = scaler.transform(xtr)
xte = scaler.transform(xte)
"""scaling/fitting"""

model = Sequential()
model.add(Dense(8, activation='relu')) # neuron num, actv func (adds layer)
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1)) # output neuron
model.compile(optimizer = 'rmsprop', loss = 'mse')
# creating model

model.fit(xtr, ytr, epochs=150)
loss = model.history.history['loss'] # loss 

##sb.lineplot(x = range(len(loss)), y = loss)
trloss = model.evaluate(xtr, ytr, verbose = 0)
teloss = model.evaluate(xte, yte, verbose = 0)

print(trloss, teloss)
# training
testPredicts = pd.Series(model.predict(xte).reshape(330, ))
predictDf = pd.DataFrame(yte, columns = ['Reals Y'])

concDf = pd.concat([predictDf, testPredicts], axis = 1)
concDf.columns = ['Real Y', 'Predict Y']

print(concDf)

sb.scatterplot(x = "Real Y", y = "Predict Y", data = concDf)

mae = mean_absolute_error(concDf['Real Y'], concDf['Predict Y'])
mse = mean_squared_error(concDf['Real Y'], concDf['Predict Y'])
print(mae, mse)
# mae için ortalama bir fiyat 870 ise 870+-mae çok önemli değil
# model evaluation
newDataProps = [[1760, 1758]]
newDataProps = scaler.transform(newDataProps)
print(model.predict(newDataProps)) # özelliklerden fiyat tahmini
model.save('btk_model.h5')
#loaded_model = load_model('btk_model.h5')
# model predicts