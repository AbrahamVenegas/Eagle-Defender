<<<<<<< HEAD
from GameWindow import GameWindow
=======
>>>>>>> origin/Log-In-Screen
from StartWindow import StartWindow
from LogInWindow import LogInWindow
from HelpWindow import HelpWindow
from RegisterWindow import RegisterWindow

if __name__ == "__main__":
    helpWindow = HelpWindow()
<<<<<<< HEAD
    #logInWindow = LogInWindow() de momento llamo a gamewindow en lugar de login para probarlo
    registerWindow = RegisterWindow()
    gameWindow = GameWindow()
    startWindow = StartWindow(helpWindow, gameWindow, registerWindow)
=======
    logInWindow = LogInWindow()
    registerWindow = RegisterWindow()
    startWindow = StartWindow(helpWindow, logInWindow, registerWindow)
>>>>>>> origin/Log-In-Screen
    startWindow.MainScreen()
