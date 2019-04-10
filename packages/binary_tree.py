class BinaryTree:
    def __init__(self, cargo, left = None, right = None):
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
            text = text + '\n' + sep + self.right.show(sep= sep.rjust(len(sep) + 2))
        return text

class Cargo:
    def __init__(self, node_type, value, threshold):
        # El tipo del nodo puede ser 'leaf' o 'decision'
        self.type = node_type
        # Si es un nodo de decisión, el valor es la columna sobre la cual se está decidiendo
        # Si es un nodo hoja, el valor es la clase final 
        self.value = value
        if node_type == 'decision':
            # Si es un nodo de decisión, se debe indicar el valor con el cual se va a particionar el intervalo.
            self.limit = threshold 

        

if __name__ == "__main__":
    tree = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4, BinaryTree(5), BinaryTree(6)))
    print(tree)