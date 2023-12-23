# Rock-Paper-Scissors against computer
import random

def rps():
    hand = input("Enter your hand - ")
    seq = ['Rock', 'Paper', 'Scissors']
    computers_hand = random.choice(seq)
    if (computers_hand == hand): print("Tie")
    elif ((computers_hand == 'Rock' and hand == 'Scissors') or 
          (computers_hand == 'Paper' and hand == 'Rock') or
          (computers_hand == 'Scissors' and hand == 'Paper')): 
         print("You Lose")
         print(computers_hand)
    else: 
        print("You win")
        print(computers_hand)

rps()