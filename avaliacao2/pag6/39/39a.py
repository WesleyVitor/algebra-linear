from sympy import *
import os

os.system("clear")


A = Matrix([
  [5,1,2,2,0],
  [3,3,2,-1,-12],
  [8,4,4,-5,12],
  [2,1,1,0,-2]
])

pprint(A.rref())

print("\n COMO OS VETORES SÃO UM CONJUNTO LD, E A BASE É FORMADA POR a1,a2 e a4,\n ENTÃO a3 e a5 PODEM SER ESCRITO COMO COMBINAÇÃO LINEAR DAS COLUNAS DA BASE")