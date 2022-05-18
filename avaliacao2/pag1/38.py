from sympy import *
import os

os.system("clear")

#
# ALGORITMO PARA DESCOBRIR A BASE DO ESPAÇO DAS COLUNAS E ESPAÇO NULO DA MATRIZ
#

A = Matrix([
  [5,3,2,-6,-8],
  [4,1,3,-8,-7],
  [5,1,4,5,19],
  [-7,-5,-2,8,5]
])
print("BASE PARA O ESPAÇO DAS COLUNAS:",end="\n\n")
pprint(A.columnspace())
print(end="\n\n")
print("BASE PARA O ESPAÇO NULO:",end="\n\n")
pprint(A.nullspace())