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
        self.color_board = (0, 0, 0) 

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
                time.sleep(0.005)  # Reducir el tiempo de espera
    
    def rota(self, times):
        """
        Rota la pieza un número determinado de veces.
        
        Args:
        times (int): El número de veces que rotar la pieza.
        """
        for _ in range(times):
            pyautogui.press('x')
            time.sleep(0.005)  # Reducir el tiempo de espera
    
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
        time.sleep(0.005)  # Reducir el tiempo de espera
    
    def capturePieceColors(self):
        """
        Captura los colores de los píxeles de las piezas actuales.
        
        Returns:
        List: Una lista de los colores de las piezas.
        """
        pieces = []
        colors = [pyscreeze.pixel(self.x1, self.y1), pyscreeze.pixel(self.x2, self.y2),
                  pyscreeze.pixel(self.x3, self.y3), pyscreeze.pixel(self.x4, self.y4),
                  pyscreeze.pixel(self.x5, self.y5)]
        
        for color in colors:
            piece = find_colors_tetris_piece(color)
            pieces.append(piece)
            time.sleep(0.005)  # Reducir el tiempo de espera
        
        for i, color in enumerate(colors):
            print(f'color detectado: {color} ==> {pieces[i]}')
        
        return pieces

    def play(self):
        """
        Inicia el juego y controla las piezas basándose en los colores capturados.
        """
        try:
            # Capture initial piece colors
            initial_pieces = self.capturePieceColors()
            for piece in initial_pieces:
                self.queue.put(piece)
                time.sleep(0.005)  # Reducir el tiempo de espera
            
            while True:
                # Check if a new piece has appeared on the board by detecting a color change
                current_pixel_color = pyscreeze.pixel(self.board_pixel_x, self.board_pixel_y)
                if current_pixel_color != self.color_board:
                    time.sleep(0.005)  # Reducir el tiempo de espera
                    piece = self.queue.get()
                    time.sleep(0.005)  # Reducir el tiempo de espera
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
                    
                    pyautogui.press('space')
                
                # Small delay to avoid high CPU usage
                time.sleep(0.005)  # Reducir el tiempo de espera
        except Exception as e:
            print(f"Error: {e}")