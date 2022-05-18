from sympy import *
import os

os.system("clear")

A = Matrix([
  [5,1],
  [3,3],
  [8,4]
])

v3 =-1 * Matrix([[2,-1,5]]).T
v4 =-1 * Matrix([[0,-12,-28]]).T
B = A.col_insert(2,v3)
B = B.col_insert(3,v4)
escalonaB0 = B.col_insert(4,zeros(3,1))

pprint(escalonaB0.rref())
print("\n c1= 10/3\n c2= -26/3\n c3= 4\n c4= Free")