import unittest
from  core.agent.base_board import BaseBoard
from core.agent.heuristic import Heuristic
from core.agent.agent import Agent
import numpy as np

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()

    def test_initialization(self):
        self.assertIsInstance(self.agent.baseBoard, BaseBoard)
        self.assertIsInstance(self.agent.heuristic, Heuristic)

    def test_evaluate_move(self):
        move = ('t', 0, 'center', 0, 0)
        move, score = self.agent.evaluate_move(move)
        self.assertIsInstance(score, (int, float))

    def test_selectBestMove(self):
        moves = [
            ('t', 0, 'center', 0, 0),
            ('t', 1, 'left', 1, 1),
            ('t', 2, 'right', 2, 2)
        ]
        best_move = self.agent.selectBestMove(moves)
        self.assertIn(best_move, moves)

    def test_predictMove(self):
        piece = 't'
        best_move = self.agent.predictMove(piece)
        self.assertIsInstance(best_move, tuple)
        self.assertEqual(len(best_move), 5)

    def test_startGame(self):
        piece = 't'
        best_move = self.agent.startGame(piece)
        self.assertIsInstance(best_move, tuple)
        self.assertEqual(len(best_move), 5)

if __name__ == '__main__':
    unittest.main()