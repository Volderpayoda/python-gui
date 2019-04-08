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