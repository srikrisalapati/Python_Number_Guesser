import random


def display_introduction():
    """Prints the welcome message and game rules."""
    print("Welcome to the number guessing game")
    print("-----------------------------------")
    print("Here are the rules:")
    print(". I will pick a random number between 1 and 100.")
    print(". You need to guess that number.")
    print(". I'll tell you if your guess is higher or lower than the secret number.")
    print(". The game continues until you guess the correct number.")
    print(". You can type 'n' or 'N' to quit the game at any time.")
    print("-----------------------------------")


def play_game_round():
    """Handles the logic for a single round of the guessing game."""
    secret_number = random.randint(1, 100)
    guess_count = 0

    while True:
        user_input = input("Guess the number: ")

        if user_input.lower() == 'n':
            print(f"You've quit the game. The number was {secret_number}")
            return  # Exit the function for this round

        try:
            guess = int(user_input)
            guess_count += 1
        except ValueError:
            print("Invalid input. Please enter a whole number or 'n' to quit.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly.")
            print(f"It took you {guess_count} guesses.")
            break  # Exit the loop and end the round


def main():
    print("Hello from number-guessin-game!")
    """The main function to orchestrate the game."""
    display_introduction()

    while True:
        play_game_round()

        play_again = input("Do you want to play again? (y/n): ")
        if not play_again.lower().startswith('y'):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
    