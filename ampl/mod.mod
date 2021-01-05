set M := {1,2,3,4,5};
set F := {1,2};
set I := {1,2,3,4};

param D{M};
param CapMin{I,F};
param CapMax{I,F};
param Costo{I,F};
param P;

var x{M,I,F}, >= 0;
var y{M}, binary;
var w{M,I,F}, binary;

minimize z: sum{m in M, f in F, i in I}(x[m,i,f]*Costo[i,f]) + sum{m in M}(y[m]*P);

#Demanda
subject to R5{m in M}: sum{f in F, i in I}(x[m,i,f])/D[m] >= 1 - y[m];

#Capacidad
subject to R2{m in M, f in F, i in I}: x[m,i,f] <= w[m,i,f]*CapMax[i,f];
subject to R3{m in M, f in F, i in I}: x[m,i,f] >= w[m,i,f]*CapMin[i,f];

#Funcionamiento
subject to R4{m in M,i in I}: sum{f in F}(w[m,i,f]) <= 1;