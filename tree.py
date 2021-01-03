class Node:
    def __init__(self, value, variables, restriction):
        self.left = None
        self.right = None
        self.value = value
        self.variables = variables
        self.restriction = restriction

def insert(root, node, dir):
    if root is None:
        root = node
    else:
        if(dir):


        