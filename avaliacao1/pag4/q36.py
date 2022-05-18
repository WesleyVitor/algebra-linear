import random
import sympy
import os
os.system("clear")

print("Matrix 5x6")
#Problema com Matrix 5x6
M1 = []
linha=5
coluna = 6
for i in range(linha):
  linha = []
  for j in range(coluna):
    num = random.random() 
    linha.append(num)	
  M1.append(linha)


matriz_M1 = sympy.Matrix(M1)
sympy.pprint(matriz_M1)

print()
print()
print("Matrix 4x4")
#Problema com Matrix 4x4
M2 = []
linha=coluna = 4
for i in range(linha):
  linha = []
  for j in range(coluna):
    num = random.randint(-9,9) 
    linha.append(num)	
  M2.append(linha)


matriz_M2 = sympy.Matrix(M2)
sympy.pprint(matriz_M2)
