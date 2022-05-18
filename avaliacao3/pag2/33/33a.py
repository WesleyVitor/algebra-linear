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

x1 = construirVetor(4,1)
y1 = construirVetor(4,1)
v = construirVetor(4,1)


print("1° Equação:\n")

res = ((x1.T * v)[0]/(v.T * v)[0])*v

print("Resultado:")
pprint(res)

print("2° Equação:\n")

res = ((y1.T*v)[0]/(v.T*v)[0])*v

print("Resultado:")
pprint(res)

print("3° Equação:\n")

res = (((x1+y1).T*v)[0]/(v.T*v)[0])*v

print("Resultado:")
pprint(res)

print("4° Equação:\n")

res = (((10*x1).T*v)[0]/(v.T*v)[0])*v

print("Resultado:")
pprint(res)






