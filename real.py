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
            time.sleep(.5)   
def moveInBoard(dir, times, rotation):
    rota(times=rotation)     
    moveDir(times=times,dir=dir)
    pyautogui.press('space')

tetris = Tetrio()
x1 = 848
y1 = 232
x2 = 851
y2 = 290
x3 = 846
y3 = 354
x4 = 850
y4 = 412
x5 = 844
y5 = 472
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
        piece = queue.get()
        print('esta pieza es: {}'.format(piece))
        pixel_color5 = pyscreeze.pixel(x5, y5)
        move = tetris.startGame(piece=piece)
        piece, rot, direction, t, move_column = move
        time.sleep(2)
        moveInBoard(dir=direction, rotation=rot, times=t)
        time.sleep(0.3)
        print('captura el color')
        piece = colores_tetris[pixel_color5]
        queue.put(piece)
        print('pieza a añadir',piece)

"""
piece = colores_tetris[pixel_color3]
piece = colores_tetris[pixel_color4]
queue =  Queue()
queue.put(piece)
piece = colores_tetris[pixel_color5]
queue.put(piece)


while True:
    pixel_color = pyscreeze.pixel(x, y)
    pixel_board = pyscreeze.pixel(672, 173)
    
    if pixel_board != (0, 0, 0):
        print('captura el color')
        piece = colores_tetris[pixel_color]
        print('esta pieza es: {}'.format(piece))
        move = tetris.startGame(piece=piece)
        piece, rot, direction, t, move_column = move
        time.sleep(0.3)
        moveInBoard(dir=direction, rotation=rot, times=t)
        time.sleep(0.3)
    
    time.sleep(0.1)  # Agregar una pausa breve al final del bucle
"""