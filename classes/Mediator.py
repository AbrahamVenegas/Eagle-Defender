from graphics.StartWindow import StartWindow
from graphics.LogInWindow import LogInWindow
from graphics.HelpWindow import HelpWindow
from graphics.RegisterWindow import RegisterWindow
from graphics.GameWindow import GameWindow
from graphics.PauseWindow import PauseWindow
from graphics.SaveMenu import SaveMenu
from graphics.LoadMenu import LoadMenu
from graphics.FinishWindow import FinishWindow
from graphics.SettingsWindow import SettingsWindow


class Mediator:
    startWindow = StartWindow()
    logInWindow = LogInWindow()
    helpWindow = HelpWindow()
    registerWindow = RegisterWindow()
    pauseWindow = PauseWindow()
    saveMenu = SaveMenu()
    loadMenu = LoadMenu()
    gameWindow = None
    finishWindow = FinishWindow()
    settingsWindow = SettingsWindow()


    def run(self):
        change = [self.startWindow.MainScreen()]
        while True:
            if change[0] == "Start":
                change = [self.startWindow.MainScreen()]
            if change[0] == "Help":
                if len(change) == 1:
                    change = self.helpWindow.HelpScreen(0, 0, 0)
                elif len(change) == 4:
                    change = self.helpWindow.HelpScreen(1, change[2], change[3])
            elif change[0] == "Login":
                change = self.logInWindow.Start()
            elif change[0] == "Register":
                change = self.registerWindow.RegisterScreen()
            elif change[0] == "Game":
                if len(change) == 2: # Pause llama a GameWindow
                    change = self.gameWindow.Start()
                elif len(change) == 3: # Load llama GameWindow
                    self.gameWindow.LoadGame()
                    change = self.gameWindow.Start()
                else:
                    self.gameWindow = GameWindow()
                    self.gameWindow.Reset()
                    change = self.gameWindow.Start()
            elif change[0] == "Pause":
                change = self.pauseWindow.pause_game(change[1], change[2])
            elif change[0] == "SaveMenu":
                change = self.saveMenu.showMenu(change[1], change[2], change[3])
            elif change[0] == "LoadMenu":
                change = self.loadMenu.showLoadMenu()
            elif change[0] == "Finish":
                change = self.finishWindow.FinishGame(change[1], change[2], change[3])
            elif change[0] == "Settings":
                change = self.settingsWindow.showSettings()
            elif change[0] == "Quit":
                break


