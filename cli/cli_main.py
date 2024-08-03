import os
from core.agent.tetrio_bot import TetrioBot
from core.tetris.predictor_colors import load_models_torch

# Variable para rastrear el estado de los modelos
models_loaded = False

def clear_console():
    """Limpia la consola basada en el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_models():
    global models_loaded
    clear_console()
    print('<-------------------------------->')
    print("Loading models...")
    load_models_torch()
    models_loaded = True
    print('<-------------------------------->')
    print("Models loaded successfully!")
    print('<-------------------------------->')

def play_game():
    if not models_loaded:
        clear_console()
        print("Error: Models need to be loaded before starting the game.")
        print('<-------------------------------->')
        return
    else:
        clear_console()
        print("Starting the game...")
        print('<-------------------------------->')
        bot = TetrioBot()
        bot.play()

def show_help():
    print("Available commands:")
    print("  load - Load the models")
    print("  start - Start the game (models must be loaded first)")
    print("  help - Show this help message")
    print("  exit - Exit the program")

def start_cli():
    while True:
        command = input("Enter command (load/start/help/exit): ").strip().lower()
        if command == 'load':
            load_models()
        elif command == 'start':
            play_game()
        elif command == 'help':
            show_help()
        elif command == 'exit':
            print("Exiting the program...")
            break
        else:
            print("Invalid command. Type 'help' to see the list of available commands.")