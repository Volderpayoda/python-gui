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