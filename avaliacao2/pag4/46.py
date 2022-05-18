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
print("MATRIZ 4X4\n")

#
A = construirMatriz(4,4)
detA  =A.det()
if(detA != 0):
  detAInv = A.inv().det()


  pprint(A)
  print("////////////////////")
  print("Det A = ",detA)
  print("Det Inverso de A = ",detAInv)
  print("///////////////////////////////////////////////////////////\n")

#
print("MATRIZ 5X5\n")
B = construirMatriz(5,5)
detB  =B.det()
if(detB != 0):
  detBInv = B.inv().det()


  pprint(B)
  print("////////////////////")
  print("Det B = ",detB)
  print("Det Inverso de B = ",detBInv)
  print("///////////////////////////////////////////////////////////\n")

#
print("MATRIZ 6X6\n")
C = construirMatriz(6,6)
detC  =C.det()
if(detC != 0):
  detCInv = C.inv().det()


  pprint(C)
  print("////////////////////")
  print("Det C = ",detC)
  print("Det Inverso de C = ",detCInv)
  print("///////////////////////////////////////////////////////////\n")




