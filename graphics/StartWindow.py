import pygame
import sys
from classes.button import Button
from classes.DJ import DJ
from REST_API import REST_API


class StartWindow:
    _instance = None
    Screen = None
    Background = pygame.image.load("assets/Background.png")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.DJ = DJ("assets/Music/Lobby_Music.mp3")

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
        response = REST_API.get_leaderboard()
        while True:
            pygame.display.set_caption("Salón de la Fama")
            leaderboardMousePosition = pygame.mouse.get_pos()

            self.Screen.fill("white")

            leadearboardText = self.GetFont(45).render("LEADERBOARD", True, "Black")
            leadearboardRectangle = leadearboardText.get_rect(center=(720, 100))

            userlabel = self.GetFont(30).render("Username", True, "Black")
            userlabelrect = leadearboardText.get_rect(center=(500, 200))

            timelabel = self.GetFont(30).render("Best time (s)", True, "Black")
            timelabelrect = leadearboardText.get_rect(center=(1100, 200))

            for i, (nombre, numero, _) in enumerate(response[:5]):
                y = 250 + i * 50
                usernamelabel = self.GetFont(30).render(f"{nombre}", True, "Black")
                usernamerect = leadearboardText.get_rect(center=(500, y))

                timelabelp = self.GetFont(30).render(f"{numero}", True, "Black")
                timerect = leadearboardText.get_rect(center=(1100, y))

                self.Screen.blit(usernamelabel, usernamerect)
                self.Screen.blit(timelabelp, timerect)

            self.Screen.blit(userlabel, userlabelrect)
            self.Screen.blit(timelabel, timelabelrect)
            self.Screen.blit(leadearboardText, leadearboardRectangle)

            leadearboardBack = Button(image=None, pos=(720, 600),
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        REST_API.get_player_saves('marco@gmail.com', 0)


            pygame.display.update()

    def MainScreen(self):
        running = True
        pygame.init()  # starts it
        self.Screen = pygame.display.set_mode((1440, 810))  # To set the parameters of the window
        pygame.display.set_caption("Eagle Defender")  # Window Title
        if not self.DJ.isPlaying():
            self.DJ.PlayLobbyMusic()

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
                        return "Game"
                    if registerButton.CheckForInput(menuMousePosition):
                        pass
                    if leaderboardButton.CheckForInput(menuMousePosition):
                        pass
                    if helpButton.CheckForInput(menuMousePosition):
                        pass
                    if quitButton.CheckForInput(menuMousePosition):
                        pygame.quit()
                        sys.exit()
                    # When the text is clicked it goes to the specific page
            pygame.display.update()
