import random
import sympy
import os
os.system("clear")

# Função para construir matrizes
def construirMatriz():
  M = []
  linha=4
  coluna = 4
  for i in range(linha):
    linha = []
    for j in range(coluna):
      num = random.randint(0,100)
      linha.append(num)
    M.append(linha)
  matriz = sympy.Matrix(M)
  return matriz

# Inicializar as matrizes
vetor = []
tamanhoVetor = 8
for i in range(tamanhoVetor):
  vetor.append(construirMatriz())

#Matriz nula
matrizNula = sympy.zeros(4,4)

#Mostrar matrizes em pares
for j in range(0,tamanhoVetor,2):
  sympy.pprint(vetor[j])
  print()
  sympy.pprint(vetor[j+1])  
  calculoIgualdade = vetor[j]*vetor[j+1] - vetor[j+1]*vetor[j]
  sympy.pprint(calculoIgualdade)
  print()
  if calculoIgualdade == matrizNula:
    print("\n*São matrizes iguais")
    print()
    
  else:
    print("\n*São matrizes diferentes")
    print()


