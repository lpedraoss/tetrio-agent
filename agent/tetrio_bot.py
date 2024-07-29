import time
import pyautogui
import pyscreeze
from queue import Queue
from tetris.predictor_colors import find_colors_tetris_piece
from agent.agent import Agent
from tetris.pixel import pixels

class TetrioBot():
    def __init__(self) -> None:
        self.agent = Agent()
        self.queue = Queue()
        
        # Initialize pixel positions
        self.x1, self.y1 = pixels[1]
        self.x2, self.y2 = pixels[2]
        self.x3, self.y3 = pixels[3]
        self.x4, self.y4 = pixels[4]
        self.x5, self.y5 = pixels[5]
        
        # Initialize board pixel position
        self.board_pixel_x = 664
        self.board_pixel_y = 66
        self.color_board = (0,0,0) 
        #pyscreeze.pixel(self.board_pixel_x, self.board_pixel_y)

    def moveDir(self, dir, times):
        if dir != 'center':
            for _ in range(times):
                pyautogui.press(dir)
    
    def rota(self, times):
        for _ in range(times):
            pyautogui.press('x')
    
    def moveInBoard(self, dir, times, rotation):
        self.rota(times=rotation)
        self.moveDir(times=times, dir=dir)
    
    def capturePieceColors(self):
        pieces = []
        pieces.append(find_colors_tetris_piece(pyscreeze.pixel(self.x1, self.y1)))
        pieces.append(find_colors_tetris_piece(pyscreeze.pixel(self.x2, self.y2)))
        pieces.append(find_colors_tetris_piece(pyscreeze.pixel(self.x3, self.y3)))
        pieces.append(find_colors_tetris_piece(pyscreeze.pixel(self.x4, self.y4)))
        pieces.append(find_colors_tetris_piece(pyscreeze.pixel(self.x5, self.y5)))
        return pieces

    def play(self):
        # Capture initial piece colors
        initial_pieces = self.capturePieceColors()
        for piece in initial_pieces:
            self.queue.put(piece)
        
        while True:
            # Check if a new piece has appeared on the board by detecting a color change
            current_pixel_color = pyscreeze.pixel(self.board_pixel_x, self.board_pixel_y)
            if current_pixel_color != self.color_board:
                piece = self.queue.get()
                print('pieza a jugar: {}'.format(piece))
                move = self.agent.startGame(piece=piece)
                piece, rot, direction, t, move_column = move
                self.moveInBoard(dir=direction, rotation=rot, times=t)
                while True:
                    # Capture the color of the new piece and add it to the queue
                    new_piece_color = pyscreeze.pixel(self.x5, self.y5)
                    new_piece = find_colors_tetris_piece(new_piece_color)
                    if new_piece != "board":
                        break
                self.queue.put(new_piece)
                print('captura el color')
                print('pieza a añadir', new_piece)
                time.sleep(1)
                pyautogui.press('space')
                
            # Small delay to avoid high CPU usage
            time.sleep(0.01)
