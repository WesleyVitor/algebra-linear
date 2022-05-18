from sympy import *
import os
os.system("clear")

Bamp = Matrix([[3,4,-7,0,0],
               [5,-8,7,4,0],
               [6,-8,6,4,0],
               [9,-7,-2,0,0]])


pprint(Bamp)
print("\n\n")

resultado = Bamp.rref()

pprint(resultado)
print("\n\n")

print("A solução de Bx=0 produz uma solução não trivial\n")
