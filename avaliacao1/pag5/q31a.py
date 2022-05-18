import sympy
import os
os.system("clear")

A = sympy.Matrix(
  [[4,-1,-1,0,0,0,0,0],
   [-1,4,0,-1,0,0,0,0],
   [-1,0,4,-1,-1,0,0,0],
   [0,-1,-1,4,0,-1,0,0],
   [0,0,-1,0,4,-1,-1,0],
   [0,0,0,-1,-1,4,0,-1],
   [0,0,0,0,-1,0,4,-1],
   [0,0,0,0,0,-1,-1,4]]
)

sympy.pprint(A)
print()
L,U,_ = A.LUdecomposition()

resultado = L*U - A
sympy.pprint(resultado)
print()
print("Deu uma matriz nula")

