'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''

import math
while True:
    print("1.Additon\n2.Subtraction\n3.Multiplicatiion\n4.Division\n5.Raise_power\n6.Factorial\n7.Exit")
    try:        
        user_input=int(input("Please select required option:"))
        if user_input>0 and user_input<8:
            pass
        else:
             print("Invalid input!! Input out of range!!")
    except:
        print("Invalid input!! Input should be must be integer") 

    match user_input:
        case 1:
            while True:
                try:
                    a=int(input("Enter first number:"))
                    b=int(input("Enter second number:"))
                    print("Addition of %d and %d is: %d"%(a,b,a+b))
                    break
                except:
                    print("Please enter an integer number!!")

        case 2:
            while True:
                try:
                    a=int(input("Enter first number:"))
                    b=int(input("Enter second number:"))
                    print("Subtraction of %d and %d is: %d"%(a,b,a-b))
                except:
                    print("Please enter an integer number!!")

        case 3:
            while True:
                try:
                    a=int(input("Enter first number:"))
                    b=int(input("Enter second number:"))
                    print("Multiplication of %d and %d is: %d"%(a,b,a*b))
                    break
                except:
                    print("Please enter an integer number!!")   

        case 4:
            while True:
                try:
                    a=int(input("Enter first number:"))
                    b=int(input("Enter second number:"))
                    print("Division of %d and %d is: %d"%(a,b,a/b))
                    break
                except:
                    print("Please enter an integer number!!")   

        case 5:
            while True:
                try:
                    a=int(input("Enter first number:"))
                    b=int(input("Enter second number:"))
                    print("%d raised to the power %d is: %d"%(a,b,a**b))
                    break
                except:
                    print("Please enter an integer number!!")


        case 6:
            while True:
                try:
                    a=int(input("Enter a number:"))
                    print("Factorial of this number is:",math.factorial(a))
                    break
                except:
                    print("Invalid input!! Input should be an integer number....")            

        case 7:
            print("Thanks your using!!")
            break
                          






        
