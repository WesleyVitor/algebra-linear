from sympy import *
import random
import os

from sympy.solvers.diophantine.diophantine import norm

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

Au = A*u
Av = A*v

print("Tamanhos:")
print("u:",u.norm())
print("Au:",Au.norm())
print("v:",v.norm())
print("Av:",Av.norm())