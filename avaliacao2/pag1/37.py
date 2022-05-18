from sympy import *
import os

os.system("clear")

#
# ALGORITMO PARA DESCOBRIR A BASE DO ESPAÇO DAS COLUNAS E ESPAÇO NULO DA MATRIZ
#

A = Matrix([
  [3,-5,0,-1,3],
  [-7,9,-4,9,-11],
  [-5,7,-2,5,-7],
  [3,-7,-3,4,0]
])
print("BASE PARA O ESPAÇO DAS COLUNAS:",end="\n\n")
pprint(A.columnspace())
print(end="\n\n")
print("BASE PARA O ESPAÇO NULO:",end="\n\n")
pprint(A.nullspace())