from sympy import *

import os

os.system("clear")
print("1° parte")
B = Matrix([
  [-6,8,-9],
  [4,-3,5],
  [-9,7,-8],
  [4,-3,3]
])

pprint(B.rref())
print("\n OS VETORES QUE FORMAM B SÃO LI, ENTÃO ELES FORMAM UMA BASE PARA H\n")

# 2 parte
print("2° parte")
x = Matrix([[4,7,-8,3]]).T

esc = B.col_insert(3,x)


pprint(esc.rref())

print("\n O VETOR X FAZ PARTE DE H\n")

#3 parte
print("3° parte")
print("\n VETOR COORDENADA:")
print(" c1= 3\n c2= 5\n c3= 2")


