import sympy
import os
os.system("clear")

#Ax=0
Aamp = sympy.Matrix(
  [[-5,6,-5,-6,0],
   [8,3,-3,8,0],
   [2,9,5,-12,0],
   [-3,2,7,-12,0]]
)
sympy.pprint(Aamp)
print()
resultado = Aamp.rref()
sympy.pprint(resultado)
print()
print("Não é injetora pois a solução Ax=0 não é trivial")


