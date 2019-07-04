import numpy as np
import pandas as pd

class Problem: pass

def import_csv(path, sep = ',', lineterminator = '\n', testPer = 0.2):
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

    # Controlar para caracteres no válidos
    try:
        for a in attributes:
            data[a].apply(lambda x: float(x))
    except: 
        raise Exception('El conjunto contiene datos no válidos.')

    # Separar los datos en el conjunto de entrenamiento y el conjunto de prueba
    testData = data.sample(frac = testPer)
    data = data.drop(testData.index)

    # Generar el problema
    problem = Problem()
    problem.data = data
    problem.testData = testData
    problem.attributes = attributes
    problem.classcolumn = classcolumn
    problem.classes = classes
    return problem

    
