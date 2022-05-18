import sympy
import os
os.system("clear")

#Ax=0
Aamp = sympy.Matrix(
  [[7,5,9,-9,0],
   [5,6,4,-4,0],
   [4,8,0,7,0],
   [-6,-6,6,5,0]]
)
sympy.pprint(Aamp)
print()
resultado = Aamp.rref()
sympy.pprint(resultado)
print()
print("É injetora pois a solução Ax=0 é trivial")


