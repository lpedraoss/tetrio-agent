import time
from agent.base_board import BaseBoard
from tetris.pieces import pieces
from tetris.rotation import checkRotation
import numpy as np
from agent.heuristic import Heuristic
from agent.test_board import  TestBoard
class Agent(BaseBoard):

    def __init__(self):
        super().__init__()
        self.board = np.zeros((20, 10), dtype=int)
        self.heuristic = Heuristic()

        
    def selectBestMove(self, moves):
        # Evaluar cada movimiento usando la heurística y seleccionar el mejor
        best_move = None
        best_score = float('inf')
        test = TestBoard()
        for move in moves:
            self.board_test = np.copy(self.board)
            piece, rot, direction, t, move_column = move
            initial = move_column
            final = move_column + len(pieces[piece][rot][0]) - 1
            test.pressAdd(piece=piece,times=t,rotation=rot,dir=direction,board=self.board_test)
            score = self.heuristic.calculate_heuristics(self.board_test, initial, final)['score']
            self.board_test = None
            if score <= best_score:
                best_score = score
                best_move = move
        return best_move

    def predictMove(self,piece):
        moves = self.generateMoves(piece=piece)    
        best_move = self.selectBestMove(moves=moves)
        return best_move

    def startGame(self,piece):
        move = self.predictMove(piece=piece)
        piece, rot, direction, t, move_column = move
        # Realizar la jugada
        self.pressAdd(piece=piece, rotation=rot, dir=direction, times=t)
        print('La mejor jugada es:', move)           
        self.showBoard()
        heuristic =  Heuristic()
        heur = heuristic.calculate_heuristics(board=self.board,initial=move_column,final=move_column+(len(pieces[piece][rot])-1))
        print('heuristica: ',heur)

        print(len(self.board))
        return move

