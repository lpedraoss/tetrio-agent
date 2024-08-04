class Message():
    def __init__(self):
        self.help = "Available commands:\n  load - Load the models\n  start - Start the game (models must be loaded first)\n  help - Show this help message\n  exit - Exit the program"
        self.error_models = "Error: Models need to be loaded before starting the game."
        self.start_game = "Starting the game..."
        self.exit = "Exit"
        self.do_exit = "Are you sure you want to exit?"
        self.name_tetris = "Tetris Bot"
        self.GUI = " GUI"
        self.do_load_models = "Load Models"
        self.do_start_game = "Start Game"
        self.do_help = "Help"
        self.success_models = "Models loaded successfully!"
        self.stop_game = "Stopping the game..."
        self.do_stop_game = "Stop Game"