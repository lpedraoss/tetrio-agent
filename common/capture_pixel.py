import time
import pyscreeze
from tetris.predictor_colors import find_colors_tetris_piece

def capture_colors():
    # Coordenadas de los píxeles de las piezas
    x1, y1 = (945, 178)
    x2, y2 = (945, 257)
    x3, y3 = (945, 353)
    x4, y4 = (943, 451)
    x5, y5 = (945, 544)

    # Coordenadas del píxel del tablero
    board_pixel_x, board_pixel_y = (664, 66)
    last_pixel_color = pyscreeze.pixel(board_pixel_x, board_pixel_y)
    color6 = pyscreeze.pixel(board_pixel_x, board_pixel_y)

    # Obtener las piezas basadas en los colores
    pieza6 = find_colors_tetris_piece(color6)
    # Imprimir las piezas capturadas
    print(f'La pieza 6 es:{color6} <==> {pieza6}')
    while True:
        current_pixel_color = pyscreeze.pixel(board_pixel_x, board_pixel_y)
        
        if current_pixel_color != last_pixel_color:
            last_pixel_color = current_pixel_color

            # Capturar los colores de las piezas
            color1 = pyscreeze.pixel(x1, y1)
            color2 = pyscreeze.pixel(x2, y2)
            color3 = pyscreeze.pixel(x3, y3)
            color4 = pyscreeze.pixel(x4, y4)
            color5 = pyscreeze.pixel(x5, y5)

            # Obtener las piezas basadas en los colores
            pieza1 = find_colors_tetris_piece(color1)
            pieza2 = find_colors_tetris_piece(color2)
            pieza3 = find_colors_tetris_piece(color3)
            pieza4 = find_colors_tetris_piece(color4)
            pieza5 = find_colors_tetris_piece(color5)

            print(f'La pieza 1 es: {pieza1}')
            print(f'La pieza 2 es: {pieza2}')
            print(f'La pieza 3 es: {pieza3}')
            print(f'La pieza 4 es: {pieza4}')
            print(f'La pieza 5 es: {pieza5}')
            print('<-------------------------->')
        # Pequeño retraso para evitar un alto uso de la CPU
        time.sleep(0.01)

