import sys
import pygame
import requests
from button import Button
from StartWindow import StartWindow
from GameWindow import GameWindow


def GetFont(size):
    return pygame.font.Font("assets/font.ttf", size)


class LogInWindow:
    inputRect1 = None
    inputRect2 = None
    inputRect3 = None
    inputRect4 = None
    color_passive = None
    inputColor = None
    baseFont = None
    background = None
    rect = None
    screen = None

    def __init__(self):
        self.width = 800
        self.height = 576
        self.p1UsernameFlag = self.p1PasswordFlag = False
        self.p2UsernameFlag = self.p2PasswordFlag = False
        self.p1Username = self.p2Username = ''
        self.p1Password = self.p2Password = ''
        self.hiddenPassword1 = self.hiddenPassword2 = ''
        self.p1UsernameRect = self.p1PasswordRect = None
        self.p2UsernameRect = self.p2PasswordRect = None
        self.username = "Email:"
        self.password = "Password:"
        self.LogIn1 = self.LogIn2 = False
        self.logIn1Failed = self.logIn2Failed = False
        self.bothLoggedIn = False
        self.gameWindow = GameWindow()

    def Start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.inputRect1 = pygame.Rect(15, 200, 350, 50)
        self.inputRect2 = pygame.Rect(15, 350, 350, 50)
        self.inputRect3 = pygame.Rect(415, 200, 350, 50)
        self.inputRect4 = pygame.Rect(415, 350, 350, 50)
        self.color_passive = pygame.Color(178, 183, 191)
        self.inputColor = pygame.Color((178, 183, 191))
        self.baseFont = pygame.font.Font(None, 25)
        self.background = pygame.image.load("assets/LogInBG.png")
        self.rect = pygame.image.load("assets/MediumRectangle.png")
        pygame.display.set_caption("Eagle Defender")

        while True:
            self.screen.blit(self.background, (0, 0))
            pygame.draw.line(surface=self.screen, start_pos=(self.width / 2, 0), end_pos=(self.width / 2, self.height),
                             color=(0, 0, 0), width=5)

            self.p1UsernameRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect1, 3)
            self.p1PasswordRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect2, 3)
            self.p2UsernameRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect3, 3)
            self.p2PasswordRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect4, 3)
            self.Player1LogIn()
            self.Player2LogIn()

            back = Button(image=None, pos=(740, 550),
                          textInput="BACK", font=GetFont(25), baseColor="White", hoveringColor="Green")

            back.ChangeColor(self.mousePos)
            back.UpdateScreen(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.p1UsernameRect.collidepoint(event.pos):
                        self.p1UsernameFlag = True
                    else:
                        self.p1UsernameFlag = False

                    if self.p1PasswordRect.collidepoint(event.pos):
                        self.p1PasswordFlag = True
                    else:
                        self.p1PasswordFlag = False

                    if self.p2UsernameRect.collidepoint(event.pos):
                        self.p2UsernameFlag = True
                    else:
                        self.p2UsernameFlag = False

                    if self.p2PasswordRect.collidepoint(event.pos):
                        self.p2PasswordFlag = True
                    else:
                        self.p2PasswordFlag = False

                    if self.logInButton1.CheckForInput(self.mousePos) and not self.LogIn1:
                        self.VerifyLogIn(player1=True, player2=False)

                    if self.logInButton2.CheckForInput(self.mousePos) and not self.LogIn2:
                        self.VerifyLogIn(player2=True, player1=False)

                    if back.CheckForInput(self.mousePos):
                        startWindow = StartWindow._instance
                        startWindow.MainScreen()

                if event.type == pygame.KEYDOWN:
                    if self.p1UsernameFlag:
                        if event.key == pygame.K_BACKSPACE:
                            self.p1Username = self.p1Username[:-1]
                        else:
                            self.p1Username += event.unicode

                    if self.p1PasswordFlag:
                        if event.key == pygame.K_BACKSPACE:
                            self.p1Password = self.p1Password[:-1]
                            self.hiddenPassword1 = self.hiddenPassword1[:-1]
                        else:
                            self.p1Password += event.unicode
                            self.hiddenPassword1 += '*'

                    if self.p2UsernameFlag:
                        if event.key == pygame.K_BACKSPACE:
                            self.p2Username = self.p2Username[:-1]
                        else:
                            self.p2Username += event.unicode

                    if self.p2PasswordFlag:
                        if event.key == pygame.K_BACKSPACE:
                            self.p2Password = self.p2Password[:-1]
                            self.hiddenPassword2 = self.hiddenPassword2[:-1]
                        else:
                            self.p2Password += event.unicode
                            self.hiddenPassword2 += '*'

            pygame.display.update()

    def Player1LogIn(self):
        self.screen.blit(self.rect, (15, 10))
        logInText = GetFont(40).render("PLAYER 1", True, (0, 0, 0))
        usernameText = GetFont(20).render(self.username, True, (0, 0, 0))
        passwordText = GetFont(20).render(self.password, True, (0, 0, 0))
        self.screen.blit(logInText, (15 + 25, 10 + 40))
        self.screen.blit(usernameText, (15, 170))
        self.screen.blit(passwordText, (15, 320))

        usernameSurface = self.baseFont.render(self.p1Username, True, self.inputColor)
        self.screen.blit(usernameSurface, (self.p1UsernameRect.x + 5, self.p1UsernameRect.y + 15))

        passwordSurface = self.baseFont.render(self.hiddenPassword1, True, self.inputColor)
        self.screen.blit(passwordSurface, (self.p1PasswordRect.x + 5, self.p1PasswordRect.y + 15))

        if not self.LogIn1:
            self.mousePos = pygame.mouse.get_pos()
            self.logInButton1 = Button(image=None, pos=(180, 450),
                                       textInput="LOG IN", font=GetFont(30), baseColor="Black", hoveringColor="Green")
            self.logInButton1.ChangeColor(self.mousePos)
            self.logInButton1.UpdateScreen(self.screen)
        else:
            Text1 = GetFont(30).render("LOGGED IN", True, (0, 0, 0))
            self.screen.blit(Text1, (50, 440))

        if self.logIn1Failed:
            Text = GetFont(14).render("INVALID EMAIL OR PASSWORD", True, (255, 0, 0))
            self.screen.blit(Text, (20, 280))

        if usernameSurface.get_width() > self.p1UsernameRect.w:
            self.p1Username = self.p1Username[:-1]
        elif passwordSurface.get_width() > self.p1PasswordRect.w:
            self.p1Password = self.p1Password[:-1]

    def Player2LogIn(self):
        self.screen.blit(self.rect, (415, 10))
        logInText = GetFont(40).render("PLAYER 2", True, (0, 0, 0))
        usernameText2 = GetFont(20).render(self.username, True, (0, 0, 0))
        passwordText2 = GetFont(20).render(self.password, True, (0, 0, 0))
        self.screen.blit(logInText, (400 + 15 + 25, 10 + 40))
        self.screen.blit(usernameText2, (415, 170))
        self.screen.blit(passwordText2, (415, 320))

        usernameSurface2 = self.baseFont.render(self.p2Username, True, self.inputColor)
        self.screen.blit(usernameSurface2, (self.p2UsernameRect.x + 5, self.p2UsernameRect.y + 15))

        passwordSurface = self.baseFont.render(self.hiddenPassword2, True, self.inputColor)
        self.screen.blit(passwordSurface, (self.p2PasswordRect.x + 5, self.p2PasswordRect.y + 15))

        if not self.LogIn2:
            self.mousePos = pygame.mouse.get_pos()
            self.logInButton2 = Button(image=None, pos=(400 + 180, 450),
                                       textInput="LOG IN", font=GetFont(30), baseColor="Black", hoveringColor="Green")
            self.logInButton2.ChangeColor(self.mousePos)
            self.logInButton2.UpdateScreen(self.screen)
        else:
            Text1 = GetFont(30).render("LOGGED IN", True, (0, 0, 0))
            self.screen.blit(Text1, (450, 440))

        if self.logIn2Failed:
            Text = GetFont(14).render("INVALID EMAIL OR PASSWORD", True, (255, 0, 0))
            self.screen.blit(Text, (420, 280))

        if usernameSurface2.get_width() > self.p2UsernameRect.w:
            self.p2Username = self.p2Username[:-1]
        elif passwordSurface.get_width() > self.p2PasswordRect.w:
            self.p2Password = self.p2Password[:-1]

    def VerifyLogIn(self, player1, player2):
        urlp1 = "http://127.0.0.1:5000/api/loginp1"
        urlp2 = "http://127.0.0.1:5000/api/loginp2"
        headers = {'Content-Type': 'application/json'}
        if player1:
            data = {
                "email": self.p1Username,
                "password": self.p1Password
            }
            response = requests.post(urlp1, headers=headers, json=data)
            if response.status_code == 201:
                self.LogIn1 = True
                self.logIn1Failed = False

            elif response.status_code == 401:
                self.logIn1Failed = True

        elif player2:
            data = {
                "email": self.p2Username,
                "password": self.p2Password
            }
            response = requests.post(urlp2, headers=headers, json=data)
            if response.status_code == 201:
                self.LogIn2 = True
                self.logIn2Failed = False
            elif response.status_code == 401:
                self.logIn2Failed = True

        if self.LogIn2 and self.LogIn1:
            self.gameWindow.Start()
