from graphics.StartWindow import StartWindow
from graphics.LogInWindow import LogInWindow
from graphics.HelpWindow import HelpWindow
from graphics.RegisterWindow import RegisterWindow
from graphics.GameWindow import GameWindow
from graphics.PauseWindow import PauseWindow
from graphics.SaveMenu import SaveMenu


class Mediator:
    startWindow = StartWindow()
    logInWindow = LogInWindow()
    helpWindow = HelpWindow()
    gameWindow = GameWindow()
    registerWindow = RegisterWindow()
    pauseWindow = PauseWindow()
    saveMenu = SaveMenu()
    username = email = player = flag = Game = None
    varList = []
    stack = []

    def run(self):
        change = [self.startWindow.MainScreen()]
        while True:
            if change[0] == "Start":
                pass
            if change[0] == "Help":  # Albert
                pass
            elif change[0] == "Leaderboard":
                pass
            elif change[0] == "Login":  # Albert
                pass
            elif change[0] == "Register":  # Albert
                pass
            elif change[0] == "Game":
                change = self.gameWindow.Start()
            elif change[0] == "Pause":
                change = self.pauseWindow.pause_game(change[1], change[2])
            elif change[0] == "SaveMenu":
                change = self.saveMenu.showMenu(change[1], change[2], change[3])
            elif change[0] == "LoadMenu":
                pass
            elif change[0] == "Quit":
                break


