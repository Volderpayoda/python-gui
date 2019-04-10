import numpy as np
import pandas as pd

def import_csv(path, sep = ','):
    # Obtener el conjunto de datos
    data = pd.read_csv(filepath_or_buffer = path, sep = sep)

    # Obtener el conjunto de atributos
    attributes = data.columns

    # Obtener el conjunto de clases
    length = attributes.size - 1
    classes = data[attributes[length]].unique()

    # Eliminar la columna de clase de la lista de atributos
    attributes = attributes.drop(labels = [attributes[length]])

    dictionary = {
        "data": data,
        "attributes": attributes,
        "classes": classes
    }

    return dictionary
