import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar PIL para redimensionar la imagen
from core.agent.agent import Agent
from core.agent.base_board import BaseBoard
from core.agent.tetrio_bot import TetrioBot
from core.tetris.predictor_colors import load_models_torch
from common.message import Message

# Variable para rastrear el estado de los modelos
models_loaded = False
bot_running = False
bot = TetrioBot()
mssg = Message()

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
    print(mssg.success_models)
    print('<-------------------------------->')
    # Cambiar el color del círculo a verde
    canvas.itemconfig(circle, fill='green')
    messagebox.showinfo(title= mssg.do_load_models, message = mssg.success_models)


def play_game():
    global bot_running, bot
    if not models_loaded:
        clear_console()
        print(mssg.error_models)
        print('<-------------------------------->')
        messagebox.showinfo(title = 'Error',message = mssg.error_models)
        return
    else:
        clear_console()
        print(mssg.start_game)
        print('<-------------------------------->')
        bot_running = True
        # Cambiar el color del círculo a rojo
        canvas.itemconfig(circle, fill='red')
        messagebox.showinfo(title = mssg.do_start_game , message = mssg.start_game)
        bot.play()


def stop_game():
    global bot_running, bot
    if bot_running and bot:
        bot_running = False
        # Cambiar el color del círculo a gris
        canvas.itemconfig(circle, fill='grey')
        messagebox.showinfo(title = mssg.do_stop_game , message = mssg.stop_game)
        bot.stop()  # Asegúrate de que TetrioBot tenga un método stop
        clear_console()
        print(mssg.stop_game)
        print('<-------------------------------->')
    


def show_help():
    messagebox.showinfo(title = mssg.do_help,message = mssg.help)

def exit_program():
    confirm = messagebox.askyesno(mssg.exit, mssg.do_exit)
    if confirm:
        root.destroy()

def start_gui():
    global root, canvas, circle
    # Crear la ventana principal
    root = tk.Tk()
    root.title(mssg.name_tetris + mssg.GUI)

    # Configurar la posición de la ventana en la parte izquierda de la pantalla
    root.geometry("+0+0")

    # Hacer la ventana inmutable
    root.resizable(False, False)

    # Mantener la ventana siempre en primer plano
    root.attributes("-topmost", True)

    # Cargar y redimensionar la imagen
    image = Image.open("./assets/bot.png")  # Reemplaza con la ruta de tu imagen
    image = image.resize((50, 50), Image.LANCZOS)  # Ajustar el tamaño de la imagen
    header_image = ImageTk.PhotoImage(image)

    # Crear un Label para la imagen del header
    header_label = tk.Label(root, image=header_image)
    header_label.image = header_image  # Mantener una referencia de la imagen
    header_label.pack(side="bottom", fill="x")
    
    # Crear un Canvas para el círculo
    canvas = tk.Canvas(root, width=50, height=50)
    canvas.pack(pady=20)
    # Dibujar un círculo gris
    circle = canvas.create_oval(10, 10, 40, 40, fill='grey')

    # Crear botones
    load_button = tk.Button(root, text=mssg.do_load_models, command=load_models)
    start_button = tk.Button(root, text=mssg.do_start_game, command=play_game)
    stop_button = tk.Button(root, text=mssg.do_stop_game, command=stop_game)

    # Colocar los botones en la ventana
    load_button.pack(pady=10)
    start_button.pack(pady=10)
    stop_button.pack(pady=10)

    # Ejecutar el bucle principal de tkinter
    root.mainloop()

