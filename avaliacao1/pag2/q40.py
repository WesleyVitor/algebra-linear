from sympy import *
import os
os.system("clear")

A= Matrix([[3,4,-7,0],
               [5,-8,7,4],
               [6,-8,6,4],
               [9,-7,-2,0]])
b = [4,-4,-4,-7]

Aamp = Matrix([[2,3,5,-5,4],
               [-7,7,0,0,-4],
               [-3,4,1,3,-4],
               [-9,3,-6,-4,-7]])

pprint(Aamp)
print("\n\n")

resultado = Aamp.rref()

pprint(resultado)
print("\n\n")

print("1.O vetor b não faz parte do range de transformação!\n")
print("2.Não existe valores de x que produz como imagem o vetor b!\n")