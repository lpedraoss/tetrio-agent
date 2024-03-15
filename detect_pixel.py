import pyscreeze
import pyautogui

# Obtener la posición actual del puntero
x, y = pyautogui.position()

# Obtener el color del píxel en esa posición
pixel_color = pyscreeze.pixel(x, y)

print(f"Posición del puntero: ({x}, {y})")
print(f"Color del píxel en esa posición: {pixel_color}")
