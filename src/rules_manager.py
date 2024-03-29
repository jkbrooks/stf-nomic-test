# Import the Rule class from rule.py
from rule import Rule

# RulesManager class to manage Rule objects using a hash map
class RulesManager:
    def __init__(self):
        # Initialize a dictionary to store Rule objects by their ID
        self.rules = {}

    def add_rule(self, rule):
        # Add a Rule object to the dictionary
        # The Rule object's ID is used as the key
        if isinstance(rule, Rule) and rule.id not in self.rules:
            self.rules[rule.id] = rule

    def remove_rule(self, rule_id):
        # Remove a Rule object from the dictionary by its ID
        if rule_id in self.rules:
            del self.rules[rule_id]

    def get_rule(self, rule_id):
        # Retrieve a Rule object by its ID
        return self.rules.get(rule_id, None)
