from sympy import *
import os 

os.system("clear")

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

a1 = A[:,0]
a2 = A[:,1]
a3 = A[:,2]
a4 = A[:,3]

a1a2 = a1.T*a2
a1a3 = a1.T*a3
a1a4 = a1.T*a4

a2a3 = a2.T*a3
a2a4 = a2.T*a4

a3a4 = a3.T*a4

print("Produtos internos:")

print("a1a2=",a1a2[0])
print("a1a3=",a1a3[0])
print("a1a4=",a1a4[0])
print("a2a3=",a2a3[0])
print("a2a4=",a2a4[0])
print("a3a4=",a3a4[0])

print("\n Os vetores de A são ortoganais, pois o produto internos entre eles é igual 0.")