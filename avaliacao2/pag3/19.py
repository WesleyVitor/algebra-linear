from sympy import *
import os

os.system("clear")


A = Matrix([
  [.4,.2,.3],
  [.3,.6,.3],
  [.3,.2,.4]
])

B = Matrix([
  [0,.2,.3],
  [.1,.6,.3],
  [.9,.2,.4]
])

print("MATRIZ A")
p1 = A**2
p2 = A**3
p3 = A**4
p4 = A**5
print()
pprint(p1)
print()
pprint(p2)
print()
pprint(p3)
print()
pprint(p4)
print("\n O único valor que varia é o do meio \n")
print(end="\n\n\n")

print("MATRIZ B")
p1 = B**2
p2 = B**3
p3 = B**4
p4 = B**5
p5 = B**6
p6 = B**7
print()
pprint(p1)
print()
pprint(p2)
print()
pprint(p3)
print()
pprint(p4)
print()
pprint(p5)
print()
pprint(p6)
print()

print("\n Quanto maior a potência percebemos que mais próximos os valores de cada linha ficam próximos entre eles\n")