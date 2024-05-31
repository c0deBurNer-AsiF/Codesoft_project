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
user_score=0
computer_score=0
round=1
while True:
    choices=["rock","paper","scissor"]

    for i in choices[::]:
        print(i,end=",")

    user_choice=input("\nchoice any one option:").strip().lower()
    computer_choice=random.choice(choices)

    if user_choice not in choices:
        print("invalid syntax\nRetry again!!")
        pass

    else: 
        print("User choice:",user_choice,"Computer choice:",computer_choice,sep="\n")
       
        if user_choice=="rock" and computer_choice=="paper":
            print("Computer Win!!")
            print("Paper beats rock")
            computer_score=computer_score+1

        elif user_choice=="rock" and computer_choice=="scissor":
            print("User Win!!")
            print("rock beats scissor")
            user_score=user_score+1

        elif user_choice=="paper" and computer_choice=="rock":
            print("User Win!!")
            print("paper beats rock")
            user_score=user_score+1 

        elif user_choice=="paper" and computer_choice=="scissor":
            print("Computer Win!!")
            print("scissor beats paper")
            computer_score=computer_score+1 

        elif user_choice=="scissor" and computer_choice=="rock":
            print("Computer Win!!")
            print("rock beats scissor")
            computer_score=computer_score+1  

        elif user_choice=="scissor" and computer_choice=="paper":
            print("User Win!!")
            print("scissor beats paper")
            user_score=user_score+1  
        else:
            print("Its a tie!")

        print("Round:",round,"User score:",user_score,"Computer score:",computer_score,sep="\n")
        round=round+1
        print("If you want to play round",round,",then enter 'YES' other wise enter 'EXIT'")
        permission=input()
        if permission=="YES":
            pass
        else:
            print("Final result:\nUser score:%d\nComputer score:%d"%(user_score,computer_score))
            break

            



        



