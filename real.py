import pyautogui
import keyboard
import pyscreeze
from pieces import colores_tetris
import time
from virtual import Tetrio
from queue import Queue
def moveDir(dir,times):
    if dir != 'center':
        count = 1
        while count <= times:
            pyautogui.press(dir)
            count+=1
def rota(times):
    if times != 0:
        count = 1
        while count <= times:
            pyautogui.press('x')
            count += 1
             
def moveInBoard(dir, times, rotation):
    rota(times=rotation)     
    moveDir(times=times,dir=dir)
    pyautogui.press('space')

tetris = Tetrio()
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

piece = colores_tetris[pixel_color1]
queue =  Queue()
queue.put(piece)
piece = colores_tetris[pixel_color2]
queue.put(piece)
piece = colores_tetris[pixel_color3]
queue.put(piece)
piece = colores_tetris[pixel_color4]
queue.put(piece)
piece = colores_tetris[pixel_color5]
queue.put(piece)

while True:
    pixel_board = pyscreeze.pixel(671, 172)
    if pixel_board != (0,0,0):
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
        piece = queue.get()
        print('pieza a jugar: {}'.format(piece))
        move = tetris.startGame(piece=piece)
        piece, rot, direction, t, move_column = move
        pixel_color5 = pyscreeze.pixel(x5, y5)
        piece = colores_tetris[pixel_color5]
        queue.put(piece)
        print('captura el color')
        print('pieza a añadir',piece)
        moveInBoard(dir=direction, rotation=rot, times=t)
        #time.sleep(0.5)

