import os

import readline
from agent.agent import Agent
from agent.base_board import BaseBoard
from agent.tetrio_bot import TetrioBot
from tetris.predictor_colors import load_models_torch

# Variable para rastrear el estado de los modelos
models_loaded = False
# Definir los comandos disponibles
commands = ['load', 'start', 'help', 'exit']
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



def completer(text, state):
    options = [cmd for cmd in commands if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None
def tetrisCLI():
    readline.set_completer(completer)
    readline.parse_and_bind('tab: complete')
    
    clear_console()
    print("Tetris Bot CLI - Type 'help' for a list of commands.")

    while True:
        try:
            # Mostrar el prompt de entrada
            command = input("> ").strip().lower()

            if command == 'load':
                load_models()
                print("Models loaded successfully.")
            elif command == 'start':
                play_game()
            elif command == 'help' or command == "?":
                clear_console()
                print("Available commands:")
                print("  load       - Load the models")
                print("  start      - Start the game (models must be loaded first)")
                print("  exit       - Exit the program")
            elif command == 'exit':
                confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
                if confirm == 'y':
                    clear_console()
                    print("Exiting...")
                    break
            else:
                clear_console()
                print(f"Unknown command: '{command}'. Type 'help' for a list of commands.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
def pressAddTest():
    print('<----- verificando resultado con pressAdd ------>')
    tet = BaseBoard()
    #tet.pressAdd(piece='i',times=0,direction='center',rotation=1)
    tet.pressAdd(piece='s',times=8,direction='right',rotation=0)
    tet.pressAdd(piece='z',times=2,direction='right',rotation=1)
    tet.pressAdd(piece='o',times=0,direction='center',rotation=0)
    tet.pressAdd(piece='i',times=11,direction='left',rotation=0)
    tet.pressAdd(piece='l',rotation=2,direction='center',times=0)
    tet.pressAdd(piece='t',rotation=0,direction='left',times=11)
    tet.pressAdd(piece='j',rotation=2,direction='right',times=1)
    tet.pressAdd(piece='s',rotation=1,direction='right',times=6)
    tet.pressAdd(piece='z',rotation=1,direction='left',times=10)
    tet.pressAdd(piece='o',rotation=0,direction='right',times=3)
    tet.showBoard()
    print('<----- board verificado ------>')
def startGameTest():

    tet = Agent()
    tet.startGame(piece='s')
    tet.startGame(piece='z')
    tet.startGame(piece='o')
    tet.startGame(piece='i')
    tet.startGame(piece='l')
    tet.startGame(piece='t')
    tet.startGame(piece='j')
    tet.startGame(piece='s')
    tet.startGame(piece='z')
    tet.startGame(piece ='o')
    print('<----- verificando resultado con startGame ------>')

    
def main():

    tetrisCLI()
    #startGameTest()
    #pressAddTest()
    
if __name__ == "__main__":
    main()
