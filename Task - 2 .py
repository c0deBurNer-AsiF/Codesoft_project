'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''

'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''

import math
def calculator():
    while True:
        print("\n1.Additon\n2.Subtraction\n3.Multiplicatiion\n4.Division\n5.Raise_power\n6.Factorial\n7.Exit\n")
        try:
            user_input=int(input("Select required option:")) 
            if user_input==7:
                print("Thank You for using!!")
                break
            if user_input<1 or user_input>7:
                print("Input out of range!!..Input must be range of (1-7)")
                continue
        except:
            print("Invalid input!!..")
            continue

        try:
            if user_input==6:
                a=int(input("Enter a integer number:"))
                if a<0:
                    print("Negative number not allow for calculatig factorial!!")
                    continue
                print("Factorial of %d is"%(a),math.factorial(a))
        except:
            print("Invalid input!!.. input should be integer number.")
            continue

        if user_input in {1,2,3,4,5}:
            try:
                a=int(input("Enter first number:"))
                b=int(input("Enter second number:"))
            except:
                print("Both value must be integer!!")
                continue    

        match user_input:
            case 1:
                print("Addition of %d and %d is %d"%(a,b,a+b))
            case 2:
                print("Subtraction of %d and %d is %d"%(a,b,a-b)) 
            case 3:
                print("Multiplication of %d and %d is %d"%(a,b,a*b))
            case 4:
                try:
                   print("Subtraction of %d and %d is"%(a,b),a/b)
                except:
                     print("ZeroDivisionError!! Denominator can not be Zero")
            case 5:
                print("%d 's power %d == %d"%(a,b,a**b))  
calculator()                                             





'''
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
                    break
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
            '''
                          






        
