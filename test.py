#from tictactoe import initial_state
from tictactoe import player
from tictactoe import actions
from tictactoe import result
from tictactoe import winner
from tictactoe import terminal
from tictactoe import utility
from tictactoe import minimax
from tictactoe import maxvalue
from tictactoe import minvalue
EMPTY = None
X = "X"
board = [["X", EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]


print(minimax(board))