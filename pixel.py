from PIL import ImageGrab
import time
import pyautogui as py
def startDetection(pixel):
    # Obtener el color inicial del pixel
    color_inicial = colorPixel(pixel[0], pixel[1])

    while True:
        # Obtener el color actual del pixel
        color_actual = colorPixel(pixel[0], pixel[1])

        # Verificar si el color ha cambiado para el pixel actual
        if color_actual != color_inicial:
            print(f"¡Se ha detectado un cambio en el pixel {pixel}!")
            

            # Esperar un segundo antes de realizar las acciones
            time.sleep(1) 

            # Simular las teclas presionadas (dos veces a la izquierda, una vez arriba, una vez espacio)
            moveToLeft(3)
            moveToRight(5)
            rotate90(2)
            py.press('space')

            # Actualizar el color inicial para ese pixel
            color_inicial = color_actual

        # Pausa para evitar un bucle infinito demasiado rápido
        time.sleep(1)
def colorPixel(x, y):
    pantalla = ImageGrab.grab()
    color = pantalla.getpixel((x, y))
    return color
def moveToLeft(steps=1):
    for _ in range(steps):
        py.press('left')
def moveToRight(steps=1):
    for _ in range(steps):
        py.press('right')

def rotate90(steps=1):
    for _ in range(steps):
        py.press('up')
def rotate180(steps=1):
    for _ in range(steps):
        py.press('a')

#pixel = (670, 224)
pixel = (671, 189)
startDetection(pixel)
