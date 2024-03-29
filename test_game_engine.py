"""
Unit tests for the game engine, focusing on dynamic rule representation, automated rule compliance checks, and enhanced player turn logic.
"""
import unittest
from game_engine import GameEngine, Rule

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.game_engine = GameEngine()

    def test_rule_addition(self):
        self.game_engine.add_rule('rule1', lambda x: x > 10)
        self.assertIn('rule1', self.game_engine.rules, 'Rule should be added')

    def test_rule_update(self):
        self.game_engine.add_rule('rule1', lambda x: x > 10)
        self.game_engine.update_rule('rule1', lambda x: x < 5)
        self.assertEqual(self.game_engine.rules['rule1'](3), True, 'Rule update should modify rule logic')

    def test_rule_archiving(self):
        self.game_engine.add_rule('rule1', lambda x: x > 10)
        self.game_engine.archive_rule('rule1')
        self.assertNotIn('rule1', self.game_engine.active_rules, 'Archived rules should not be in active rules')

    def test_rule_compliance_check(self):
        self.game_engine.add_rule('rule1', lambda x: x > 10)
        result = self.game_engine.check_compliance(11)
        self.assertTrue(result, 'Compliance check should pass for compliant values')

    def test_enhanced_player_turn_logic(self):
        self.game_engine.add_rule('turn_rule', lambda player, turn: player == turn % 2)
        self.assertTrue(self.game_engine.check_turn(1, 3), 'Player turn logic should correctly evaluate player turns based on rules')

if __name__ == '__main__':
    unittest.main()
