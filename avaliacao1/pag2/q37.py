from sympy import *
import os
os.system("clear")

Aamp = Matrix([[2,3,5,-5,0],
               [-7,7,0,0,0],
               [-3,4,1,3,0],
               [-9,3,-6,-4,0]])


pprint(Aamp)
print("\n\n")

resultado = Aamp.rref()

pprint(resultado)
print("\n\n")

print("A solução de Ax=0 produz uma solução não trivial\n")
