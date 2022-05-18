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
      num = random.randint(0,100)
      linha.append(num)
    M.append(linha)
  matriz = Matrix(M)
  return matriz

J = construirMatriz(6,4)
K = construirMatriz(4,7)
A = J*K

print("Matriz A:")
pprint(A)
print("\n")
C = A.columnspace()
print("Base para Col A:")
pprint(C)
print("\n")
N = A.nullspace()
print("Base para Nul A:")
pprint(N)
print("\n")
R = A.rowspace()
print("Base para Row A:")
pprint(Matrix(R))



