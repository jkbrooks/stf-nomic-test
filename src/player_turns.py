# Import necessary modules
from rule_verification import verify_rules

# Function to execute a player's turn
def execute_player_turn(player):
    print(f"\n{player}'s turn. Please follow the rules.")
    while True:
        action = input("Enter your action: ")
        if verify_rules(action):
            print("Action verified and executed.")
            break
        else:
            print("Action violates the rules. Please try again.")

# Function to prompt for rule adherence
def prompt_for_rule_adherence():
    print("Remember to adhere to the game rules!")

# Function to confirm action
def confirm_action(action):
    confirmation = input(f"Are you sure you want to perform '{action}'? (yes/no): ")
    return confirmation.lower() == 'yes'

# Main function to handle the turn logic
def main():
    player = input("Enter player's name: ")
    prompt_for_rule_adherence()
    execute_player_turn(player)

if __name__ == '__main__':
    main()
