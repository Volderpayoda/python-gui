import numpy as np
import pandas as pd

from packages.c45 import *

path = 'datasets/iris.csv'

# Obtener el conjunto de datos
data = pd.read_csv(filepath_or_buffer = path, sep = ',')

# Obtener el conjunto de atributos
attributes = data.columns

# Obtener el conjunto de clases
length = attributes.size - 1
classcolumn = attributes[length]
classes = data[attributes[length]].unique()

# Eliminar la columna de clase de la lista de atributos
attributes = attributes.drop(labels = [attributes[length]])

# print("Las observaciones distintas en la columna de clase son:")
# print(data[data.columns[data.columns.size - 1]].nunique())

# print(sameClassC(data.loc[data['variety'] == 'Setosa'], classcolumn))
