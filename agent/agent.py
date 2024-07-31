import time
from agent.base_board import BaseBoard
from tetris.pieces import pieces
from tetris.rotation import checkRotation
import numpy as np
from agent.heuristic import Heuristic
class Agent():
    """
    Represents an agent that plays the Tetris game.

    Attributes:
        baseBoard (BaseBoard}: The base board object.
        heuristic (Heuristic): The heuristic object used for evaluating moves.
    """

    def __init__(self):
        self.baseBoard = BaseBoard()
        self.heuristic = Heuristic()

    def selectBestMove(self, moves):
        """
        Selects the best move from a list of possible moves.

        Args:
            moves (list): A list of possible moves.

        Returns:
            tuple: The best move as a tuple of (piece, rot, direction, t, move_column).
        """
        best_move = None
        best_score = float('inf')
        
        for move in moves:
            # Crear una copia del tablero para probar movimientos
            testing = self.baseBoard.copy()
            piece, rot, direction, t, move_column = move
            initial = move_column
            final = move_column + len(pieces[piece][rot][0]) - 1
            testing.pressAdd( piece = piece,times = t,rotation = rot,dir = direction,board = testing.board )
            score = self.heuristic.calculate_heuristics( testing.board, initial, final )['score']
            
            if score <= best_score:
                best_score = score
                best_move = move
        return best_move

    def predictMove(self,piece):
        """
        Predicts the best move for a given piece.

        Args:
            piece (str): The piece to predict the move for.

        Returns:
            tuple: The best move as a tuple of (piece, rot, direction, t, move_column).
        """
        moves = self.baseBoard.generateMoves(piece=piece)    
        best_move = self.selectBestMove(moves=moves)
        return best_move

    def startGame(self,piece):
        """
        Starts the game and makes the best move for the given piece.

        Args:
            piece(str) The piece to make the move for.

        Returns:
            tuple: The best move as a tuple of (piece, rot, direction, t, move_column).
        """
        move = self.predictMove(piece=piece)
        piece, rot, direction, t, move_column = move
        # Realizar la jugada
        
        self.baseBoard.pressAdd(piece=piece, rotation=rot, dir=direction, times=t)
        
        print('La mejor jugada es:', move)           
        self.baseBoard.showBoard()
        heuristic =  Heuristic()
        heur = heuristic.calculate_heuristics(board=self.baseBoard.board,initial=move_column,final=move_column+(len(pieces[piece][rot])-1))
        print('heuristica: ',heur)

        print(len(self.baseBoard.board))
        return move

