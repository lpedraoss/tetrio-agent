import os
import tkinter as tk
from tkinter import messagebox
from core.agent.agent import Agent
from core.agent.base_board import BaseBoard
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
    messagebox.showinfo("Help", "Available commands:\n  load - Load the models\n  start - Start the game (models must be loaded first)\n  exit - Exit the program")

def exit_program():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

def pressAddTest():
    print('<----- verificando resultado con pressAdd ------>')
    tet = BaseBoard()
    # tet.pressAdd(piece='i', times=0, direction='center', rotation=1)

def start_gui():
    global root
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tetris Bot GUI")

    # Configurar la posición de la ventana en la parte izquierda de la pantalla
    root.geometry("+0+0")

    # Hacer la ventana inmutable
    root.resizable(False, False)

    # Mantener la ventana siempre en primer plano
    root.attributes("-topmost", True)

    # Crear botones
    load_button = tk.Button(root, text="Load Models", command=load_models)
    start_button = tk.Button(root, text="Start Game", command=play_game)
    help_button = tk.Button(root, text="Help", command=show_help)
    exit_button = tk.Button(root, text="Exit", command=exit_program)
    test_button = tk.Button(root, text="Test pressAdd", command=pressAddTest)

    # Colocar los botones en la ventana
    load_button.pack(pady=10)
    start_button.pack(pady=10)
    help_button.pack(pady=10)
    exit_button.pack(pady=10)
    test_button.pack(pady=10)

    # Ejecutar el bucle principal de tkinter
    root.mainloop()