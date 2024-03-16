import pyscreeze
from pieces import colores_tetris
x = 848
y = 232
pixel_color = pyscreeze.pixel(x, y)

print(f"Posición del píxel: ({x}, {y})")
print(f"Color del píxel en esa posición: {pixel_color}")

piece = colores_tetris[pixel_color]
print('esta pieza es: {}'.format(piece))