from sympy import *
import os
os.system("clear")

A = Matrix([[2,3,5,-5],
               [-7,7,0,0],
               [-3,4,1,3],
               [-9,3,-6,-4]])

b = [8,7,5,-3]

Aamp = Matrix([[2,3,5,-5,8],
               [-7,7,0,0,7],
               [-3,4,1,3,5],
               [-9,3,-6,-4,-3]])

pprint(Aamp)
print("\n\n")

resultado = Aamp.rref()

pprint(resultado)
print("\n\n")

print("1.O vetor b faz parte do range de transformação!\n")
print("2.Os valores de x que produz como imagem o vetor b são infinitas!\n")