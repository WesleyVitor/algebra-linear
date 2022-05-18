import random
import sympy
import os
os.system("clear")

# Função para construir matrizes
def construirMatriz():
  M = []
  linha=5
  coluna = 5
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
tamanhoVetor = 3
for i in range(tamanhoVetor):
  vetor.append(construirMatriz())

#Matriz identidade
matrizIdentidade = sympy.eye(5)
matrizNula = sympy.zeros(5,5)
for j in range(tamanhoVetor):
  sympy.pprint(vetor[j])
  print()
  calculoIgualdade = ((vetor[j]+matrizIdentidade)* (vetor[j]-matrizIdentidade)) - (vetor[j]*vetor[j]-matrizIdentidade)
  sympy.pprint(calculoIgualdade)
  print()
  if calculoIgualdade == matrizNula:
    print("\n*São matrizes iguais")
    print()
    
  else:
    print("\n*São matrizes diferentes")
    print()


