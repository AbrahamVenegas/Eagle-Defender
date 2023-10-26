from graphics.StartWindow import StartWindow
from graphics.LogInWindow import LogInWindow
from graphics.HelpWindow import HelpWindow
from graphics.RegisterWindow import RegisterWindow
from graphics.GameWindow import GameWindow

if __name__ == "__main__":
    gameWindow = GameWindow()
    helpWindow = HelpWindow()
    logInWindow = LogInWindow()
    registerWindow = RegisterWindow()
    startWindow = StartWindow(helpWindow, gameWindow, registerWindow)
    startWindow.MainScreen()
