from amplpy import AMPL, Environment
from tree import *

amplPATH = 'C:\\Users\\jose_\\Documents\\USM\\USM\\2020-2\\GIO\\tareas\\Tarea1\\ampl_mswin64'
ampl = AMPL(Environment(amplPATH))

def feasible(restrictions):
    # restrictions = []
    valids = 0
    for r in restrictions:
        if r:
            valids += 1 
    return valids == len(restrictions)

def simplex():
    print("-------------------------------")
    print("Comenzando algoritmo simplex")
    print("-------------------------------")

    # Interpret the two files
    print("leyendo mod.mod...")
    ampl.read('ampl/mod.mod')

    print("leyendo dat.dat...")
    ampl.readData('dat.dat')

    print("resolviendo el problema...")
    ampl.solve()

    # Results
    z = ampl.getObjective('total_cost')
    variables = ampl.getVariables
    print("\n Resultados:")
    print("fo: ", z)
    print("variables: ", variables)
    return z, variables

def branch_and_bound():
    z, variables = simplex()
    return True