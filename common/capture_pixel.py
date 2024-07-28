from PIL import ImageGrab

# Captura una captura de pantalla
screenshot = ImageGrab.grab()

# Coordenadas del píxel
x, y = (945, 252)

# Obtener el color del píxel
color = screenshot.getpixel((x, y))
print(f'El color del píxel en ({x}, {y}) es: {color}')
