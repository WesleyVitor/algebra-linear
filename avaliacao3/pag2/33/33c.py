from sympy import *
import os
import random

os.system("clear")

def construirVetor(linha, coluna):
  M = []
  for i in range(linha):
    linha = []
    for j in range(coluna):
      num = random.randint(1,100)
      linha.append(num)
    M.append(linha)
  matriz = Matrix(M)
  return matriz

x = construirVetor(4,1)
v = construirVetor(4,1)

res = ((x.T*v)[0]/(v.T*v)[0])*v


print("Resultado:")
pprint(res)


