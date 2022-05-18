from sympy import *
import os

os.system("clear")

A = Matrix([
  [2,4,-2,8,-8],
  [0,0,-4,4,4],
  [-4,2,0,8,0],
  [-6,-4,1,-3,0],
  [0,4,-7,15,1]
])

pprint(A.rref())

A.col_del(3)
print("\nBASE PARA FORMAR Col A:")
pprint(A)