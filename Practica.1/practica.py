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

# print("Size: " + data.shape)







