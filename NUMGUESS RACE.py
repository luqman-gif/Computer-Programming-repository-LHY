import random

def play_game():
    """Runs the two-team number guessing game with a range of 1 to 5.
    A team moves back one step only after two consecutive incorrect guesses in their turn.
    """

    # --- Game Setup ---
    print("--- Welcome to the Number Guessing Race! ---")
    print("Teams will guess a number. Correct guess moves forward,")
    print("two incorrect guesses in a row moves backward.\n")

    # Getting players info for Team 1
    team1_name = input("Enter name for Team 1: ")
    team1_player1 = input(f"Enter name for Player 1 of {team1_name} (the guesser): ")
    team1_player2 = input(f"Enter name for Player 2 of {team1_name} (the mover): ")

    # Getting players info for Team 2
    team2_name = input("Enter name for Team 2: ")
    team2_player1 = input(f"Enter name for Player 1 of {team2_name} (the guesser): ")
    team2_player2 = input(f"Enter name for Player 2 of {team2_name} (the mover): ")

    # Intial team positions and counters for wrong guesses
    team1_position = 0
    team2_position = 0
    team1_consecutive_wrong_guesses = 0
    team2_consecutive_wrong_guesses = 0

    winning_score = 5  # You can change this to make the game longer or shorter
    current_turn = 1
    guess_range_min = 1
    guess_range_max = 3    # You can change the range to adjust the level of difficulty, make it easier or harder

    #Display game start info
    print(f"\n--- Game Start! ---")
    print(f"{team1_name}: {team1_player1} (guessing), {team1_player2} (moving)")
    print(f"{team2_name}: {team2_player1} (guessing), {team2_player2} (moving)")
    print(f"Guess a number between {guess_range_min} and {guess_range_max}.")
    print(f"First team to reach {winning_score} steps wins!\n")

    # --- Game Loop ---
    while team1_position < winning_score and team2_position < winning_score:
        print(f"\n--- Turn {current_turn} ---")

        # --- Team 1's Turn ---
        if team1_position < winning_score and team2_position < winning_score: # Check win condition before turn
            print(f"\nIt's {team1_name}'s turn. {team1_player1} is guessing.")
            secret_number_team1 = random.randint(guess_range_min, guess_range_max)
            guess_team1 = 0

            # Guessing loop for Team 1
            while True: # This inner loop is for a single guess attempt
                try:
                    guess_team1 = int(input(f"{team1_player1}, guess a number between {guess_range_min} and {guess_range_max}: "))
                    if guess_range_min <= guess_team1 <= guess_range_max:
                        break # Valid guess, exit inner loop
                    else:
                        print(f"Oops! Please enter a number between {guess_range_min} and {guess_range_max}.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            # Check if the guess is correct
            if guess_team1 == secret_number_team1:
                print(f"Correct! The number was {secret_number_team1}.")
                team1_position += 1
                team1_consecutive_wrong_guesses = 0 # Reset wrong guesses counter
                print(f"{team1_player2} moves 1 step forward for {team1_name}!")
            else:
                print(f"Incorrect. The number was {secret_number_team1}.")
                team1_consecutive_wrong_guesses += 1
                if team1_consecutive_wrong_guesses >= 2:
                    team1_position = max(0, team1_position - 1) # Ensure position doesn't go below 0
                    print(f"{team1_player2} moves 1 step back for {team1_name} (2 wrong guesses).")
                    team1_consecutive_wrong_guesses = 0 # Reset after moving back
                else:
                    print(f"{team1_name} has {team1_consecutive_wrong_guesses} wrong guess. One more wrong guess will move them back.")

            print(f"Current positions: {team1_name}: {team1_position}, {team2_name}: {team2_position}")

        if team1_position >= winning_score: # Check win condition after Team 1's move
            break   # End the game if team 1 already won

        # --- Team 2's Turn ---
        if team1_position < winning_score and team2_position < winning_score: # Check win condition before turn
            print(f"\nIt's {team2_name}'s turn. {team2_player1} is guessing.")
            secret_number_team2 = random.randint(guess_range_min, guess_range_max)
            guess_team2 = 0

            # Guessing loop for Team 2
            while True: # This inner loop is for a single guess attempt
                try:
                    guess_team2 = int(input(f"{team2_player1}, guess a number between {guess_range_min} and {guess_range_max}: "))
                    if guess_range_min <= guess_team2 <= guess_range_max:
                        break # Valid guess, exit inner loop
                    else:
                        print(f"Oops! Please enter a number between {guess_range_min} and {guess_range_max}.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            if guess_team2 == secret_number_team2:
                print(f"Correct! The number was {secret_number_team2}.")
                team2_position += 1
                team2_consecutive_wrong_guesses = 0 # Reset wrong guesses counter
                print(f"{team2_player2} moves 1 step forward for {team2_name}!")
            else:
                print(f"Incorrect. The number was {secret_number_team2}.")
                team2_consecutive_wrong_guesses += 1
                if team2_consecutive_wrong_guesses >= 2:
                    team2_position = max(0, team2_position - 1) # Ensure position doesn't go below 0
                    print(f"{team2_player2} moves 1 step back for {team2_name} (2 wrong guesses).")
                    team2_consecutive_wrong_guesses = 0 # Reset after moving back
                else:
                    print(f"{team2_name} has {team2_consecutive_wrong_guesses} wrong guess. One more wrong guess will move them back.")

            print(f"Current positions: {team1_name}: {team1_position}, {team2_name}: {team2_position}")


        current_turn += 1 # Move on to the next round

    # --- Game Over ---
    print("\n--- Game Over! ---")
    if team1_position >= winning_score:
        print(f"🎉 Congratulations {team1_name}! {team1_player1} and {team1_player2} win! 🎉")
    elif team2_position >= winning_score:
        print(f"🎉 Congratulations {team2_name}! {team2_player1} and {team2_player2} win! 🎉")
    else:
        # This case should ideally not be reached if the loop condition is correct,
        # but it's good for robustness.
        print("The game ended unexpectedly. Please check the scores.")

# Start the game
play_game()
