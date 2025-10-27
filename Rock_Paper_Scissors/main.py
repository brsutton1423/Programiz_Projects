play_again = "yes"
from player import get_user_input
from computer import get_computer_choice
from game_logic import determine_winner
def get_emoji(choice):
    EMOJI_MAP = {"rock":"✊","paper":"👋","scissors":"✌️"}
    if choice in EMOJI_MAP:
        return EMOJI_MAP[choice]
    else:
        return None
def welcome_user():
    print("Welcome to Rock, Paper, Scissors!")
player_score = 0
computer_score = 0
while play_again == "yes":
    welcome_user()
    valid_choices = ["rock","paper","scissors"]
    user_choice = get_user_input(valid_choices)
    print(f"You chose: {get_emoji(user_choice)}")
    computer_choice = get_computer_choice(valid_choices)
    print(f"Computer chose: {get_emoji(computer_choice)}")
    result = determine_winner(user_choice,computer_choice)
    print(result)
    if result == "You win!":
        player_score +=1
    elif result == "You lose!":
        computer_score +=1
    play_again = input("Do you want to play again? (yes/no): ")
print(f"Your score: {player_score}\nComputer score: {computer_score}")
print("Thank you for playing")