"""
A module for managing game state history.
"""

class GameStateHistory:
    def __init__(self):
        self._history = []

    def add_state(self, state):
        """
        Adds a new game state to the history.

        :param state: The game state to add.
        """
        self._history.append(state)

    def get_previous_state(self):
        """
        Retrieves the previous game state.

        :return: The previous game state if available, else None.
        """
        if len(self._history) > 1:
            return self._history[-2]
        return None

    def revert_to_state(self, index):
        """
        Reverts to a specific state in the history based on the provided index.

        :param index: The index of the state to revert to.
        :return: The reverted state if the index is valid, else None.
        """
        if 0 <= index < len(self._history):
            self._history = self._history[:index+1]
            return self._history[-1]
        return None
