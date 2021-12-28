import numpy as np


class Grid:
    """
    Class representing the grid of the HexWar.
    """
    def __init__(self, size):
        self._size = size
        self._grid = np.zeros(shape=(self._size, self._size))

    def get_size(self):
        return self._size

    def set_hex(self, player, coordinate):
        self._grid[coordinate[1], coordinate[0]] = player

    def get_hex(self, coordinate):
        return self._grid[coordinate[1], coordinate[0]]

    def get_grid(self):
        return self._grid

    def neighbors(self, coordinates):
        neighbors = []
        directions = [[0, -1], [1, -1], [1, 0], [0, 1], [-1, 1], [-1, 0]]

        for dir in directions:
            new_coordinates = [coordinates[0]+dir[0], coordinates[1]+dir[1]]
            if 0 <= new_coordinates[0] < self._size and 0 <= new_coordinates[1] < self._size:
                neighbors.append(new_coordinates)

        return neighbors

    def check_win(self, player):
        """
       Check the winning condition for a player.
       :return: True or False
       """
        neighbors = []
        if player == 1:
            for y in range(self.get_size()):
                if self.get_hex([0, y]) == 1:
                    neighbors.append([0, y])
        else:
            for x in range(self.get_size()):
                if self.get_hex([x, 0]) == 2:
                    neighbors.append([x, 0])

        if len(neighbors) == 0:
            return False

        # Checking if Player won
        for neighbor in neighbors:
            potential_neighbors = self.neighbors(neighbor)
            for next_neighbor in potential_neighbors:
                if self.get_hex(next_neighbor) == player and (next_neighbor not in neighbors):
                    if next_neighbor[player-1] == self.get_size() - 1:
                        return True
                    else:
                        neighbors.append(next_neighbor)

        return False

    def free_moves(self):
        possible_moves = []
        for x in range(self._size):
            for y in range(self._size):
                if self.get_hex([x, y]) == 0:
                    possible_moves.append([x, y])
        return possible_moves