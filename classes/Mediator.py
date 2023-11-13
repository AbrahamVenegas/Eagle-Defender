from graphics.StartWindow import StartWindow
from graphics.LogInWindow import LogInWindow
from graphics.HelpWindow import HelpWindow
from graphics.RegisterWindow import RegisterWindow
from graphics.GameWindow import GameWindow


class Mediator:
    startWindow = StartWindow()
    logInWindow = LogInWindow()
    helpWindow = HelpWindow()
    registerWindow = RegisterWindow()
    gameWindow = GameWindow()
    stack = []

    def run(self):
        change = self.startWindow.StartScreen()
        while True:
            if change == "Start":
                change = self.startWindow.StartScreen()
            if change == "Help":  # Albert
                pass
            elif change == "Leaderboard":
                pass
            elif change == "Login":  # Albert
                pass
            elif change == "Register":  # Albert
                pass
            elif change == "Game":
                pass
            elif change == "Pause":
                pass
            elif change == "SaveMenu":
                pass
            elif change == "LoadMenu":
                pass
            elif change == "Quit":
                break


