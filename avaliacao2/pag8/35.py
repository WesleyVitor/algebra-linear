from sympy import *
import os

os.system("clear")

H = Matrix([
  [11,14],
  [-5,-8],
  [10,13],
  [7,10]
])

x = Matrix([[19,-13,18,15]]).T

escalona = H.col_insert(2,x)

pprint(escalona.rref())

print("\n SIM, O VETOR X FAZ PARTE DO SPAN DE H!\n")
print("Vetor cordenada de x em relação a Beta:")
print("c1= -5/3\nc2= 8/3")
