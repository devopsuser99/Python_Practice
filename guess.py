import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input (f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Higher!")
        elif guess > random_number:
            print("Lower!")
        if guess == random_number:
            print(f"You got it! the number was {random_number}5")


guess(10)