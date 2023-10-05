from GameWindow import GameWindow
from StartWindow import StartWindow
from LogInWindow import LogInWindow
from HelpWindow import HelpWindow
from RegisterWindow import RegisterWindow

if __name__ == "__main__":
    helpWindow = HelpWindow()
    #logInWindow = LogInWindow() de momento llamo a gamewindow en lugar de login para probarlo
    registerWindow = RegisterWindow()
    gameWindow = GameWindow()
    startWindow = StartWindow(helpWindow, gameWindow, registerWindow)
    startWindow.MainScreen()
