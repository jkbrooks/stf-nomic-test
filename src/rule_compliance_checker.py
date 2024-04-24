# This class is responsible for checking the compliance of player actions with the active rules in a Nomic game.

from typing import List


class RuleComplianceChecker:
    def __init__(self, nomic_game):
        self.nomic_game = nomic_game
        self.active_rules = []

    def register_rule_change(self, rule):
        """Register a new rule or update an existing one."""
        # Check if the rule already exists
        for i, active_rule in enumerate(self.active_rules):
            if active_rule.id == rule.id:
                self.active_rules[i] = rule
                return
        # If the rule is new, add it to the list
        self.active_rules.append(rule)

    def check_action_compliance(self, action) -> bool:
        """Check if an action complies with the active rules."""
        for rule in self.active_rules:
            if not rule.is_compliant(action):
                return False
        return True

    def get_active_rules(self) -> List:
        """Return a list of active rules."""
        return self.active_rules
