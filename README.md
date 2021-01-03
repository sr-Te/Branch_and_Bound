# Branch_and_Bound
## Consideraciones previas
* La solución de un problema es un UB (uper bound) sólo si todas sus variables son enteras, en caso contrario es un LB (lower bound).
* Un UB es mejor que otro cuando es más pequeño, en caso de un LB es mejor cuando es más grande.
* Un subproblema es un nodo.
## Algoritmo
1. Seleccionamos un subproblema.
2. Si es factible resolvemos el problema mediante simplex, en caso contrario se descarta.
3. Si LB > UB, el subproblema se descarta.
4. Si LB < UB:
    1. Se guarda el mejor LB/UB.
    2. Se crean dos subproblemas, con sus restricciones correspondientes.
        1. Se elige una variable fraccionaria.
        2. Se crean dos subproblemas con las restricciones:
            * xi >= Func.techo(xi) => Nodo derecho
            * xi <= Func.piso(xi) => Nodo izquierdo
    3. Volver al paso 1.
5. Si LB = UB, Nos detenemos.