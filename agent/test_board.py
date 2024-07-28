from agent.base_board import BaseBoard
from tetris.pieces import pieces
from tetris.rotation import checkRotation
import numpy as np
from agent.heuristic import Heuristic

class TestBoard(BaseBoard):

    def __init__(self):
        super().__init__()
        self.board = np.zeros((40, 10), dtype=int)
        self.board_test=None
        #self.board = board
        self.checkRotation = checkRotation
        self.piece = None
        self.height = None
        self.current_height = 4
        self.MAX_HEIGHT = 20
        self.width = None 
        self.rotations = None  
        self.heuristic = Heuristic()
