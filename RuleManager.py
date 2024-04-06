class RuleManager:
    def __init__(self):
        self.rules = {}

    def add_rule(self, rule_id, rule_text):
        """Add a new rule to the rules dictionary."""
        self.rules[rule_id] = rule_text

    def remove_rule(self, rule_id):
        """Remove a rule from the rules dictionary by its identifier."""
        if rule_id in self.rules:
            del self.rules[rule_id]

    def modify_rule(self, rule_id, new_rule_text):
        """Modify an existing rule's text by its identifier."""
        if rule_id in self.rules:
            self.rules[rule_id] = new_rule_text
