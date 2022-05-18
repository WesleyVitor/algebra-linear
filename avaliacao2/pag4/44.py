from sympy import *
import random
# Função para construir matrizes
def construirMatriz(linha, coluna):
  M = []
  for i in range(linha):
    linha = []
    for j in range(coluna):
      num = random.randint(0,100)
      linha.append(num)
    M.append(linha)
  matriz = Matrix(M)
  return matriz

for i in range(4):
  A = construirMatriz(3,3)
  B = construirMatriz(3,3)
  detAB = (A*B).det()
  detA = A.det()
  detB = B.det()
  print("det AB:",detAB)
  print("det A * det B:",detA*detB)
  print(end="\n\n")