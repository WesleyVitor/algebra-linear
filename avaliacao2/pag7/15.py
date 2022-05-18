from sympy import *
import os

os.system("clear")

A = Matrix([
  [1,0,2,2,3],
  [0,1,-2,-1,-1],
  [-2,2,-8,10,-6],
  [3,3,0,3,9]
])

pprint(A.rref())

A.col_del(2)
print("\nBASE PARA FORMAR Col A:")
pprint(A)