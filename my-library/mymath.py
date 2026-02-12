#Sophia Alexander
#Last edited: 02/11/2026
from cmath import sqrt

#variable type assignments
A = int
B = int
C = int
x = int


def SolveAxPlusB():
    A = input("Hello! Please enter the number you would like to use for A: \n")
    B = input("Hello! Please enter the number you would like to use for B: \n")
    x = -B/A
    print("The solution is: " + x)

def SolveHypotenuse():
    A = input("Hello! Please enter the number you would like to use for A: \n")
    B = input("Hello! Please enter the number you would like to use for B: \n")
    C = sqrt(A^2 + B^2)
    print("The solution is: " + C)