import numpy as np

from Players.Player import Player


class RandomPlayer(Player):
    def __init__(self, size):
        super().__init__(size, 0, 0)
        self.name = "Random"
        self._possible_moves = []

        for x in range(self._size):
            for y in range(self._size):
                self._possible_moves.append([x, y])

    def step(self):
        move = self._possible_moves[np.random.choice(len(self._possible_moves))]
        self._possible_moves.remove(move)
        return move

    def update(self, move_other_player):
        self._possible_moves.remove(move_other_player)