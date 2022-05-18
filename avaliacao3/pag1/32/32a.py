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

a1 = A[:,0]
a2 = A[:,1]
a3 = A[:,2]
a4 = A[:,3]

print("Tamanhos:\n")
print("a1:",a1.norm())
print("a2:",a2.norm())
print("a3:",a3.norm())
print("a4:",a4.norm())

print("Produtos Internos:\n")
print("a1.a2:",(a1.T * a2)[0])
print("a1.a3:",(a1.T * a3)[0])
print("a1.a4:",(a1.T * a4)[0])
print("a2.a3:",(a2.T * a3)[0])
print("a2.a4:",(a2.T * a4)[0])
print("a3.a4:",(a3.T * a4)[0])

