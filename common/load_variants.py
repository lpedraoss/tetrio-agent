import json
import os

def load_variants(json_path):
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"El archivo {json_path} no se encuentra en la ruta especificada.")
    
    with open(json_path, 'r') as f:
        variants = json.load(f)
    
    variants = {tuple(map(int, k.split(','))): v for k, v in variants.items()}
    return variants

# Define the path to the JSON file
json_path = os.path.join(os.path.dirname(__file__), '../data/tetris_colors_variants.json')

# Load the variants
variants = load_variants(json_path)
