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
    for attribute in attributes:
        dataOrd = data.sort_values(by = [attribute, classcolumn])
        resg = dataOrd.iloc[0][classcolumn]
        pos = 0
        for value in dataOrd[classcolumn]:
            if value != resg:
                threshold = dataOrd.iloc[pos - 1][attribute]
                impurityEval2(dataOrd, attribute, threshold, classcolumn)
                resg = value
            pos += 1
    return False

def selectAg(p0,p,attributes):
    # To Do
    return False

def impurityEval2(dataOrd, attribute, threshold, classcolumn):
    n = dataOrd.shape[0]
    # Generar los subconjuntos "<=" y ">"
    data1 = dataOrd.loc[dataOrd[attribute] <= threshold]
    n1 = data1.shape[0]
    data2 = dataOrd.loc[dataOrd[attribute] > threshold]
    n2 = data2.shape[0]
    pi = n1/n * impurityEval1(data1, classcolumn) + n2/n * impurityEval1(data2, classcolumn)    
    return pi

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
    freqclass = freq[0]
    return freqclass

def sameClassC(data, classcolumn):
    if data[classcolumn].nunique() == 1:
        return True
    return False
    

def decisiontree(data, attributes, classes, classcolumn, tree, threshold):
    cj = frequentClass(data, classes, classcolumn)
    if sameClassC(data, classcolumn):
        leafNode(cj)
    elif attributes.length() == 0:
        leafNode(cj)
    else:
        p0 = impurityEval1(data, classcolumn)
        p = []
        p = impurityCalc(attributes, data)
        g = selectAg(p0, p, attributes)
        if (p0 - p[g]) < threshold:
            cj = frequentClass(data, classes, classcolumn)
            leafNode(cj)
        else:
            decisionNode(tree, attributes[g])
            Dsubsets = partitionD(data, attributes[g], g)
            j = 0
            for d in Dsubsets:
                if d.length() != 0:
                    createBranch(attributes[g])
                    j += 1
                    decisiontree(Dsubsets[j], A-A[g], tree[j])
