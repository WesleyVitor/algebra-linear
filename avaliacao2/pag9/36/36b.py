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

C = A.columnspace()
N = A.nullspace()
R = Matrix(A.rowspace())

print("Base para Nul A Transposto:")
M = A.T.nullspace()
pprint(M)
print("\n")

print("\n Matriz S:")
S = Matrix([])
S = S.row_join(R.T)
for i in N:
  S = S.row_join(i)
pprint(S)

print("\n Matriz T:")
T = Matrix([])
for i in C:
  T = T.row_join(i)
T = T.row_join(M[0])
pprint(T)
print("\n")
pprint(T.rref())
print("\n Não, S E T SÃO MATRIZES NÃO INVERSÍVEIS! PORQUE A QUANTIDADE LINHAS DE T É DIFERENTE DO NÚMERO DE PIVÓS\n")
