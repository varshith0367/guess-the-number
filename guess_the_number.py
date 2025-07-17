import random

def welcome():
    print("Hello! Welcome to my Guess the Number Game.")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

def play_game():
    number_to_guess = random.randint(1, 100)
    tries = 0

    while True:
        guess = input("Type your guess: ")
        tries += 1

        # Check if the input is a number
        if not guess.isdigit():
            print("Oops! Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < number_to_guess:
            print("Too low! Try a bigger number.")
        elif guess > number_to_guess:
            print("Too high! Try a smaller number.")
        else:
            print(f"Awesome! You guessed the number {number_to_guess} in {tries} attempts.")
            break

if __name__ == "__main__":
    welcome()
    play_game()
    print("Thanks for playing! - varshith0367")
