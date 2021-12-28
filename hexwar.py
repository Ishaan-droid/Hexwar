from Players.MinimaxPlayer import MinimaxPlayer
from Players.MinimaxPlayer_ImprovedHeuristic import MinimaxPlayer_ImprovedHeuristic
from Players.NegmaxPlayer import NegmaxPlayer
from Players.NegmaxABPlayer import NegmaxABPlayer
from Players.NegmaxPlayer_ImprovedHeuristic import NegmaxPlayer_ImprovedHeuristic
from Players.NegmaxABPlayer_ImprovedHeuristic import NegmaxABPlayer_ImprovedHeuristic

from Players.RandomPlayer import RandomPlayer
from controller import Controller
from gui import GUI

''' 
Experiment 1 
Minmax with default heuristics vs Minmax with improved heuristics
'''
player1 = MinimaxPlayer_ImprovedHeuristic(6,2,1)
player2 = MinimaxPlayer(6, 1, 2)
# Winner - MinimaxPlayer_ImprovedHeuristic

''' 
Experiment 2 
NegMax with default heuristics vs NegMax with improved heuristics
'''
# player1 = NegmaxPlayer(6,1,2)
# player2 = NegmaxPlayer_ImprovedHeuristic(6,2,1)
# Winner - NegmaxPlayer_ImprovedHeuristic

''' 
Experiment 3
NegMax with default heuristics vs NegMax AlphaBeta with default heuristics
'''
# player1 = NegmaxPlayer(6,1,2)
# player2 = NegmaxABPlayer(6,2,1)
# Winner - NegmaxABPlayer

''' 
Experiment 4
NegMax AlphaBeta with default heuristics vs NegMax AlphaBeta with improved heuristics
'''
# player1 = NegmaxABPlayer(6,1,2)
# player2 = NegmaxABPlayer_ImprovedHeuristic(6,2,1)
# Winner - NegmaxABPlayer_ImprovedHeuristic

''' 
Experiment 5
NegMax with improved heuristics vs NegMax AlphaBeta with improved heuristics
'''
# player1 = NegmaxABPlayer_ImprovedHeuristic(6,2,1)
# player2 = NegmaxPlayer_ImprovedHeuristic(6,1,2)
# Winner - Depends who is Player - 1

''' 
Experiment 6
Minmax with improved heuristics vs NegMax AlphaBeta with improved heuristics
'''
# player1 = NegmaxABPlayer_ImprovedHeuristic(6,2,1)
# player2 = MinimaxPlayer_ImprovedHeuristic(6,1,2)
# Winner - Depends who is Player - 1


controller = Controller(6, player1, player2)
gui = GUI(controller)