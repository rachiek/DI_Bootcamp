import random

def number_guessing_game():
    random_number = random.randint(1, 100)

    print("I am thinking of a number between 1 and 100. Guess it!")

    for attempt in range(7):
        guess = int(input("Enter your guess: "))
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("You won!")
            return
    print("Game over! The number was:", random_number)

number_guessing_game()