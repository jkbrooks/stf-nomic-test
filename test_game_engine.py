import unittest
from game_engine import Rule, RuleComplianceChecker, Player, VotingProcess


class TestRule(unittest.TestCase):
    def test_rule_initialization(self):
        rule = Rule('Must be over 18', lambda x: x.age > 18)
        self.assertEqual(rule.description, 'Must be over 18')
        self.assertTrue(rule.condition(19))


class TestRuleComplianceChecker(unittest.TestCase):
    def test_compliance_check(self):
        rule = Rule('Must be over 18', lambda x: x.age > 18)
        checker = RuleComplianceChecker([rule])
        self.assertTrue(checker.check_compliance(19))
        self.assertFalse(checker.check_compliance(17))


class TestPlayerTurnLogic(unittest.TestCase):
    def test_player_turn(self):
        player = Player('John Doe', 20)
        self.assertEqual(player.name, 'John Doe')
        self.assertEqual(player.age, 20)
        # Assuming turn logic involves age, just as an example
        self.assertTrue(player.age >= 18)


class TestAutomatedVotingProcess(unittest.TestCase):
    def test_voting_process(self):
        voting = VotingProcess(['John', 'Jane', 'Doe'])
        voting.vote('John')
        voting.vote('Jane')
        results = voting.calculate_results()
        self.assertEqual(results['John'], 1)
        self.assertEqual(results['Jane'], 1)
        self.assertEqual(results['Doe'], 0)


if __name__ == '__main__':
    unittest.main()