import numpy as np
import pandas as pd

def impurityEval1(data):
    # To Do
    return False

def impurityCalc(data,attributes): # calcular-impurezas
    # To Do
    return False

def selectAg(p0,p,attributes):
    # To Do
    return False

def impurityEval2():
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
        p0 = impurityEval1(data)
        p = []
        p = impurityCalc(attributes, data)
        g = selectAg(p0, p, attributes)
        if (p0 - p[g]) < threshold:
            cj = frequentClass(data)
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
