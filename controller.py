from grid import Grid
from gui import GUI


class Controller:
    """
    Class Controller.
    The controller manage the Hex game itself, ad how the player plays one after each other.
    """
    def __init__(self, size, player1, player2):
        self._grid = Grid(size)
        self._player1 = player1
        self._player2 = player2
        self._current_player = 1
        self._winner = 0

    def update(self):
        """
        Update method.
        This method check which player is supposed to play
        and call the function :func:`~Player.Player.step`
        of the class Player that decide what moves will be played.
        """
        if self._current_player == 1:
            # Call the methods steps that will return the move of Player 1.
            coordinates = self._player1.step()
            # Modify the grid with the new move.
            self._grid.set_hex(self._current_player, coordinates)
            self._current_player = 2
            self._player2.update(coordinates)
        else:
            # Call the methods steps that will return the move of Player 2.
            coordinates = self._player2.step()
            # Modify the grid with the new move.
            self._grid.set_hex(self._current_player, coordinates)
            self._current_player = 1
            self._player1.update(coordinates)

        self._check_win()

    def _check_win(self):
        """
        Check the winning condition for both player.
        """

        neighbors1 = []
        neighbors2 = []
        for y in range(self._grid.get_size()):
            if self._grid.get_hex([0, y]) == 1:
                neighbors1.append([0, y])

        for x in range(self._grid.get_size()):
            if self._grid.get_hex([x, 0]) == 2:
                neighbors2.append([x, 0])

        if len(neighbors1) == 0 and len(neighbors2) == 0:
            return

        # Checking if Player 1 won
        for neighbor in neighbors1:
            neighbors = self._grid.neighbors(neighbor)
            for next_neighbor in neighbors:
                if self._grid.get_hex(next_neighbor) == 1 and (next_neighbor not in neighbors1):
                    if next_neighbor[0] == self._grid.get_size()-1:
                        self._winner = 1
                        self._player1.calc_average_time(1)
                        self._player2.calc_average_time(2)
                        self._player1.calc_total_time()
                        return
                    else:
                        neighbors1.append(next_neighbor)

        # Check if Player 2 won.
        for neighbor in neighbors2:
            neighbors = self._grid.neighbors(neighbor)
            for next_neighbor in neighbors:
                if self._grid.get_hex(next_neighbor) == 2 and (next_neighbor not in neighbors2):
                    if next_neighbor[1] == self._grid.get_size()-1:
                        self._winner = 2
                        self._player1.calc_average_time(1)
                        self._player2.calc_average_time(2)
                        self._player2.calc_total_time()
                        return
                    else:
                        neighbors2.append(next_neighbor)

