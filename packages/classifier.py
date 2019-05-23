class Classifier:
    def __init__(self, attributes):
        self.attributes = attributes
    
    def classifyData(self, tree, data):
        if tree.cargo.type == 'leaf':
            return tree.cargo.value
        else:
            if tree.cargo.value == self.attributes[0]:
                if data[0] <= tree.cargo.limit:
                    return self.classifyData(tree.left, data)
                else:
                    return self.classifyData(tree.right, data)
            if tree.cargo.value == self.attributes[1]:
                if data[1] <= tree.cargo.limit:
                    return self.classifyData(tree.left, data)
                else:
                    return self.classifyData(tree.right, data)
    
    def classifyDataFrame(self, tree, trainData):
        nTest = (trainData.shape)[0] #calcula la cantidad de filas de d
        cont = 0
        i = 0
        while i < nTest:
            #seleccion de elementos para partitionD
            a1 = trainData.iloc[i][0]
            a2 = trainData.iloc[i][1]
            c = trainData.iloc[i][2]
            arr = [a1, a2]
            output = self.classifyData(tree, arr)
            if c == output:
                cont = cont + 1
            i = i + 1
        accuracy = cont / nTest
        return accuracy