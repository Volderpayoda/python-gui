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

def gainCalc(p0, p):
    p['gain'] = p['impurity'].apply(lambda x: p0 - x)
    return p

def gainRatioCalc(p, data):
    d = (data.shape)[0] #calcula la cantidad de filas de d
    aux = []
    i = 0

    while i < (p.shape)[0]:
        #seleccion de elementos para partitionD
        a = p.iloc[i][0] #seleccion del atributo
        v = p.iloc[i][1] #seleccion del valor
        g = p.iloc[i][3] #seleccion de la ganancia de información

        #llamado a partitionD
        d1,d2 = partitionD(data, a, v)

        #calculo de tamaño de particiones
        shapeD1 = (d1.shape)[0]
        shapeD2 = (d2.shape)[0]

        # Calcular la primera parte del denominador  
        if shapeD1 == 0: 
            den1 = 0
        else:
            den1 = ((shapeD1)/d)*math.log((shapeD1/d),2)

        # Calcular la segunda parte del denominador

        if shapeD2 == 0:
            den2 = 0
        else:
            den2 = ((shapeD2)/d)*math.log((shapeD2/d),2)

        #calcular el gainRatio
        if g == 0:
            gainRatio = 0
        else:
            gainRatio = g/(-(den1+den2))

        i +=1
        aux.append(gainRatio)  
    npaux = np.array(aux)
    p['gainRatio'] = npaux
    return p 

def selectAg(p, gainFunc):
    p = p.sort_values([gainFunc,'attribute'], ascending = [0,1])
    Ag = p.iloc[0]
    return Ag['attribute'], Ag['value'], Ag['gain']

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

def frequentClass(data, classcolumn):
    freq = data[classcolumn].value_counts()
    max = freq.max()
    values = np.array(freq.tolist())
    keys = np.array(freq.index.tolist())
    order = np.lexsort((keys, values))
    for i in order:
        if values[i] == max:
            return keys[i]

def sameClassC(data, classcolumn):
    if data[classcolumn].nunique() == 1:
        return True
    return False
    
def decisionTree(data, attributes, classes, classcolumn, tree, threshold, gainFunc):
    # Calcula la clase más frequente
    cj = frequentClass(data, classcolumn)
    # Evaluamos para los casos base
    if sameClassC(data, classcolumn):
        leafNode(cj, tree, data, classcolumn)
        return tree
    else:
        # El conjunto no es puro
        p0 = impurityEval1(data, classcolumn)
        # Calculamos las entropías para todas las particiones posibles de cada atributo
        p = impurityCalc(data, attributes, classcolumn)
        # Calculamos la ganancia y la tasa de ganancia para todas las particiones posibles de cada atributo
        p = gainCalc(p0, p)
        if gainFunc == 'gainRatio':
            p = gainRatioCalc(p, data)
        a, val, gain = selectAg(p, gainFunc)
        if gain < threshold:
            leafNode(cj, tree, data, classcolumn)
            return tree
        else:
            # Caso recursivo
            decisionNode(tree, a, val)
            data1, data2 = partitionD(data, a, val)
            if data1.shape[0] != 0:
                tree.left = decisionTree(data1, attributes, classes, classcolumn, bt.BinaryTree(), threshold, gainFunc)
            if data2.shape[0] != 0:
                tree.right = decisionTree(data2, attributes, classes, classcolumn, bt.BinaryTree(), threshold, gainFunc)
    return tree