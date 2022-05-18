from sympy import *
import os

os.system("clear")


#5-3t+4t²+2t³
p1 = Matrix([[5,-3,4,2]])

#9+t+8t²-6t³
p2 = Matrix([[9,1,8,-6]])
#6-2t+5t²
p3 = Matrix([[6,-2,5,0]])

#t³
p4 = Matrix([[0,0,0,1]])

A = Matrix([])

A = A.row_insert(0,p1)
A = A.row_insert(1,p2)
A = A.row_insert(2,p3)
A = A.row_insert(3,p4)

A = A.col_insert(4,zeros(4,1))

pprint(A.rref())


print("\n O CONJUNTO DE VETORES QUE REPRESENTA ESSES POLINÔMIOS SÃO LD, ENTÃO ELES NÃO FORMAM\n UMA BASE PARA P3.")

