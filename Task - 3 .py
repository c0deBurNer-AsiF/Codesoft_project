'''A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.
User Input: Prompt the user to specify the desired length of the
password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen'''


import random 
import string

def generate_password(length):
    character=string.ascii_letters+string.punctuation+string.digits
    password="".join(random.choices(character,k=length))
    return password

def re_generate():
    while True:
        re_enter=input(("\nIf you want to re-generate the password enter 'Yes' otherwise 'Exit':\n")).strip().upper()
        if re_enter=="YES":
            userInput()
            break
        elif re_enter=="EXIT":
            print("\nYour password generated successfully!!")
            break
        else:
            print("\nInvalid input!! Please enter 'Yes' or 'Exit'")


def userInput():
    while True:  
        try:
          user_input=int(input("Enter the length of the password:"))
          if user_input<=0:
              print("Please enter a postive integer value!!")
          else:
              break
        except:
            print("Invalid input!! The length must be a positive integer value")

    final_password=generate_password(user_input)
    print("Generated password is:",final_password)
    re_generate()

userInput()







