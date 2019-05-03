import numpy as np
import pandas as pd

class Problem: pass

def import_csv(path, sep = ',', lineterminator = '\n'):
    # Obtener el conjunto de datos
    data = pd.read_csv(filepath_or_buffer = path, sep = sep)

    # Obtener el conjunto de atributos
    attributes = data.columns

    # Obtener el conjunto de clases
    length = attributes.size - 1
    classcolumn = attributes[length]
    classes = data[attributes[length]].unique()

    # Eliminar la columna de clase de la lista de atributos
    attributes = attributes.drop(labels = [attributes[length]])

    problem = Problem()
    problem.data = data
    problem.attributes = attributes
    problem.classcolumn = classcolumn
    problem.classes = classes
    return problem
'''
    problem = {
        "data": data,
        "attributes": attributes,
        "classcolumn": classcolumn,
        "classes": classes
    }
'''

    
