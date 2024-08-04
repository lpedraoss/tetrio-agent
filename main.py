from logging import root
import os
import tkinter as tk
import readline
from tkinter import messagebox
from cli.cli_main import start_cli
from core.agent.agent import Agent
from core.agent.base_board import BaseBoard
from core.agent.tetrio_bot import TetrioBot
from core.tetris.predictor_colors import load_models_torch
import sys

from gui.gui_main import start_gui

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
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'cli':
            start_cli()
        elif sys.argv[1] == 'gui':
            start_gui()
        else:
            print("Usage: python main.py [cli|gui]")
    else:
        print("Usage: python main.py [cli|gui]")

if __name__ == "__main__":
    main()    

