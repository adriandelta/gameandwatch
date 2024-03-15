# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:12:01 2024

@author: Adrian Hall
for fun Blackjack program
"""

import random # for random int generation
import sys # for force quit

print("Welcome to Blackjack in Python!")

user_total = random.randint(1,21) #draws two cards that total up to 21
user_act = "default"

print(f"Your starting total is {user_total}!")

# as long as action is NOT pass, execute loop
while (user_act != "Pass") and (user_act != "pass") and (user_act != "PASS") and (user_total <= 21):
    if user_act == "default": # first loop only
        user_act = input("Hit or Pass? ")
    elif (user_act == "Hit") or (user_act == "hit") or (user_act == "HIT"):
        user_draw = random.randint(1,11) # draws a random card
        if (user_draw == 11) and (user_total > 10): # if Ace/11 would cause bust
            user_draw = 1 # then use it as a 1 instead
        print(f'Drew {user_draw}!') #display the card we just drew
        user_total += user_draw # add its value to our current total
        print(f'Your current total is {user_total}.') #display new total
        if user_total > 21: #if we went over 21, bust
            print("Player BUST!")
            print("Computer wins!")
            sys.exit() #exits program
        else:
            user_act = input("Hit or Pass? ") #ask again to continue loop
    else: # if user inputs an action that is not hit or pass
        print("Invalid input!")
        user_act = input("Hit or Pass? ")

if user_total > 21: #I'm not sure if I need this section but i'm scared to remove it
    print("Player BUST!")
    print("Computer wins!")
    sys.exit()

elif (user_act == "Pass") or (user_act == "pass") or (user_act == "PASS"):
    print(f'Computer\'s turn!')

NPC_total = random.randint(1,21) # computer starting draw

if NPC_total == 21: #if computer draws exactly 21 stop
    print(f'Computer drew 21!')
elif NPC_total <= user_total:
    while NPC_total <= user_total: # otherwise draw until npc is > user_total
        print(f'Computer total is currently: {NPC_total}')
        user_draw = random.randint(1,11)
        print(f'Computer drew {user_draw}!')
        NPC_total += user_draw

if NPC_total > 21: # if computer goes above 21
    print("Computer BUST!")
    print("You win!")  

else: # see who won
    print(f'Computer total is currently: {NPC_total}')
    if NPC_total > user_total:
        print("Computer wins!")
    elif NPC_total < user_total: # belatedly realizing this will never execute
        print("You win!")
    else:
        print("Tie with computer!") # do I want this to be an option?

#end program

        
        
        