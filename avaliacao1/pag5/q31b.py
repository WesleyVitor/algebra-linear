import sympy
import os

os.system("clear")

A = sympy.Matrix(
  [[4,-1,-1,0,0,0,0,0],
   [-1,4,0,-1,0,0,0,0],
   [-1,0,4,-1,-1,0,0,0],
   [0,-1,-1,4,0,-1,0,0],
   [0,0,-1,0,4,-1,-1,0],
   [0,0,0,-1,-1,4,0,-1],
   [0,0,0,0,-1,0,4,-1],
   [0,0,0,0,0,-1,-1,4]]
)
# Fatoração LU
L,U,_ = A.LUdecomposition()
print("Ax=b")
print()
print("(L*(U*x)=b")
print()
print("L*y=b")

b = [5,15,0,10,0,10,20,30]

#inserir vetor b para criar uma matriz ampliada
LBampliado = L.col_insert(8,sympy.Matrix(b))

#Matriz reduzida
y = LBampliado.rref()

#Vetor y
y = y[0].col(-1)
print("U*x=y")

#inserir vetor y para criar uma matriz ampliada
UYampliado = U.col_insert(8,sympy.Matrix(y))

#Matriz reduzida
x = UYampliado.rref()

#Vetor x
x = x[0].col(-1)

print("Vetor x")
sympy.pprint(x)


