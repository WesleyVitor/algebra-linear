from sympy import *
import os

os.system("clear")

A = Matrix([
  [-6,3,-27,-33,-13],
  [6,-5,25,28,14],
  [8,-6,34,38,18],
  [12,-10,50,41,23],
  [14,-21,49,29,33]
])

N = A.nullspace()
R = Matrix(A.rowspace()).T
print("Matrix nul A:")
pprint(N)
print("\n")
print("Matrix row A:")
pprint(R)

print("\nResultado: A soma das quantidades de vetores é igual ao número de colunas de A")