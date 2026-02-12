#This file is where the user should be prompted for their two numbers and recieve their response








import mymath

choice = int(input("Please enter which equation you'd like solved \n1.) Ax+B=0 solving for x: \n2.) A^2 + B^2 = C^2 solving for C\n"))

if choice == 1:
    A = int(input("Please enter the number you would like to use for A: \n"))
    B = int(input("Please enter the number you would like to use for B: \n"))
    mymath.SolveAxPlusB(A,B)
elif choice == 2:
    A = int(input("Hello! Please enter the number you would like to use for A: \n"))
    B = int(input("Hello! Please enter the number you would like to use for B: \n"))
    mymath.SolveHypotenuse(A,B)
else:
    print("I'm sorry, I didn't understand your input.")