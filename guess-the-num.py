# The computer generates a number and the user has to guess that number
import random
def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while (user_guess != random_number):
        user_guess = int(input("Enter your guess - "))
        if random_number == user_guess: 
            print("You were correct!")
        else: print("You were incorrect :(")