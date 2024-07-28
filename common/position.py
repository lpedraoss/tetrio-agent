import pyautogui
import pyscreeze

# Obtener la posición actual del cursor del mouse
x, y = pyautogui.position()

# Obtener el color del píxel en la posición del cursor
pixel_color = pyscreeze.pixel(x, y)

print(f"La posición del cursor es: ({x}, {y})")
print(f"El color del píxel en la posición del cursor es: {pixel_color}")
