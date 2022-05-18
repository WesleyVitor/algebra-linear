from sympy import *
import os

os.system("clear")

## W FAZ PARTE DE NUL A?

A = Matrix([
  [-8,5,-2,0],
  [-5,2,1,-2],
  [10,-8,6,-3],
  [3,-2,1,0]
])

w = Matrix([[1,2,1,0]]).T

baseNulA = A.nullspace()
baseNulA = Matrix([baseNulA])
print("Base para Nul A")
pprint(baseNulA)
print("\n\n")
escalonada = (baseNulA.col_insert(1,w)).rref()
pprint(escalonada)

print("\n w FAZ PARTE DO ESPAÇO NULO DE A! ")
print("x1 =1")