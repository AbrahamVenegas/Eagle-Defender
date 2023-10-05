from StartWindow import StartWindow
from LogInWindow import LogInWindow
from HelpWindow import HelpWindow

if __name__ == "__main__":
    helpWindow = HelpWindow()
    logInWindow = LogInWindow()
    startWindow = StartWindow(helpWindow, logInWindow)
    startWindow.MainScreen()
