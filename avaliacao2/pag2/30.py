from sympy import *
import os

os.system("clear")

#
# ALGORITMO PARA DESCOBRIR A BASE DO ESPAÇO DAS COLUNAS E ESPAÇO NULO DA MATRIZ
#

A = Matrix([
  [-6,8,-9],
  [3,0,4],
  [-9,7,-8],
  [4,-3,3]
])
x=Matrix([[11,-2,17,-8]]).T

matrizAmpliada = A.col_insert(3,x)

matrizEscalonada = matrizAmpliada.rref()
pprint(matrizEscalonada)
print()
print("1. Todos as colunas tem posição pivó, então B será uma base para a H\n")
print("2. O vetor x está em H, pois ele pode ser escrito como combinação linear das colunas da Base\n")
print("3. O vetor coordenada em relação a Base é:")
pprint(Matrix([[-2,1,1]]).T)