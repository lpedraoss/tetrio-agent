from agent.agent import Agent
from agent.tetrio_bot import TetrioBot
from tetris.predictor_colors import load_models_torch

def main():
    """load_models_torch()
    print('<--------------------->')
    input('press Enter to continue')
    print('<--------------------->')
    
    bot = TetrioBot()
    bot.play()
    """
    tet = Agent()
    ##tet.pressAdd(piece='s',times=0,dir='right',rotation=0)
    #tet.pressAdd(piece='l',times=0,dir='right',rotation=0)
    #tet.pressAdd(piece='z',times=0,dir='right',rotation=0)
    
    #tet.showBoard()
    tet.startGame(piece='o')
    tet.startGame(piece='s')
    tet.startGame(piece='l')
    tet.startGame(piece='s')
    tet.startGame(piece='z')
    tet.startGame(piece='l')
    
    
if __name__ == "__main__":
    main()
