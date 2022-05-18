import sympy
import os
os.system("clear")

#Ax=0
Aamp = sympy.Matrix(
  [[4,-7,3,7,5,0],
   [6,-8,5,12,-8,0],
   [-7,10,-8,-9,14,0],
   [3,-5,4,2,-6,0],
   [-5,6,-6,-7,3,0]]
)
sympy.pprint(Aamp)
print()
resultado = Aamp.rref()
sympy.pprint(resultado)
print()
print("Não é sobrejetora pois a solução Ax=0 não é trivial, assim as colunas de A não forma todo o R5")


