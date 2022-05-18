from sympy import *
import os

os.system("clear")

#
# ALGORITMO PARA DESCOBRIR A BASE DO ESPAÇO DAS COLUNAS E ESPAÇO NULO DA MATRIZ
#

A = Matrix([
  [15,14],
  [-5,-10],
  [12,13],
  [7,17]
])
x=Matrix([[16,0,11,3]]).T

matrizAmpliada = A.col_insert(2,x)

matrizEscalonada = matrizAmpliada.rref()
pprint(matrizEscalonada)
print()
print("X NÃO PERTENCE AO SPAN DE V1 E V2, POIS 0 != 1")