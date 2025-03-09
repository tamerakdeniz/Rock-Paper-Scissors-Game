import os
import random

from art import game_images, logo


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice():
    while True:
        try:
            choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if 0 <= choice <= 2:
                return choice
            print("Please enter a number between 0 and 2.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    clear_screen()
    print(logo)
    print("\nWelcome to Rock Paper Scissors!")
    
    user_choice = get_user_choice()
    print(f"\nYou chose:\n{game_images[user_choice]}")
    
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")
    
    # Determine winner
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

def main():
    while True:
        result = play_game()
        print(f"\n{result}")
        
        if not input("\nWould you like to play again? (y/n): ").lower().startswith('y'):
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()