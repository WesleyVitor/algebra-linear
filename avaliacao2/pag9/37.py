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

espacoColA = A.columnspace()
C = Matrix([])
for i in espacoColA:
  C = C.row_join(i)
R = Matrix(A.rowspace())

print("Matriz C (5x4):")
pprint(C)
print("\n")
print("Matriz R (4x7):")
pprint(R)
print("\n")
print("Matriz CR (5x7):")
CR = C*R
pprint(CR)