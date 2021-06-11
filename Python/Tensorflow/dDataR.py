import pandas as pd
from datetime import datetime

data = pd.read_csv('Deprem.csv')

for i in range(len(data['Zaman'])):
    data['Zaman'].iloc[i] = int(datetime.timestamp(datetime.strptime(data['Zaman'].iloc[i], '%Y-%m-%d %X')))

data.to_csv('EarthQs.csv')