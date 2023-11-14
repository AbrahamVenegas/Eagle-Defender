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
        self.Game, change = self.startWindow.MainScreen()
        while True:
            if change == "Start":
                if self.Game == "Back":
                    _, change = self.startWindow.MainScreen()
                else:
                    self.Game, change = self.startWindow.MainScreen()
            if change == "Help":  # Albert
                pass
            elif change == "Leaderboard":
                pass
            elif change == "Login":  # Albert
                pass
            elif change == "Register":  # Albert
                pass
            elif change == "Game":
                if self.Game == "Start":
                    print("Start")
                    self.gameWindow.gameState = False
                    self.username, self.email, change = self.gameWindow.Start()
                elif self.Game == "Back":
                    print("Reset")
                    self.gameWindow.Reset()
                    self.username, self.email, change = self.gameWindow.Start()
                else:
                    self.username, self.email, change = self.gameWindow.Start()
            elif change == "Pause":
                self.varList.clear()
                self.varList, self.Game, change = self.pauseWindow.pause_game(self.username, self.email)
                if not self.varList:
                    pass
                else:
                    self.player = self.varList[0]
                    self.email = self.varList[1]
                    self.flag = self.varList[2]
            elif change == "SaveMenu":
                change = self.saveMenu.showMenu(self.player, self.email, self.flag)
            elif change == "LoadMenu":
                pass
            elif change == "Quit":
                break


