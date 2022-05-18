from sympy import *
import os
os.system("clear")

M1 = Matrix([
  [1,1,1],
  [1,2,2],
  [1,2,3]
])
det1 = M1.det()
escalonada1 = M1.rref()
print(det1)
pprint(escalonada1)
print("\n\n")
M2 = Matrix([
  [1,1,1,1],
  [1,2,2,2],
  [1,2,3,3],
  [1,2,3,4]
])
det2 = M2.det()
escalonada2 = M2.rref()
print(det2)
pprint(escalonada2)
print("\n\n")

M3 = Matrix([
  [1,1,1,1,1],
  [1,2,2,2,2],
  [1,2,3,3,3],
  [1,2,3,4,4],
  [1,2,3,4,5]
])
det3 = M3.det()
escalonada3 = M3.rref()
print(det3)
pprint(escalonada3)
print("\n\n")
print("\n O VALOR DO DETERMINANTE DAS PRÍXIMAS MATRIZES QUE SEGUEM ESSE ESTILO SERÁ 1")