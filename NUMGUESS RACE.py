import random  # Import random module to generate random numbers for guessing

def play_game():
    """Runs the two-team number guessing game with a range of 1 to 5.
    A team moves back one step only after two consecutive incorrect guesses in their turn.
    """

    # --- Game Setup ---
    print("--- Welcome to the Number Guessing Race! ---")
    print("Teams will guess a number. Correct guess moves forward,")
    print("two incorrect guesses in a row moves backward.\n")

    # Get team 1 name and player names
    team1_name = input("Enter name for Team 1: ")
    team1_player1 = input(f"Enter name for Player 1 of {team1_name} (the guesser): ")
    team1_player2 = input(f"Enter name for Player 2 of {team1_name} (the mover): ")

    # Get team 2 name and player names
    team2_name = input("Enter name for Team 2: ")
    team2_player1 = input(f"Enter name for Player 1 of {team2_name} (the guesser): ")
    team2_player2 = input(f"Enter name for Player 2 of {team2_name} (the mover): ")

    # Initialize team positions (starting point 0)
    team1_position = 0
    team2_position = 0

    # Counters to track consecutive wrong guesses for each team
    team1_consecutive_wrong_guesses = 0
    team2_consecutive_wrong_guesses = 0

    winning_score = 5  # Number of steps needed to win the game
    current_turn = 1   # Counter for the current turn number
    guess_range_min = 1  # Minimum number in the guessing range
    guess_range_max = 3  # Maximum number in the guessing range (difficulty level)

    # Show game start info with player roles and rules
    print(f"\n--- Game Start! ---")
    print(f"{team1_name}: {team1_player1} (guessing), {team1_player2} (moving)")
    print(f"{team2_name}: {team2_player1} (guessing), {team2_player2} (moving)")
    print(f"Guess a number between {guess_range_min} and {guess_range_max}.")
    print(f"First team to reach {winning_score} steps wins!\n")

    # --- Game Loop ---
    # The loop continues until one team reaches the winning score
    while team1_position < winning_score and team2_position < winning_score:
        print(f"\n--- Turn {current_turn} ---")

        # --- Team 1's Turn ---
        if team1_position < winning_score and team2_position < winning_score:  # Check if game is still going
            print(f"\nIt's {team1_name}'s turn. {team1_player1} is guessing.")

            # Randomly generate the secret number for team 1 to guess
            secret_number_team1 = random.randint(guess_range_min, guess_range_max)
            guess_team1 = 0

            # Loop until a valid guess is entered by the player
            while True:
                try:
                    guess_team1 = int(input(f"{team1_player1}, guess a number between {guess_range_min} and {guess_range_max}: "))
                    if guess_range_min <= guess_team1 <= guess_range_max:
                        break  # Exit the loop if guess is valid
                    else:
                        print(f"Oops! Please enter a number between {guess_range_min} and {guess_range_max}.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            # Check if the guess matches the secret number
            if guess_team1 == secret_number_team1:
                print(f"Correct! The number was {secret_number_team1}.")
                team1_position += 1  # Move forward one step
                team1_consecutive_wrong_guesses = 0  # Reset wrong guess counter
                print(f"{team1_player2} moves 1 step forward for {team1_name}!")
            else:
                print(f"Incorrect. The number was {secret_number_team1}.")
                team1_consecutive_wrong_guesses += 1  # Increase wrong guess counter

                # If two wrong guesses in a row, move one step back
                if team1_consecutive_wrong_guesses >= 2:
                    team1_position = max(0, team1_position - 1)  # Ensure position does not go below 0
                    print(f"{team1_player2} moves 1 step back for {team1_name} (2 wrong guesses).")
                    team1_consecutive_wrong_guesses = 0  # Reset wrong guesses after moving back
                else:
                    print(f"{team1_name} has {team1_consecutive_wrong_guesses} wrong guess. One more wrong guess will move them back.")

            # Show current positions of both teams
            print(f"Current positions: {team1_name}: {team1_position}, {team2_name}: {team2_position}")

        # If team 1 already won, break the loop and end game
        if team1_position >= winning_score:
            break

        # --- Team 2's Turn ---
        if team1_position < winning_score and team2_position < winning_score:  # Check if game still ongoing
            print(f"\nIt's {team2_name}'s turn. {team2_player1} is guessing.")

            # Randomly generate the secret number for team 2
            secret_number_team2 = random.randint(guess_range_min, guess_range_max)
            guess_team2 = 0

            # Loop until team 2's guess is valid
            while True:
                try:
                    guess_team2 = int(input(f"{team2_player1}, guess a number between {guess_range_min} and {guess_range_max}: "))
                    if guess_range_min <= guess_team2 <= guess_range_max:
                        break
                    else:
                        print(f"Oops! Please enter a number between {guess_range_min} and {guess_range_max}.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            # Check if team 2's guess is correct
            if guess_team2 == secret_number_team2:
                print(f"Correct! The number was {secret_number_team2}.")
                team2_position += 1  # Move forward
                team2_consecutive_wrong_guesses = 0  # Reset wrong guess counter
                print(f"{team2_player2} moves 1 step forward for {team2_name}!")
            else:
                print(f"Incorrect. The number was {secret_number_team2}.")
                team2_consecutive_wrong_guesses += 1

                # Two wrong guesses move team 2 backward by one step
                if team2_consecutive_wrong_guesses >= 2:
                    team2_position = max(0, team2_position - 1)
                    print(f"{team2_player2} moves 1 step back for {team2_name} (2 wrong guesses).")
                    team2_consecutive_wrong_guesses = 0
                else:
                    print(f"{team2_name} has {team2_consecutive_wrong_guesses} wrong guess. One more wrong guess will move them back.")

            # Show current positions
            print(f"Current positions: {team1_name}: {team1_position}, {team2_name}: {team2_position}")

        current_turn += 1  # Increase turn count for next round

    # --- Game Over ---
    print("\n--- Game Over! ---")
    if team1_position >= winning_score:
        print(f"🎉 Congratulations {team1_name}! {team1_player1} and {team1_player2} win! 🎉")
    elif team2_position >= winning_score:
        print(f"🎉 Congratulations {team2_name}! {team2_player1} and {team2_player2} win! 🎉")
    else:
        # Shouldn't happen if game loop works correctly
        print("The game ended unexpectedly. Please check the scores.")

# Start the game by calling the function
play_game()
