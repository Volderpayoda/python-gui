import json

class Cargo:
    def __init__(self, nodeType = None, value = None, limit = None, supportCount = None, confidence = None):
        # El tipo del nodo puede ser 'leaf' o 'decision'
        self.type = nodeType
        # Si es un nodo de decisión, el valor es la columna sobre la cual se está decidiendo
        # Si es un nodo hoja, el valor es la clase final 
        self.value = value
        if nodeType == 'decision':
            # Si es un nodo de decisión, se debe indicar el valor con el cual se va a particionar el intervalo.
            self.limit = limit 
        else: 
            # Si es un nodo hoja, se debe indicar el conteo de soporte y la confianza. 
            self.supportCount = supportCount
            self.confidence = confidence
    
    def __str__(self):
        str = ""
        str = str + "nodeType: {0} - ".format(self.type)
        str = str + "value: {0} - ".format(self.value)
        if self.type == 'decision':
            str = str + "limit: {0}".format(self.limit)
        else:
            str = str + "supportCount: {0} - ".format(self.supportCount)
            str = str + "confidence: {0}/{1}".format(self.confidence[0], self.confidence[1])
        return str
    
    def toString(self):
        if self.type == 'decision':
            return self.value + ' : ' + str(self.limit)
        if self.type == 'leaf':
            return self.value + ' : ' + str(self.confidence[0]) + '/' + str(self.confidence[1])


class BinaryTree:
    def __init__(self, cargo = Cargo(), left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return self.show()

    def show(self, sep = '|-'):
        if self.cargo is None:
            return ''
        text = str(self.cargo)
        if self.left is not None:
            text = text + '\n' + sep + self.left.show(sep = sep.rjust(len(sep) + 2))
        if self.right is not None:
            text = text + '\n' + sep + self.right.show(sep = sep.rjust(len(sep) + 2))
        return text

    def stringTree(self, level = 0):
        string = '\t' * level + str(self.cargo) + '\n'
        if self.left is not None:
            string = string + self.left.stringTree(level = level + 1)
        if self.right is not None:
            string = string + self.right.stringTree(level = level + 1)
        return string
    
    def toDict(self):
        if self.cargo.type == 'leaf':
            dic = {'name' : self.cargo.toString()}
            return dic
        if self.cargo.type == 'decision':
            dic = {'name' : self.cargo.toString()}
            dic['children'] = [self.left.toDict(), self.right.toDict()]
        return dic

    def toJson(self):
        dic = self.toDict()
        jsonStr = json.dumps(dic)
        return jsonStr
        
if __name__ == "__main__":
    tree = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4, BinaryTree(5), BinaryTree(6)))
    print(tree)
    print(tree.stringTree())