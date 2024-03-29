# This class is responsible for checking the compliance of player actions with the current set of active rules.

class RuleComplianceChecker:
    def __init__(self):
        # Initialize with a list of active rules
        self.active_rules = []

    def add_rule(self, rule):
        # Add a new rule to the list of active rules
        self.active_rules.append(rule)

    def check_compliance(self, player_action):
        # Check if the player action complies with all the active rules
        for rule in self.active_rules:
            if not rule.is_compliant(player_action):
                return False
        return True

    def prevent_non_compliant_actions(self, player_action):
        # Automatically prevent actions that violate the rules
        if not self.check_compliance(player_action):
            print(f'Action {player_action} is not allowed as per the current rules.')
            return False
        print(f'Action {player_action} is allowed.')
        return True
