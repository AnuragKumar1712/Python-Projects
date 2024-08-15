### Rock, Paper, Scissors Game in Python

**Project Overview:**

This Python project implements the classic game "Rock, Paper, Scissors." The program allows a user to play the game against the computer in an interactive command-line interface. The game will continue until the user chooses to quit.

**Features:**

1. **Random Computer Choice:**
   - The computer's choice is randomly generated from the options "rock," "paper," and "scissors" using Python's `random` module.
  
2. **User Input:**
   - The user is prompted to enter their choice of "rock," "paper," or "scissors."
   - The program validates the user's input to ensure it is one of the allowed choices. If an invalid input is provided, the user is prompted again until a valid choice is entered.
   - The user can exit the game at any time by entering 'q'.
  
3. **Winner Determination:**
   - The game logic determines the winner based on the traditional rules:
     - Rock beats Scissors.
     - Scissors beat Paper.
     - Paper beats Rock.
   - If both the user and the computer choose the same option, the game results in a tie.
  
4. **Continuous Play:**
   - The game continues to prompt the user for their choice and play rounds against the computer until the user decides to quit by entering 'q'.

5. **User-Friendly Output:**
   - After each round, the program displays the choices made by both the user and the computer, followed by the result of the round (either "You Win!", "Computer Wins!", or "It's a tie!").

This project is a simple yet engaging way to practice fundamental Python concepts such as loops, conditionals, functions, and user input handling. It's also a great example of how to use the `random` module for generating unpredictable results.
