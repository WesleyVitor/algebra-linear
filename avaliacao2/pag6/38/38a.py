from sympy import *
import os

os.system("clear")

## W FAZ PARTE DE COL A?

A = Matrix([
  [-8,5,-2,0],
  [-5,2,1,-2],
  [10,-8,6,-3],
  [3,-2,1,0]
])

w = Matrix([[1,2,1,0]]).T

baseColA = A.columnspace()
baseColA = Matrix([baseColA])
print("Base para Col A")
pprint(baseColA)
print("\n\n")
escalonada = (baseColA.col_insert(3,w)).rref()
pprint(escalonada)

print("\n w FAZ PARTE DO ESPAÇO DAS COLUNAS DE A! ")
print("x1 =-2\nx2 =-3\nx3 =1")