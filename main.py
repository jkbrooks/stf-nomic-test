import random
from datetime import datetime
from RuleComplianceChecker import RuleComplianceChecker
class NomicGame:
    def __init__(self, player_names):
        self.rule_checker = RuleComplianceChecker()
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.rules = {
            "R1": Rule("Players must vote on rule changes.", True),
            "R2": Rule("A player gains points by rolling a die.", True)
        }
        self.currentPlayerIndex = 0
        self.game_over = False
        self.players = [Player(name) for name in player_names]
        class Rule:
    def __init__(self, description, active):
        self.description = description
        self.active = active
        self.versions = [(description, datetime.now())]

    def add_version(self, new_description):
        self.description = new_description
        self.versions.append((new_description, datetime.now()))

    def update_version(self, new_description):
        if self.versions:
            self.versions[-1] = (new_description, datetime.now())
            self.description = new_description

    def archive_rule(self):
        self.active = False
            "R1": Rule("Players must vote on rule changes.", False),
            "R2": Rule("A player gains points by rolling a die.", True)
        }
        self.currentPlayerIndex = 0
         self.game_over = False
    def take_turn(self):
        player = self.players[self.currentPlayerIndex]
        print(f"{player.name}'s turn:")
        
        proposed_rule_description = input(f'{player.name}, propose a new rule or press enter to skip: ')
        if proposed_rule_description:
            proposed_rule = Rule(proposed_rule_description, True)
        else:
            return
        if proposed_rule_description and not self.rule_checker.check_compliance(proposed_rule.description):
            print("Proposed rule does not comply with current rules.")
            return
        proposal_passed = False
        if proposed_rule_description:
            proposal_passed = self.conduct_vote(proposed_rule)
        
        if proposal_passed:
            print(f"Proposal passed. Implementing new rule: {proposed_rule}")
            self.rules[f"R{len(self.rules) + 1}"] = Rule(proposed_rule, True)
        else:
            print("Proposal failed.")
        
        points = self.roll_die()
        print(f"{player.name} rolls a die and gains {points} points.")
        player.score += points
        print(f"{player.name}'s score is now: {player.score}\n")
        
        self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)
        if any(player.score >= 100 for player in self.players) and self.currentPlayerIndex == 0:
            self.game_over = True
    
    def roll_die(self):
        return random.randint(1, 6)
    
    def conduct_vote(self, proposed_rule):
        print('Voting on proposed rule: ' + proposed_rule.description)
        votes_for = 0
        for p in self.players:
            vote = input(f'{p.name}, vote for the rule change. Yes/No: ').lower()
            if vote == 'yes':
                votes_for += 1
        votes_against = len(self.players) - votes_for
        votes_against = len(self.players) - votes_for
        print(f'Votes for: {votes_for}, Votes against: {votes_against}')
        return votes_for > votes_against
        return votes_for > len(self.players) / 2

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def propose_rule(self):
        # For the sake of this example, return a static proposed rule
        return "Example proposed rule."
    
    def vote(self, proposed_rule):
        # Randomly vote for the proposal for the sake of this example
        return random.choice([True, False])

class Rule:
    def __init__(self, description, is_mutable):
        self.description = description
        self.is_mutable = is_mutable
def load_player_names_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            valid_names = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f'Error: The file {file_path} was not found.')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []
    return valid_names
    
        name = input('Enter player name (or type "done" to finish): ').strip()
        if name.lower() == 'done' and valid_names:
            break
        elif len(name) > 20 or not name.isalnum() or name == '':
            print('Invalid name. Please ensure the name is alphanumeric, not too long, and not empty.')
        else:
            valid_names.append(name)
    return valid_names

def main():
    choice = input('Do you want to load player names from a file? (yes/no): ').strip().lower()
    if choice == 'yes':
        file_path = input('Enter the file path: ')
        player_names = load_player_names_from_file(file_path)
    else:
        player_names = []
        while True:
            name = input('Enter player name (or type "done" to finish): ').strip()
            if name.lower() == 'done' and player_names:
                break
            elif len(name) > 20 or not name.isalnum() or name == '':
                print('Invalid name. Please ensure the name is alphanumeric, not too long, and not empty.')
            else:
                player_names.append(name)
    game = NomicGame(player_names)
    while not game.game_over:
        game.take_turn()

if __name__ == "__main__":
    file_path = input('Enter the path to the player names file: ')
    player_names = load_player_names_from_file(file_path)
    if not player_names:
        print('No valid player names loaded. Exiting game.')
        exit()
    game = NomicGame(player_names)
    
    # Simulate a few turns of the game
    while not game.game_over:
        game.take_turn()
