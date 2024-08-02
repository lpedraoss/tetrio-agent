import unittest
import numpy as np
from agent.base_board import BaseBoard
from tetris.pieces import pieces

class TestBaseBoard(unittest.TestCase):
    def setUp(self):
        self.board = BaseBoard()

    def test_initial_board(self):
        self.assertTrue(np.array_equal(self.board.board, np.zeros((40, 10), dtype=np.uint8)))

    def test_moveInBoard_center(self):
        self.assertEqual(self.board.moveInBoard(direction='center'), 2)

    def test_moveInBoard_left(self):
        self.assertEqual(self.board.moveInBoard(times=1, direction='left'), 1)

    def test_moveInBoard_right(self):
        self.assertEqual(self.board.moveInBoard(times=1, direction='right', piece=np.array([[1, 1]])), 2)

    def test_detectCollision_no_collision(self):
        piece = np.array([[1, 1], [1, 1]])
        self.assertFalse(self.board.detectCollision(0, 0, piece))

    def test_detectCollision_with_collision(self):
        piece = np.array([[1, 1], [1, 1]])
        self.board.addPiece(0, 0, piece)
        self.assertTrue(self.board.detectCollision(0, 0, piece))

    def test_addPiece(self):
        piece = np.array([[1, 1], [1, 1]])
        self.board.addPiece(0, 0, piece)
        expected_board = np.zeros((40, 10), dtype=np.uint8)
        expected_board[0:2, 0:2] = piece
        self.assertTrue(np.array_equal(self.board.board, expected_board))

    def test_checkLines(self):
        self.board.board[0] = 1
        self.board.checkLines()
        self.assertTrue(np.array_equal(self.board.board[0], np.zeros(10, dtype=np.uint8)))

    def test_increase_height(self):
        self.board.increase_height(0)
        self.assertEqual(self.board.current_height, 8)

    def test_generateMoves(self):
        moves = self.board.generateMoves('i')
        self.assertTrue(len(moves) > 0)

    def test_pressAdd(self):
        self.board.pressAdd('i', 0, 0, 'center')
        self.assertTrue(np.any(self.board.board))

    def test_copy(self):
        new_board = self.board.copy()
        self.assertTrue(np.array_equal(self.board.board, new_board.board))
        self.assertEqual(self.board.current_height, new_board.current_height)
        self.assertEqual(self.board.MAX_HEIGHT, new_board.MAX_HEIGHT)

if __name__ == '__main__':
    unittest.main()