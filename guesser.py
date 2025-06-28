import random

def display_introduction():
    """Prints the welcome message and game rules."""
    print("\nWelcome to the number guessing game")
    print("-----------------------------------")
    print("Here are the rules:")
    print(". First, you will choose a difficulty level.")
    print(". I will then pick a random number within that difficulty's range.")
    print(". You need to guess that number.")
    print(". I'll tell you if your guess is higher or lower than the secret number.")
    print(". You can type 'q' or 'quit' to exit the game at any time.")
    print("-----------------------------------")

def get_difficulty():
    """Asks the user for a difficulty level and returns the range."""
    while True:
        level = input("Choose a difficulty (easy, medium, hard): ").lower()
        if level == "easy":
            return 1, 50
        elif level == "medium":
            return 1, 100
        elif level == "hard":
            return 1, 500
        elif level in ['q', 'quit']:
            return None, None
        else:
            print("Invalid input. Please choose easy, medium, or hard.")

def play_game_round(min_range, max_range):
    """Handles the logic for a single round of the guessing game."""
    secret_number = random.randint(min_range, max_range)
    guess_count = 0

    print(f"\nI've picked a number between {min_range} and {max_range}. Good luck!")

    while True:
        user_input = input("Guess the number: ")

        if user_input.lower() in ['q', 'quit']:
            print(f"You've quit the game. The number was {secret_number}")
            return # Exit the function for this round

        try:
            guess = int(user_input)
            guess_count += 1
        except ValueError:
            print("Invalid input. Please enter a whole number or 'q' to quit.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You've guessed the number {secret_number} correctly.")
            print(f"It took you {guess_count} guesses.")
            break # Exit the loop and end the round

def main():
    """The main function to orchestrate the game."""
    print("Hello from the enhanced number-guessing-game!")
    display_introduction()

    while True:
        min_num, max_num = get_difficulty()

        if min_num is None: # User chose to quit from difficulty selection
            break

        play_game_round(min_num, max_num)

        play_again = input("\nDo you want to play again? (y/n): ")
        if not play_again.lower().startswith('y'):
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()