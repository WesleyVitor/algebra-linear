from sympy import *
import os

os.system("clear")

#Matriz 4x4
tamanho = 4
identidade = eye(tamanho)
uns = ones(tamanho)
A = uns-identidade
inversa_A = A.inv()
pprint(inversa_A)
print(end="\n\n")
#Matriz 5x5
tamanho = 5
identidade = eye(tamanho)
uns = ones(tamanho)
A = uns-identidade
inversa_A = A.inv()
pprint(inversa_A)
print(end="\n\n")
#Matriz 6x6
tamanho = 6
identidade = eye(tamanho)
uns = ones(tamanho)
A = uns-identidade
inversa_A = A.inv()
pprint(inversa_A)
print(end="\n\n")
print("DIAGONAL PRINCIPAL É ((-tamanho+2)/tamanho-1) e o restante é (1/tamanho-1)")