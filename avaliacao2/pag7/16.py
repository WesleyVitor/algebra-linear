from sympy import *
import os

os.system("clear")

A = Matrix([
  [1,-2,3,5,2],
  [0,0,-1,-3,-1],
  [0,0,1,3,1],
  [1,2,-1,-4,0]
])

pprint(A.rref())

A.col_del(3)
A.col_del(3)
print("\nBASE PARA FORMAR Col A:")
pprint(A)