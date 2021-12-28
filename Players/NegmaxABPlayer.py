import numpy as np

from Players.Player import Player
from grid import Grid
import copy
import datetime


class NegmaxABPlayer(Player):
    def __init__(self, size, player_number, adv_number):
        super().__init__(size, player_number, adv_number)
        self.name = "NegmaxAB"
        self._possible_moves = []
        self.node = Grid(size)
        self.store_average_action_time = []
        self.average_action_time = 0
        self.start_game_time = datetime.datetime.now()
        self.end_game_time = 0

    def step(self):
        """
        Calculate the best action to execute and execute it.
        :return: Action executed
        """
        start_time = datetime.datetime.now()
        best_move = self.node.free_moves()[0]
        best = -np.inf
        alpha = best
        for move in self.node.free_moves():
            new_node = copy.deepcopy(self.node)
            new_node.set_hex(self.player_number, move)
            value = -self.negMax(new_node, 2,-np.inf,-alpha,self.adv_number)
            if value > best:
                best = value
                best_move = move
            alpha = max(alpha, best)
        self.node.set_hex(self.player_number, best_move)
        end_time = datetime.datetime.now()
        timeForOneAction = (end_time - start_time).total_seconds()
        self.store_average_action_time.append(timeForOneAction)
        return best_move

    def update(self, move_other_player):
        """
        Update the state of the problem with the action of the other player.
        :param move_other_player: Move played by the other player.
        """
        self.node.set_hex(self.adv_number, move_other_player)

   

    def negMax(self, node, depth, alpha, beta,player):
        """
        Implement a simple version of minmax with alpha-beta.
        :param node: Node to evaluate.
        :param depth: depth remaining.
        :param alpha: value of alpha.
        :param beta: value of beta.
        :return: The value of node.
        """
        turn = 1
        if player == self.adv_number:
            turn = -1
        if node.check_win(self.player_number):
            return np.inf*turn
        if node.check_win(self.adv_number):
            return -np.inf*turn
        if depth == 0:
            return self.heuristic(node)*turn

        value = -np.inf
        if player == self.player_number:
            other_player = self.adv_number
        else:
            other_player = self.player_number
        for move in node.free_moves():
            new_node = copy.deepcopy(node)
            new_node.set_hex(player, move)
            value = max(value, -self.negMax(new_node, depth - 1,-beta,-alpha,other_player))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
           
        return value

    def heuristic(self, node):
        """
        Heurisitic function. Be careful this heuristic is far from being good or optimized.
        :param node: Current node/state
        :return: Heuristic value
        """
        return self._value_player(node, self.player_number)

    def _value_player(self, node, player):
        """ Calculate the value of the node for the current player."""
        coordinates = []
        value = 0
        for x in range(node.get_size()):
            for y in range(node.get_size()):
                if ([x, y] not in coordinates) and (node.get_hex([x, y]) == player):
                    n = self._number_connected(player, [x, y], node)
                    coordinates += n[1]
                    if n[0] > value:
                        value = n[0]
        return value

    def _number_connected(self, player, coordinate, node):
        """
        Number of hex connected to a specific hex for a specific player
        :param player: Player
        :param coordinate: coordinate of the hex
        :param node: Node/state of the game
        :return: number of hex connected
        """
        neighbors = [coordinate]
        for neighbor in neighbors:
            n = node.neighbors(neighbor)
            for next_neighbor in n:
                if self.node.get_hex(next_neighbor) == player and (next_neighbor not in neighbors):
                    neighbors.append(next_neighbor)
        return len(neighbors), []
        
    def calc_average_time(self, Player):
        for t in self.store_average_action_time:
            self.average_action_time += t
        self.average_action_time = self.average_action_time / len(self.store_average_action_time)
        return print(f'Average Time taken by Player-{Player} to execute an action {round(self.average_action_time,4)} seconds.')

    def calc_total_time(self):
        self.end_game_time = datetime.datetime.now()
        total_game_time = 0
        for t in self.store_average_action_time:
            total_game_time += t
        total_game_time = (self.end_game_time - self.start_game_time).total_seconds()
        return print(f'Total time taken to complete the game {round(total_game_time,2)} seconds.')