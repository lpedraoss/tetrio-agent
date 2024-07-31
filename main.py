import os
from agent.agent import Agent
from agent.base_board import BaseBoard
from agent.tetrio_bot import TetrioBot
from common.capture_pixel import capture_colors
from tetris.predictor_colors import load_models_torch

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

def tetrisCLI():
    clear_console()
    print("Tetris Bot CLI - Type 'help' for a list of commands.")

    while True:
        # Mostrar el prompt de entrada
        command = input("> ").strip().lower()

        if command == 'load':
            load_models()
        elif command == 'start':
            play_game()
        elif command == 'help' or command == "?":
            clear_console()
            print("Available commands:")
            print("  load       - Load the models")
            print("  start      - Start the game (models must be loaded first)")
            print("  exit       - Exit the program")
        elif command == 'exit':
            clear_console()
            print("Exiting...")
            break
        else:
            clear_console()
            print("Unknown command. Type 'help' for a list of commands.")

def pressAddTest():
    
    tet = BaseBoard()
    tet.pressAdd(piece='s',times=8,dir='right',rotation=0)
    tet.pressAdd(piece='z',times=2,dir='right',rotation=1)
    tet.pressAdd(piece='o',times=0,dir='center',rotation=0)
    tet.pressAdd(piece='i',times=11,dir='left',rotation=0)
    tet.pressAdd(piece='l',rotation=2,dir='center',times=0)
    tet.pressAdd(piece='t',rotation=0,dir='left',times=11)
    tet.pressAdd(piece='j',rotation=2,dir='right',times=1)
    tet.pressAdd(piece='s',rotation=1,dir='right',times=6)
    tet.pressAdd(piece='z',rotation=1,dir='left',times=10)
    tet.pressAdd(piece='o',rotation=0,dir='right',times=3)
    
    tet.showBoard()
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
    #tet.baseBoard.showBoard()
def main():

    #tetrisCLI()
    startGameTest()
    print('<----- verificando resultado con startGame ------>')

    print('<----- verificando resultado con pressAdd ------>')
    pressAddTest()
    print('<----- board verificado ------>')

    
    #capture_colors()
if __name__ == "__main__":
    main()
