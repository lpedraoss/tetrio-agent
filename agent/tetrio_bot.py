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
        """
        Mueve la pieza en la dirección especificada un número determinado de veces.
        
        Args:
        dir (str): La dirección en la que mover la pieza ('left', 'right', 'center').
        times (int): El número de veces que mover la pieza en la dirección especificada.
        """
        if dir != 'center':
            for _ in range(times):
                pyautogui.press(dir)
                time.sleep(0.01)
    
    def rota(self, times):
        """
        Rota la pieza un número determinado de veces.
        
        Args:
        times (int): El número de veces que rotar la pieza.
        """
        for _ in range(times):
            pyautogui.press('x')
            time.sleep(0.01)
    
    def moveInBoard(self, dir, times, rotation):
        """
        Mueve y rota la pieza dentro del tablero.
        
        Args:
        dir (str): La dirección en la que mover la pieza ('left', 'right', 'center').
        times (int): El número de veces que mover la pieza en la dirección especificada.
        rotation (int): El número de veces que rotar la pieza.
        """
        self.rota(times=rotation)
        self.moveDir(times=times, dir=dir)
        time.sleep(0.01)
    
    def capturePieceColors(self):
        """
        Captura los colores de los píxeles de las piezas actuales.
        
        Returns:
        List: Una lista de los colores de las piezas.
        """
        pieces = []
        color1 = pyscreeze.pixel(self.x1, self.y1)
        color2 = pyscreeze.pixel(self.x2, self.y2)
        color3 = pyscreeze.pixel(self.x3, self.y3)
        color4 = pyscreeze.pixel(self.x4, self.y4)
        color5 = pyscreeze.pixel(self.x5, self.y5)
        piece1 = find_colors_tetris_piece(color1)
        piece2 = find_colors_tetris_piece(color2)
        piece3 = find_colors_tetris_piece(color3)
        piece4 = find_colors_tetris_piece(color4)
        piece5 = find_colors_tetris_piece(color5)
        pieces.append(piece1)
        time.sleep(0.01)
        pieces.append(piece2)
        time.sleep(0.01)
        pieces.append(piece3)
        time.sleep(0.01)
        pieces.append(piece4)
        time.sleep(0.01)
        pieces.append(piece5)
        time.sleep(0.01)
        
        print('color detectado: ',color1,' ==> {}'.format(piece1))
        print('color detectado: ',color2,' ==> {}'.format(piece2))
        print('color detectado: ',color3,' ==> {}'.format(piece3))
        print('color detectado: ',color4,' ==> {}'.format(piece4))
        print('color detectado: ',color5,' ==> {}'.format(piece5))
        
        return pieces

    def play(self):
        """
        Inicia el juego y controla las piezas basándose en los colores capturados.
        """
        # Capture initial piece colors
        initial_pieces = self.capturePieceColors()
        for piece in initial_pieces:
            self.queue.put(piece)
            time.sleep(0.01)
        
        while True:
            # Check if a new piece has appeared on the board by detecting a color change
            current_pixel_color = pyscreeze.pixel(self.board_pixel_x, self.board_pixel_y)
            if current_pixel_color != self.color_board:
                time.sleep(0.01)
                piece = self.queue.get()
                time.sleep(0.01)
                move = self.agent.startGame(piece=piece)
                piece, rot, direction, t, move_column = move
                self.moveInBoard(dir=direction, rotation=rot, times=t)
                print('{*********************************}')
                print('pieza a jugar: {}'.format(piece))
                print('{*********************************}')
                while True:
                    # Capture the color of the new piece and add it to the queue
                    new_piece_color = pyscreeze.pixel(self.x5, self.y5)
                    print('color nuevo: ', new_piece_color)
                    
                    new_piece = find_colors_tetris_piece(new_piece_color)
                    if new_piece != "board":
                        break
                self.queue.put(new_piece)
                print('<----------------------------->')
                print('captura el color')
                print('pieza a añadir', new_piece)
                print('<----------------------------->')
                
                time.sleep(3)
                pyautogui.press('space')
                
            # Small delay to avoid high CPU usage
            time.sleep(0.01)
