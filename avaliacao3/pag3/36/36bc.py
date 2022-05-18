from sympy import *
import os 
import random
os.system("clear")

def normalizarMatriz(A,colunas):
  M = Matrix([])
  for i in range(colunas):
    cI = A[:,i]
    normcI = cI.norm()
    nova_coluna = cI/normcI
    M = M.col_insert(i, nova_coluna)
  return M

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
  
print("\n/// Letra B:\n")
A = Matrix([
    [-6,-3,6,1],
    [-1,2,1,-6],
    [3,6,3,-2],
    [6,-3,6,-1],
    [2,-1,2,3],
    [-3,6,3,2],
    [-2,-1,2,-3],
    [1,2,1,6]
  ])

U = normalizarMatriz(A, 4)
y = construirVetor(8,1)

p = U*U.T*y
print("Vetor p:")
pprint(p)

colA = Matrix([A.columnspace()])
esc = colA.col_insert(4,p).rref()
print("Matriz Escalonada, provando que p faz parte de Col A:")
pprint(esc)

print("\n\n")

z = y-p
print("Vetor z:")
pprint(z)
print("\n")
print("Produto Interno entre z e p:", (z.T*p)[0])

print("\n\n\n")
print("\n/// Letra C:\n")


a1 = A[:,0]
a2 = A[:,1]
a3 = A[:,2]
a4 = A[:,3]

print("z.T*a1:",(z.T*a1)[0])
print("z.T*a2:",(z.T*a2)[0])
print("z.T*a3:",(z.T*a3)[0])
print("z.T*a4:",(z.T*a4)[0])
print("\n Sim, z é ortogonal a cada coluna de A!")










