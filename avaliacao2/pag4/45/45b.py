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


#
print("MATRIZ 5X5\n")
A = construirMatriz(5,5)
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

#
print("MATRIZ 6X6\n")
B = construirMatriz(6,6)
detB  =B.det()
detBTransp = B.T.det()
detBOposto = (-1*B).det()
det2B = (2*B).det()
det10B = (10*B).det()

pprint(B)
print("////////////////////")
print("Det B = ",detB)
print("Det B transposto = ",detBTransp)
print("Det -B = ",detBOposto)
print("Det 2B = ",det2B)
print("Det 10B = ",det10B)
print("///////////////////////////////////////////////////////////\n")

