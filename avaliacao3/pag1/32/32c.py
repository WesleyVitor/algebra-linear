
from sympy import *
import random
import os


os.system("clear")

def construirVetor(linha, coluna):
  M = []
  for i in range(linha):
    linha = []
    for j in range(coluna):
      num = random.randint(0,100)
      linha.append(num)
    M.append(linha)
  matriz = Matrix(M)
  return matriz

A = Matrix([
  [.5,.5,.5,.5],
  [.5,.5,-.5,-.5],
  [.5,-.5, 5,-.5],
  [.5,-.5,-.5,.5]
])

v = construirVetor(4,1)
u = construirVetor(4,1)

uv = (u.T*v)[0]
normaUV = u.norm()*v.norm()


Au = A*u
Av = A*v


AuAv = (Au.T*Av)[0]
normaAuAv = Au.norm()*Av.norm()

cossenoA1= uv/normaUV
cossenoA2=AuAv/normaAuAv
print("ângulo entre u e v:",cossenoA1)
print("ângulo entre Au e Av:",cossenoA2)
