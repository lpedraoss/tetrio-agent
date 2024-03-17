import pyscreeze
import pyautogui
x1 = 848
y1 = 232
x2 = 846
y2 = 296
x3 = 845
y3 = 354
x4 = 848
y4 = 556
x5 = 845
y5 = 588
# Obtener la posición actual del puntero
x, y = pyautogui.position()

# Obtener el color del píxel en esa posición
pixel_color = pyscreeze.pixel(x, y) 

print(f"Posición del puntero: ({x}, {y})")
print(f"Color del píxel en esa posición: {pixel_color}")
