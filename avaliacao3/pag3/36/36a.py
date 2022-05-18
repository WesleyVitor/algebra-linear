from sympy import *
import os 

os.system("clear")

def normalizarMatriz(A,colunas):
  M = Matrix([])
  for i in range(colunas):
    cI = A[:,i]
    normcI = cI.norm()
    nova_coluna = cI/normcI
    M = M.col_insert(i, nova_coluna)
  return M

  

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

UtU = U.T*U
UUt = U*U.T

print("UtU:\n")
print("Matriz Identidade")
pprint(UtU)
print("UUt:\n")
pprint(UUt)

