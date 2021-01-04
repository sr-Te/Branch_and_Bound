class Node:
    def __init__(self, type, value, variables, restriction):
        self.left = None
        self.right = None
        self.type = type
        self.value = value
        self.variables = variables
        self.restriction = restriction

    def insert(self, node, dir):
        if dir == 'right':
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node, 'right')
        else:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node, 'left') 

        