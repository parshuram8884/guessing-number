import random 

number = random, randint(1,9)
guess = 5 

while guess != number: 
    guess = int(input("Enter Guess:"))

    if (guess < number):
        print("Guess higher")
    elif (guess > number):
        print ("Guess lower")
    else: 
        print("You Won!")