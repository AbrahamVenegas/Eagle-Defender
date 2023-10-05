from StartWindow import StartWindow
from LogInWindow import LogInWindow
from HelpWindow import HelpWindow
from RegisterWindow import RegisterWindow

if __name__ == "__main__":
    helpWindow = HelpWindow()
    logInWindow = LogInWindow()
    registerWindow = RegisterWindow()
    startWindow = StartWindow(helpWindow, logInWindow, registerWindow)
    startWindow.MainScreen()
