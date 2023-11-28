#Create a Rock, Paper, Scissors game where players can choose from three options. Ensure that users receive a prompt if they enter an invalid option. In each round, players must input one of the available choices and will receive feedback on whether they won, lost, or tied with the opponent. At the conclusion of each round, players have the option to continue playing or conclude the game. The game should handle user inputs by converting them to lowercase and notifying users if their choice is valid or invalid. Display the player's score at the end of the game.
import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'win'
    else:
        return 'lose'

def play_game():
    player_score = 0

    while True:
        print("\n--- New Round ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'win':
            print("You won this round!")
            player_score += 1
        elif result == 'lose':
            print("You lost this round.")
        else:
            print("It's a tie!")

        print(f"Your current score: {player_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\n--- Game Over ---")
    print(f"Your final score: {player_score}")

if __name__ == "__main__":
    play_game()
