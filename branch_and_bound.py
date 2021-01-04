from tree import *

def feasible(restrictions):
    # restrictions = []
    valids = 0
    for r in restrictions:
        if r:
            valids += 1 
    return valids == len(restrictions)

def simplex():
    return True

def branch_and_bound():
    return True