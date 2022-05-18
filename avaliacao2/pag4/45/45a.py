from sympy import *
import os
import random
os.system("clear")

# Função para construir matrizes
def construirMatriz(linha, coluna):
  M = []
  for i in range(linha):
    linha = []
    for j in range(coluna):
      num = random.randint(-9,9)
      linha.append(num)
    M.append(linha)
  matriz = Matrix(M)
  return matriz
print("MATRIZES 4X4\n")
for i in range(3):

  #
  A = construirMatriz(4,4)
  detA  =A.det()
  detATransp = A.T.det()
  detAOposto = (-1*A).det()
  det2A = (2*A).det()
  det10A = (10*A).det()

  pprint(A)
  print("////////////////////")
  print("Det A = ",detA)
  print("Det A transposto = ",detATransp)
  print("Det -A = ",detAOposto)
  print("Det 2A = ",det2A)
  print("Det 10A = ",det10A)
  print("///////////////////////////////////////////////////////////\n")

