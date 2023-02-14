import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)
    tries = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        tries += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break
    
    print("Good job, " + name + "! You guessed my number in " + str(tries) + " guesses!")

guess_the_number()