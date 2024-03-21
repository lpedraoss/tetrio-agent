import pyautogui
import pyscreeze
from tetris.colors import determine_tetris_piece

from agent.agent import Agent
from queue import Queue

class TetrioBot():
    def __init__(self) -> None:
        pass        
    def moveDir(self,dir,times):
        if dir != 'center':
            count = 1
            while count <= times:
                pyautogui.press(dir)
                count+=1
    def rota(self,times):
        if times != 0:
            count = 1
            while count <= times:
                pyautogui.press('x')
                count += 1
    def moveInBoard(self,dir, times, rotation):
        self.rota(times=rotation)     
        self.moveDir(times=times,dir=dir)
        
    
    def play(self):
        
        agent = Agent()
        x1,y1 =(877, 197)
        x2,y2 = (877, 269)
        x3,y3 =  (877, 341) 
        x4,y4 = (877, 412)
        x5,y5 = (876, 485) 

        pixel_color1 = pyscreeze.pixel(x1, y1)
        pixel_color2 = pyscreeze.pixel(x2, y2)
        pixel_color3 = pyscreeze.pixel(x3, y3)
        pixel_color4 = pyscreeze.pixel(x4, y4)
        pixel_color5 = pyscreeze.pixel(x5, y5)

        piece = determine_tetris_piece(pixel_color1)
        queue =  Queue()
        queue.put(piece)
        piece = determine_tetris_piece(pixel_color2)
        queue.put(piece)
        piece = determine_tetris_piece(pixel_color3)
        queue.put(piece)
        piece = determine_tetris_piece(pixel_color4)
        queue.put(piece)
        piece = determine_tetris_piece(pixel_color5)
        queue.put(piece)

        while True:
            pixel_board = pyscreeze.pixel(671, 172)
            if pixel_board != (0,0,0):

                piece = queue.get()
                print('pieza a jugar: {}'.format(piece))
                move = agent.startGame(piece=piece)
                piece, rot, direction, t, move_column = move                
                self.moveInBoard(dir=direction, rotation=rot, times=t)
                pixel_color5 = pyscreeze.pixel(x5, y5)
                piece = determine_tetris_piece(pixel_color5)
                queue.put(piece)
                print('captura el color')
                print('pieza a añadir',piece)
                pyautogui.press('space')

