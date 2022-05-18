import sympy
import os
os.system("clear")

#Ax=0
Aamp = sympy.Matrix(
  [[9,43,5,6,-1,0],
   [14,15,-7,-5,4,0],
   [-8,-6,12,-5,-9,0],
   [-5,-6,-4,9,8,0],
   [13,14,15,3,11,0]]
)
sympy.pprint(Aamp)
print()
resultado = Aamp.rref()
sympy.pprint(resultado)
print()
print("É sobrejetora pois a solução Ax=0 é trivial, assim as colunas de A forma todo o R5")


