from StartWindow import StartWindow
from LogInWindow import LogInWindow
from HelpWindow import HelpWindow
from RegisterWindow import RegisterWindow
from GameWindow import GameWindow

if __name__ == "__main__":
    gameWindow = GameWindow()
    helpWindow = HelpWindow()
    logInWindow = LogInWindow()
    registerWindow = RegisterWindow()
    startWindow = StartWindow(helpWindow, gameWindow, registerWindow)
    startWindow.MainScreen()
