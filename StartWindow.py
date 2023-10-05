import pygame
import sys
from button import Button


class StartWindow:
    _instance = None
    helpWindow = None
    logInWindow = None
    Screen = None
    Background = pygame.image.load("assets/Background.png")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, helpWindow, logInWindow, registerWindow):
        self.helpWindow = helpWindow
        self.logInWindow = logInWindow
        self.registerWindow = registerWindow

    def GetFont(self, size):  # To return it in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def StartScreen(self):
        while True:
            pygame.display.set_caption("Inicio de Sesión")  # To change the title of the window
            playMousePosition = pygame.mouse.get_pos()
            # To obtain the position of the mouse, this will be changed for the joystick later
            self.Screen.fill("black")

            playText = self.GetFont(45).render("This is the LOG IN screen.", True, "White")
            playRectangle = playText.get_rect(center=(720, 260))
            # To add text to the screen
            self.Screen.blit(playText, playRectangle)

            playBack = Button(image=None, pos=(720, 460),
                              textInput="BACK", font=self.GetFont(75), baseColor="White", hoveringColor="Green")
            # Button Escape to go back to the last screen
            playBack.ChangeColor(playMousePosition)
            playBack.UpdateScreen(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playBack.CheckForInput(playMousePosition):
                        self.MainScreen()

            pygame.display.update()

    def LeaderboardScreen(self):
        while True:
            pygame.display.set_caption("Salón de la Fama")
            leaderboardMousePosition = pygame.mouse.get_pos()

            self.Screen.fill("white")

            leadearboardText = self.GetFont(45).render("This is the LEADERBOARD screen.", True, "Black")
            leadearboardRectangle = leadearboardText.get_rect(center=(720, 260))
            self.Screen.blit(leadearboardText, leadearboardRectangle)

            leadearboardBack = Button(image=None, pos=(720, 460),
                                      textInput="BACK", font=self.GetFont(75), baseColor="Black", hoveringColor="Green")

            leadearboardBack.ChangeColor(leaderboardMousePosition)
            leadearboardBack.UpdateScreen(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if leadearboardBack.CheckForInput(leaderboardMousePosition):
                        self.MainScreen()

            pygame.display.update()

    def MainScreen(self):
        running = True
        pygame.init()  # starts it
        self.Screen = pygame.display.set_mode((1440, 810))  # To set the parameters of the window
        pygame.display.set_caption("Eagle Defender")  # Window Title

        while running:
            self.Screen.blit(self.Background, (0, 0))

            menuMousePosition = pygame.mouse.get_pos()

            menuText = self.GetFont(50).render("EAGLE DEFENDER", True, "#b68f40")
            menuRectangle = menuText.get_rect(center=(720, 100))

            playButton = Button(image=pygame.image.load("assets/MediumRectangle.png"), pos=(720, 215),
                                textInput="START", font=self.GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
            registerButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 340),
                                    textInput="¡REGISTER!", font=self.GetFont(50), baseColor="#d7fcd4",
                                    hoveringColor="Purple")
            leaderboardButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 465),
                                       textInput="LEADERBOARD", font=self.GetFont(50), baseColor="#d7fcd4",
                                       hoveringColor="Purple")
            helpButton = Button(image=pygame.image.load("assets/MediumRectangle.png"), pos=(720, 590),
                                textInput="HELP", font=self.GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
            quitButton = Button(image=pygame.image.load("assets/QuitRectangle.png"), pos=(720, 715),
                                textInput="QUIT", font=self.GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
            # Set the button for each Screen

            self.Screen.blit(menuText, menuRectangle)

            for button in [playButton, registerButton, leaderboardButton, quitButton, helpButton]:
                button.ChangeColor(menuMousePosition)
                button.UpdateScreen(self.Screen)
            # Changes the color when the mouse is on top of the text

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if playButton.CheckForInput(menuMousePosition):
                        running = False
                        pygame.quit()
                        self.logInWindow.Start()
                    if registerButton.CheckForInput(menuMousePosition):
                        self.registerWindow.RegisterScreen()
                    if leaderboardButton.CheckForInput(menuMousePosition):
                        self.LeaderboardScreen()
                    if helpButton.CheckForInput(menuMousePosition):
                        self.helpWindow.HelpScreen()
                    if quitButton.CheckForInput(menuMousePosition):
                        pygame.quit()
                        sys.exit()
                    # When the text is clicked it goes to the specific page
            pygame.display.update()
