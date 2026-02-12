#Sophia Alexander
#Last edited: 02/11/2026
from cmath import sqrt

#variable type assignments
A = int
B = int
C = int
x = int


def SolveAxPlusB(A,B):
    x = -B/A
    print("The solution is: ", x)

def SolveHypotenuse(A,B):
    C = sqrt(A^2 + B^2)
    print("The solution is: ", C)