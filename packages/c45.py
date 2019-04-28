import numpy as np
import pandas as pd
import math
import packages.binaryTree as bt

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
            imp = impurityEval2(data, a, classcolumn, val)
            d = pd.DataFrame([[a, val, imp]], columns = ['attribute', 'value', 'impurity'])
            p = p.append(d, ignore_index = True)
    return p.sort_values(['impurity','attribute'], ascending = [1,1])

def impurityEval2(data, a, classcolumn, val):
    # Particionar el conjunto data en todos los subconjuntos
    data1, data2 = partitionD(data, a, val)
    # Calcular la impureza de cada subconjunto
    n1 = data1.shape[0]
    n2 = data2.shape[0]
    imp1 = impurityEval1(data1, classcolumn)
    ## Control para el último corte
    if n2 == 0:
        imp2 = 0
    else: 
        imp2 = impurityEval1(data2, classcolumn)
    # Calcular la impureza total
    n = data.shape[0]
    imp = ((n1/n) * imp1) + ((n2/n) * imp2)
    # Retorna la impureza total
    return imp

def gain(p0, p1):
    return p0 - p1

# def gainRatio(p0, p1):
   
def selectAg(p):
    Ag = p.iloc[0]
    return Ag['attribute'], Ag['value'], Ag['impurity']

def leafNode(cj, tree, data, classcolumn):
    tree.cargo = bt.Cargo()
    # Se indica que el nodo es de tipo hoja
    tree.cargo.type = 'leaf'
    # Se asigna el valor de la clase
    tree.cargo.value = cj
    # Calcular y asignar el supportCount
    tree.cargo.supportCount = data.loc[data[classcolumn] == cj].shape[0]    # Calcular y asignar la confianza
    # Calcular y asignar la confianza
    tree.cargo.confidence = [tree.cargo.supportCount, data.shape[0]]
    return False
'''
def createBranch(valueAg):
    # To Do    
    return False
'''
def decisionNode(tree, attribute, value):
    tree.cargo = bt.Cargo()
    # Indicar que es un nodo de decisión
    tree.cargo.type = 'decision'
    # Indicar sobre cual atributo se está decidiendo
    tree.cargo.value = attribute
    # Indicar el punto de corte
    tree.cargo.limit = value
    return False

def partitionD(data, attribute, val):
    data1 = data.loc[data[attribute] <= val]
    data2 = data.loc[data[attribute] > val]
    return (data1, data2)

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
    
def decisionTree(data, attributes, classes, classcolumn, tree, threshold):
    # Calcula la clase más frequente
    cj = frequentClass(data, classes, classcolumn)
    # Evaluamos para los casos base
    if sameClassC(data, classcolumn):
        leafNode(cj, tree, data, classcolumn)
        return tree
    # Deshabilitamos esta parte ya que nunca se remueven atributos de la lista
    # elif attributes.length() == 0:
    #    leafNode(cj)
    else:
        # El conjunto no es puro
        p0 = impurityEval1(data, classcolumn)
        # Calculamos las entropías para todas las particiones posibles de cada atributo
        p = impurityCalc(data, attributes, classcolumn)
        a, val, imp = selectAg(p)
        if (p0 - imp) < threshold:
            cj = frequentClass(data, classes, classcolumn)
            leafNode(cj, tree, data, classcolumn)
            return tree
        else:
            # Caso recursivo
            decisionNode(tree, a, val)
            data1, data2 = partitionD(data, a, val)
            if data1.shape[0] != 0:
                # createBranch(a)
                tree.left = decisionTree(data1, attributes, classes, classcolumn, bt.BinaryTree(), threshold)
            if data2.shape[0] != 0:
                # createBranch(a)
                tree.right = decisionTree(data2, attributes, classes, classcolumn, bt.BinaryTree(), threshold)
    return tree