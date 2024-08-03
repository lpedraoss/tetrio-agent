
from core.agent.base_board import BaseBoard
from core.tetris.pieces import pieces
from core.tetris.rotation import checkRotation
import numpy as np
from core.agent.heuristic import Heuristic
from concurrent.futures import ThreadPoolExecutor

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

    def evaluate_move(self, move):
        """
        Evaluates a single move.

        Args:
            move (tuple): A move to evaluate.

        Returns:
            tuple: The move and its score.
        """
        testing = self.baseBoard.copy()
        piece, rot, direction, t, move_column = move
        initial = move_column
        final = move_column + len(pieces[piece][rot][0]) - 1
        testing.pressAdd(piece=piece, times=t, rotation=rot, direction=direction)
        score = self.heuristic.calculate_heuristics(board=testing.board, initial=initial, final=final)['score']
        return move, score

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

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self.evaluate_move, moves))

        for move, score in results:
            print('movimiento: {}, con puntaje de {}'.format(move, score))
            if score <= best_score:
                best_score = score
                best_move = move

        print(f"Selected best move: {best_move} with score {best_score}")
        return best_move

    def predictMove(self, piece):
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

    def startGame(self, piece):
        """
        Starts the game and makes the best move for the given piece.

        Args:
            piece (str): The piece to make the move for.

        Returns:
            tuple: The best move as a tuple of (piece, rot, direction, t, move_column).
        """
        move = self.predictMove(piece=piece)
        piece, rot, direction, t, move_column = move
        # Realizar la jugada
        self.baseBoard.pressAdd(piece=piece, rotation=rot, direction=direction, times=t)
        
        print('La mejor jugada es:', move)           
        self.baseBoard.showBoard()
        return move