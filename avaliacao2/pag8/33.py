from sympy import *
import os

os.system("clear")


# 3+7t
p1 = Matrix([[3,7,0,0]])

#5+t-2t³
p2 = Matrix([[5,1,0,-2]])

#t-2t²
p3 = Matrix([[0,1,-2,0]])

#1+16t-6t²+2t³

p4 = Matrix([[1,16,-6,2]])


A = Matrix([])

A = A.row_insert(0,p1)
A = A.row_insert(1,p2)
A = A.row_insert(2,p3)
A = A.row_insert(3,p4)

A = A.col_insert(4,zeros(4,1))

pprint(A.rref())

print("\n O CONJUNTO DE VETORES QUE REPRESENTA ESSES POLINÔMIOS SÃO LD, ENTÃO ELES NÃO FORMAM\n UMA BASE PARA P3.")



