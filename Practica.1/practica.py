import numpy as np
import pandas as pds

## Obtengo y muestro datos
weatherPath = './weatherAUS.csv'
data = pds.read_csv(weatherPath)
print(data)

# Obtengo las caracteristicas de los datos
data_frame = pds.DataFrame
print(data_frame.shape)
print(data[0:5])
# Obtengo las 5 primeras lineas
print(data[0:5])

# 5

# print("Size: " + data.shape)

# 10
from sklearn import preprocessing

arreglo = preprocessing.LabelEncoder()
df = df.apply(arreglo.fit_transform)

scaler = preprocessing.MinMaxScaler()
scaler.fit(df)

df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
df.iloc[4:10]




