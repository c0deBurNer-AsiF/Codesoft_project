"""User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback."""


import random
choices=["rock","paper","scissor"]
computer_score=0
user_score=0
round=1
def user_typed():
    for i in choices:
        print(i,end=" ")
    while True:    
        try:
            user_input=input("\nSelect your choice:").strip().lower()
            if user_input in choices:
               print("\nUser's choice=",user_input)
               return user_input 
            
            elif user_input not in choices:
                print("Invalid Syntax!!\nRetry!!")
                continue
        except:
            print("Invalid Input!!.. Input should be 'rock', 'paper' or 'scissor'")
            continue
        
    
def performe():
    global computer_score,user_score,round
    user_choice=user_typed()
    computer_choice=random.choice(choices)
    print("Computer choice=",computer_choice)
    
    print("\nUser choice:",user_choice,"\nComputer choice:",computer_choice)
       
    if user_choice=="rock" and computer_choice=="paper":
        print("User lose!!")
        print("Paper beats rock")
        computer_score+=1

    elif user_choice=="rock" and computer_choice=="scissor":
        print("User Win!!")
        print("rock beats scissor")
        user_score+=1

    elif user_choice=="paper" and computer_choice=="rock":
        print("User Win!!")
        print("paper beats rock")
        user_score+=1 

    elif user_choice=="paper" and computer_choice=="scissor":
        print("User lose!!")
        print("scissor beats paper")
        computer_score+=1 

    elif user_choice=="scissor" and computer_choice=="rock":
        print("User lose!!")
        print("rock beats scissor")
        computer_score+=1  

    elif user_choice=="scissor" and computer_choice=="paper":
        print("User Win!!")
        print("scissor beats paper")
        user_score+=1  
    else:
        print("Its a tie!")

    print("\nRound=",round,"\nUser's score=",user_score,"\nComputer's score=",computer_score) 
    round+=1   
    
  
def permission():
    performe()
    while True:
        print("Wanna play round",round,"?\n'YES' or 'EXIT'")
        x=input().strip().lower()
        try:
            if x=="yes":
                performe()
                pass
            elif x=="exit":
                print("\nFinal result:\nUser's Score=",user_score,"\nComputer's Score:",computer_score)
                break
            else:
                print("Invalid Input!! Input must be 'YES' or 'Exit'")
                continue
        except:
            print("Invalid Syntax!!.. Input must be string!")    
permission()

            



        



