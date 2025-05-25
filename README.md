# Computer-Programming-repository-LHY
Assignment Purpose
Number Guessing Race Game


Overview


Number Guessing Race is a simple, turn-based console game. Two teams, where each with two players (a "guesser" and a "mover"), compete to be the first to reach a target number of steps. Teams can only advance if and only if the guess a randomly generated number correctly. But on the contrary, two incorrect guesses in a row will move your team one step backwards.


Features


Two Teams, Two Players Each: Designate one player to guess the number and the corresponding team mate to move.
Random Number Guessing: Players guess a number within a defined range.


Step-Based Movement:


Correct guess: Mover takes 1 step forward.

Incorrect guess: The team gets a "wrong guess".

Two consecutive incorrect guesses in a team's turn: Mover takes 1 step backward. The strike count resets.

Winning Condition: The first team to reach a predefined number of steps wins.


How to Play

NOTE: Ensure you have Python 3 installed on your system.


Run the Game:


Save the game code as a Python file (e.g., guessing_game.py).

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Execute the script using the command: python guessing_game.py
or 
downloading an IDE and running the game inside.


Game Setup:


The game will first prompt you to enter the name for Team 1.

Then, enter the name of Player 1 (the guesser) for Team 1.

Next, enter the name of Player 2 (the mover) for Team 1.

Repeat this process for Team 2.


Gameplay:


The game will announce whose turn it is.

The designated "guesser" for the current team must enter a number between 1 and 5 when prompted.


Correct Guess:


The team's "mover" advances 1 step.

Any count of previous consecutive wrong guesses for that team is reset.


Incorrect Guess:


The team accumulates one "wrong guess strike" for that turn.

If this is the first incorrect guess in a row for the turn, the team is warned.

If this is the second consecutive incorrect guess in a row for the turn, the team's "mover" moves 1 step backward (but not below 0 steps). The wrong guess strike count is then reset for that team.

The game will display the current positions of both teams after each guess.

Turns alternate between Team 1 and Team 2.


Winning the Game:


The first team whose "mover" reaches the winning_score is declared the winner.

The game will then end.


Code Description


The game is contained within a single Python script.

import random: Used to generate the secret numbers for guessing.

play_game() function: This is the main function that encapsulates all the game logic.


Game Setup:


Initializes player names, team positions (team1_position, team2_position), and counters for consecutive wrong guesses (team1_consecutive_wrong_guesses, team2_consecutive_wrong_guesses).

Sets game parameters like winning_score, guess_range_min, and guess_range_max.

Prints welcome messages and initial instructions.

Game Loop (while team1_position < winning_score and team2_position < winning_score:):

This loop continues as long as neither team has reached the winning_score.

It manages turns for Team 1 and Team 2.


Game Over:


Once the game loop terminates, a "Game Over!" message is displayed.

The winning team is announced.
