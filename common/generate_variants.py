import random
import json

def generate_color_variants(base_color, num_variants=10000):
    """Genera una lista de variantes de colores basadas en un color base."""
    variants = set()
    while len(variants) < num_variants:
        # Modifica cada componente del color base con un pequeño ajuste aleatorio
        new_color = tuple(
            max(0, min(255, c + random.randint(-30, 30)))
            for c in base_color
        )
        variants.add(new_color)
    return list(variants)

def color_to_string(color):
    """Convierte una tupla de color a una cadena."""
    return f"{color[0]},{color[1]},{color[2]}"

# Colores base para las piezas del Tetris
base_colors = {
    'i': (50, 200, 150),
    'l': (190, 120, 60),
    'j': (80, 60, 160),
    'o': (200, 170, 60),
    'z': (185, 60, 60),
    's': (140, 200, 60),
    't': (175, 75, 175)
}

# Generar variantes para cada pieza
tetris_colors_variants = {}
for piece, base_color in base_colors.items():
    variants = generate_color_variants(base_color)
    print(f"Generando variantes para la pieza '{piece}': {len(variants)} variantes.")
    tetris_colors_variants.update(
        {color_to_string(color): piece for color in variants}
    )

# Guardar el diccionario en un archivo JSON
with open('tetris_colors_variants.json', 'w') as file:
    json.dump(tetris_colors_variants, file, indent=4)

print(f"El archivo 'tetris_colors_variants.json' ha sido creado con éxito con {len(tetris_colors_variants)} colores.")
