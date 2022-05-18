from sympy import *
import os
os.system("clear")

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

Bamp = Matrix([[12,10,-6,4,0],
               [-7,-6,4,-7,0],
               [9,9,-9,9,0],
               [-4,-3,-1,-8,0],
               [8,7,-5,1,0]])

pprint(Bamp)
print("\n\n")
B_reduzida = Bamp.rref()
pprint(B_reduzida)
print("Solução:")
print()
print("Para que Bx=0 tenha apenas a solução trivial \n Foi necessário construir B com os vetores de A que produzir uma solução trivial")