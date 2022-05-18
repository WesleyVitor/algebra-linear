from sympy import *
import os
os.system("clear")

# Matrix aumentada com solução não trivial
Aamp = Matrix([[12,10,-6,8,4,-14,0],
               [-7,-6,4,-5,-7,9,0],
               [9,9,-9,9,9,-18,0],
               [-4,-3,-1,0,-8,1,0],
               [8,7,-5,6,1,-11,0]])
pprint(Aamp)
print("\n\n")

A_reduzida = Aamp.rref()
pprint(A_reduzida)
print("\n\n")

print("******Nova Matriz ")
#Com colunas que me possibilita uma solução trivial
Bamp = Matrix([[12,10,-6,4,0],
               [-7,-6,4,-7,0],
               [9,9,-9,9,0],
               [-4,-3,-1,-8,0],
               [8,7,-5,1,0]])

pprint(Bamp)
print("\n\n")

B_reduzida = Bamp.rref()
pprint(B_reduzida)

