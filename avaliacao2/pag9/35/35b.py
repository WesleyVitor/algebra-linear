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

C = A.columnspace()
N = A.nullspace()
R = Matrix(A.rowspace())

print("Base para Nul A Transposto:")
M = A.T.nullspace()
pprint(M)
print("\n")

print("\n Matriz S:")
S = Matrix([])
S = S.row_join(R.T)
for i in N:
  S = S.row_join(i)
pprint(S)

print("\n Matriz T:")
T = Matrix([])
for i in C:
  T = T.row_join(i)
T = T.row_join(M[0])
pprint(T)
print("\n")
print("Determinante de S:%.2f"%(S.det()))
print("Determinante de T:%.2f"%(T.det()))
print("\n SIM, S E T SÃO MATRIZES INVERSÍVEIS!\n")
