from sympy import *
import os
os.system("clear")

v = [10, -7, 5, 23] 

#Pegando a matriz B e ampliando com o vetor podemos provar se
# Bx = v, em que v faz parte do span das colunas de B
Bamp = Matrix([[3,-4,7,10],
               [-5,-3,-11,-7],
               [4,3,2,5],
               [8,-7,4,23]])

pprint(Bamp)
print("\n\n")

B_Reduzida = Bamp.rref()
pprint(B_Reduzida)

print("\n\n Então v faz parte do span das colunas de B")