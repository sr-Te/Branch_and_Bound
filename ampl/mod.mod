set M := {1,2,3,4,5};
set F := {1,2};
set I := {1,2,3,4};

param D{M};
param CapMin{I,F};
param CapMax{I,F};
param Costo{I,F};
param P;

var x{M,F,I}, >= 0;
var y{M}, binary;

minimize z: sum{m in M}(sum{f in F}(sum{i in I}(x[m,f,i]*Costo[i,f] + y[m]*P)));

subject to R1{m in M}: sum{f in F}(sum{i in I}(x[m,f,i])) <= D[m];
subject to R3{f in F, i in I}: sum{m in M}(x[m,f,i]) <= CapMax[i,f];
subject to R4{f in F, i in I}: sum{m in M}(x[m,f,i]) >= CapMin[i,f];
