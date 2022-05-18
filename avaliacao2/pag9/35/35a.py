from sympy import *
import os

os.system("clear")

A = Matrix([
  [7,-9,-4,5,3,-3,-7],
  [-4,6,7,-2,-6,-5,5],
  [5,-7,-6,5,-6,2,8],
  [-3,5,8,-1,-7,-4,8],
  [6,-8,-5,4,4,9,3]
])
print("Matriz A:")
pprint(A)
print("\n")
C = A.columnspace()
print("Base para Col A:")
pprint(C)
print("\n")
N = A.nullspace()
print("Base para Nul A:")
pprint(N)
print("\n")
R = A.rowspace()
print("Base para Row A:")
pprint(Matrix(R))


