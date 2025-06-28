# Number Guessing Game

A simple, fun, and interactive number guessing game written in Python. The program generates a random number and challenges the user to guess it, providing feedback along the way.

## Features

-   **Random Number Generation**: A secret number is randomly chosen between 1 and 100 for each round.
-   **Interactive Guessing**: Users can input their guesses directly in the terminal.
-   **Helpful Hints**: The game tells you if your guess is "Too high!" or "Too low!"
-   **Guess Counter**: At the end of a successful round, the game reports how many guesses it took.
-   **User-Friendly Controls**: Quit the current round at any time by typing `n` or `N`.
-   **Replayability**: After each round, you have the option to play again for endless fun.
-   **Robust Input Handling**: The program gracefully handles non-numeric input without crashing.

## How to Play

### Prerequisites

-   Python 3.x must be installed on your system.

### Running the Game

1.  Save the code as a Python file (e.g., `game.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the game using the following command:
    ```bash
    python game.py
    ```
5.  Follow the on-screen instructions to play the game!

## Game Rules

1.  The computer will pick a random number between 1 and 100.
2.  Your goal is to guess that number.
3.  After each guess, the computer will tell you if your guess is higher or lower than the secret number.
4.  The game continues until you guess the correct number.
5.  You can type 'n' or 'N' to quit the game at any time during a round.

## Code Structure

The program is organized into three main functions for clarity and maintainability:

-   `display_introduction()`: Prints the welcome message and the game rules to the user.
-   `play_game_round()`: Contains the core logic for a single round of the game, including random number generation, user input, and win/loss conditions.
-   `main()`: The main function that orchestrates the game flow, calls the introduction, and manages the "play again" loop.

The `if __name__ == "__main__":` block ensures that the `main()` function is called only when the script is executed directly.
