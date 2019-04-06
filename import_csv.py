import numpy as np
import pandas as pd

path = 'datasets/iris.csv'

# Obtener el conjunto de datos
data = pd.read_csv(filepath_or_buffer = path, sep = ',')

# Obtener el conjunto de atributos
attributes = data.columns

# Obtener el conjunto de clases
length = attributes.size - 1
classes = data[attributes[length]].unique()

# Eliminar la columna de clase de la lista de atributos
attributes = attributes.drop(labels = [attributes[length]])

print("Los datos son: ")
print(data)
print("Los atributos son: ")
print(attributes)
print("Las clases son: ")
print(classes)