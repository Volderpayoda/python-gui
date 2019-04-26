import numpy as np
import pandas as pd
import math

def impurityEval1(data, classcolumn):
    # Calcula la entropía del conjunto data
    p0 = 0
    n = data.shape[0]
    freqs = data[classcolumn].value_counts()
    for f in freqs:
        p0 += - (f/n) * math.log((f/n), 2)
    return p0

def impurityCalc(data, attributes, classcolumn): # calcular-impurezas
    p = pd.DataFrame(columns = ['attribute', 'value', 'impurity'])
    for a in attributes:
        valOrd = np.sort(data[a].unique()) # Arreglo que contiene los valores únicos y ordenados del atributo
        for val in valOrd:
            # imp = impurityEval2(data, a, classcolumn, val)
            imp = 1
            d = pd.DataFrame([[a, val, imp]], columns = ['attribute', 'value', 'impurity'])
            p = p.append(d, ignore_index = True)
    return p

def impurityEval2(data, a, classcolumn, val):
    pass

def selectAg(p0,p,attributes):
    # To Do
    return False

def leafNode(cj):
    # To Do
    return False

def createBranch(valueAg):
    # To Do    
    return False

def decisionNode(tree, valueAg):
    # To Do
    return False

def partitionD(data, valueAg, g):
    # To Do
    return False

def frequentClass(data, classes, classcolumn):
    freq = data[classcolumn].value_counts()
    freq = freq.index.tolist()
    # TODO Ordenar lexicograficamente las clases antes de emitir
    freqclass = freq[0]
    return freqclass

def sameClassC(data, classcolumn):
    if data[classcolumn].nunique() == 1:
        return True
    return False
    
def decisiontree(data, attributes, classes, classcolumn, tree, threshold):
    # Calcula la clase más frequente
    cj = frequentClass(data, classes, classcolumn)
    # Evaluamos para los casos base
    if sameClassC(data, classcolumn):
        leafNode(cj)
    # Deshabilitamos esta parte ya que nunca se remueven atributos de la lista
    # elif attributes.length() == 0:
    #    leafNode(cj)
    else:
        # El conjunto no es puro
        p0 = impurityEval1(data, classcolumn)
        # Calculamos las entropías para todas las particiones posibles de cada atributo
        p = impurityCalc(attributes, data)
        g = selectAg(p0, p, attributes)
        if (p0 - p[g]) < threshold:
            cj = frequentClass(data, classes, classcolumn)
            leafNode(cj)
        else:
            # Caso recursivo
            decisionNode(tree, attributes[g])
            Dsubsets = partitionD(data, attributes[g], g)
            j = 0
            for d in Dsubsets:
                if d.length() != 0:
                    createBranch(attributes[g])
                    j += 1
                    decisiontree(Dsubsets[j], A-A[g], tree[j])
