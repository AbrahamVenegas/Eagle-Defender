import sys
import pygame


def GetFont(size):
    return pygame.font.Font("assets/font.ttf", size)


class LogInWindow:

    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 576
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.rect = pygame.image.load("assets/MediumRectangle.png")
        self.p1UsernameFlag = self.p1PasswordFlag = False
        self.p2UsernameFlag = self.p2PasswordFlag = False
        self.p1Username = self.p2Username = ''
        self.p1Password = self.p2Password = ''
        self.hiddenPassword1 = self.hiddenPassword2 = ''
        self.inputRect1 = pygame.Rect(15, 200, 350, 50)
        self.inputRect2 = pygame.Rect(15, 350, 350, 50)
        self.inputRect3 = pygame.Rect(415, 200, 350, 50)
        self.inputRect4 = pygame.Rect(415, 350, 350, 50)
        self.p1UsernameRect = self.p1PasswordRect = None
        self.p2UsernameRect = self.p2PasswordRect = None
        self.color_passive = pygame.Color(178, 183, 191)
        self.username = "Username:"
        self.password = "Password:"
        self.baseFont = pygame.font.Font(None, 25)
        background = pygame.image.load("assets/LogInBG.png")
        pygame.display.set_caption("Eagle Defender")

        while True:
            self.screen.blit(background, (0, 0))
            pygame.draw.line(surface=self.screen, start_pos=(self.width/2, 0), end_pos=(self.width/2, self.height), color=(0, 0, 0), width=5)

            self.p1UsernameRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect1, 3)
            self.p1PasswordRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect2, 3)
            self.p2UsernameRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect3, 3)
            self.p2PasswordRect = pygame.draw.rect(self.screen, self.color_passive, self.inputRect4, 3)
            self.Player1LogIn()
            self.Player2LogIn()

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
        self.screen.blit(logInText, (15+25, 10+40))
        self.screen.blit(usernameText, (15, 170))
        self.screen.blit(passwordText, (15, 320))

        usernameSurface = self.baseFont.render(self.p1Username, True, (178, 183, 191))
        self.screen.blit(usernameSurface, (self.p1UsernameRect.x+5, self.p1UsernameRect.y+15))

        passwordSurface = self.baseFont.render(self.hiddenPassword1, True, (178, 183, 191))
        self.screen.blit(passwordSurface, (self.p1PasswordRect.x+5, self.p1PasswordRect.y+15))

    def Player2LogIn(self):
        self.screen.blit(self.rect, (415, 10))
        logInText = GetFont(40).render("PLAYER 2", True, (0, 0, 0))
        usernameText2 = GetFont(20).render(self.username, True, (0, 0, 0))
        passwordText2 = GetFont(20).render(self.password, True, (0, 0, 0))
        self.screen.blit(logInText, (400+15+25, 10+40))
        self.screen.blit(usernameText2, (415, 170))
        self.screen.blit(passwordText2, (415, 320))

        usernameSurface2 = self.baseFont.render(self.p2Username, True, (178, 183, 191))
        self.screen.blit(usernameSurface2, (self.p2UsernameRect.x+5, self.p2UsernameRect.y+15))

        passwordSurface = self.baseFont.render(self.hiddenPassword2, True, (178, 183, 191))
        self.screen.blit(passwordSurface, (self.p2PasswordRect.x+5, self.p2PasswordRect.y+15))


LogInWindow()
