import numpy as np
import pandas as pd

def impurityEval1(Data):
    # To Do

def impurityCalc(Data,Attributes): # calcular-impurezas
    # To Do

def selectAg(p0,p,Attributes):
    # To Do

def impurityEval2():
    # To Do

def leafNode(cj):
    # To Do

def createBranch(valueAg):
    # To Do    

def decisionNode(Tree, valueAg):
    # To Do

def partitionD(Data, valueAg, g):
    # To Do

def frequentClass(Data):
    # To Do

def sameClassC(Data):
    # To Do

def decisionTree(Data, Attributes, Tree, threshold):
    # To Do 
    cj = frequentClass(Data)
    if sameClassC(Data):
        leafNode(cj)
    elif Attributes.length() == 0:
        leafNode(cj)
    else:
        p0 = impurityEval1(Data)
        p = []
        p = impurityCalc(Attributes, Data)
        g = selectAg(p0, p, Attributes)
        if (p0 - p[g]) < threshold:
            cj = frequentClass(Data)
            leafNode(cj)
        else:
            decisionNode(Tree, Attributes[g])
            Dsubsets = partitionD(Data, Attributes[g], g)
            j = 0
            for d in Dsubsets:
                if d.length() != 0:
                    createBranch(Attributes[g])
                    j += 1
                    decisionTree(Dsubsets[j], A-A[g], Tree[j])
