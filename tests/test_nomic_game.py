import unittest
from nomic_game import NomicGame


class TestNomicGame(unittest.TestCase):
    def setUp(self):
        self.game = NomicGame()

    def test_add_rule(self):
        initial_rule_count = len(self.game.rules)
        self.game.add_rule('Players must say please to take a turn.')
        self.assertEqual(len(self.game.rules), initial_rule_count + 1)

    def test_validate_rule(self):
        self.assertTrue(self.game.validate_rule('No talking out of turn.'))
        self.assertFalse(self.game.validate_rule(''))  # Assuming empty rules are invalid

    def test_is_rule_mutable(self):
        self.game.add_rule('All players must jump once before their turn.', mutable=False)
        rule_id = list(self.game.rules.keys())[-1]
        self.assertFalse(self.game.is_rule_mutable(rule_id))

    def test_take_turn(self):
        self.game.add_player('Alice')
        self.game.take_turn('Alice', 'I wish to draw a card.')
        # Assuming some mechanism to verify turn was taken, e.g., state change

    def test_conduct_vote(self):
        self.game.add_rule('Players may draw two cards instead of one.')
        rule_id = list(self.game.rules.keys())[-1]
        self.game.conduct_vote(rule_id, {'Alice': True, 'Bob': False, 'Charlie': True})
        # Assuming some mechanism to verify vote outcome, e.g., rule enabled/disabled

    def test_game_flow_integration(self):
        # Simulate a series of turns with rule proposals and votes
        self.game.add_player('Alice')
        self.game.add_player('Bob')
        self.game.add_rule('Players must draw a card at the start of their turn.')
        for player in ['Alice', 'Bob']:
            self.game.take_turn(player, 'Propose rule change.')
            rule_id = list(self.game.rules.keys())[-1]
            self.game.conduct_vote(rule_id, {player: True, 'Alice': True, 'Bob': False})
            # Verify game state changes as expected

    def test_end_to_end_game(self):
        # Run a simulated game from start to finish
        self.game.add_player('Alice')
        self.game.add_player('Bob')
        self.game.start_game()
        while not self.game.is_game_over():
            for player in self.game.players:
                self.game.take_turn(player, 'Take action.')
                # Simulate rule proposal and voting
                self.game.add_rule(f'{player} proposes a new rule.')
                rule_id = list(self.game.rules.keys())[-1]
                self.game.conduct_vote(rule_id, {player: True, 'Alice': False, 'Bob': True})
        # Verify final game state to ensure game logic and performance

if __name__ == '__main__':
    unittest.main()