import pandas as pd

vehiculo = pd.read_csv('vehiculos.csv')
vehiculo = vehiculo.dropna()

vehiculo.shape

vehiculo.info

vehiculo.head()

pd.value_counts(vehiculo['class'])

import matplotlib.pyplot as plt

pd.value_counts(vehiculo['class']).plot(kind="bar")