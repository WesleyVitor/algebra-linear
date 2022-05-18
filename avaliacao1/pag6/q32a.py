import sympy
import os

from sympy.deprecated.class_registry import C
os.system("clear")


C=1
K = 1+2*C
A = sympy.Matrix(
  [[K,-C,0,0],
   [-C,K,-C,0],
   [0,-C,K,-C],
   [0,0,-C,K]]
)

L,U,_ = A.LUdecomposition()
print("L:")
sympy.pprint(L)
print()
print("U:")
sympy.pprint(U)