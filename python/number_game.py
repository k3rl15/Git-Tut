import random
import sys

guesses = 3

winning_number = random.randint(1, 10)
guessed_number = None
print("Guess the Number [1-10]")

while guesses > 0:
    try:
        guessed_number = int(input(f"Guess: "))
        if guessed_number == winning_number:
            print(f"Your guess {winning_number} was correct!")
            sys.exit()
        elif guessed_number > 10:
            print(f"Try to guess a number from 1 to 10, no freebies since you guessed a number. "
                  f"You have {guesses - 1} remaining!")
        else:
            print(f"Wrong")
        guesses -= 1

    except ValueError:
        print(f"Invalid input! You have {guesses} remaining!")

print(f"You are out of guesses and you haven't guessed {winning_number}!")
