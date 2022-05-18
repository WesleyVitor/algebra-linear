from sympy import *
import os
os.system("clear")

# Matrix aumentada com solução não trivial
Aamp = Matrix([[3,-4,10,7,-4,0],
            [-5,-3,-7,-11,15,0],
            [4,3,5,2,1,0],
            [8,-7,23,4,15,0]])
pprint(Aamp)
print("\n\n")

A_reduzida = Aamp.rref()
pprint(A_reduzida)
print("\n\n")

print("******Nova Matriz ")
#Com colunas que me possibilita uma solução trivial
Bamp = Matrix([[3,-4,7,0],
               [-5,-3,-11,0],
               [4,3,2,0],
               [8,-7,4,0]])

pprint(Bamp)
print("\n\n")

B_Reduzida = Bamp.rref()
pprint(B_Reduzida)


