from sympy import *
import os

os.system("clear")

A = Matrix([
  [-3,3,0,6,-6],
  [2,0,2,-2,3],
  [6,-9,-4,-14,0],
  [0,0,0,0,-1],
  [-7,6,-1,13,0]
])

pprint(A.rref())

A.col_del(3)
print("\nBASE PARA FORMAR Col A:")
pprint(A)