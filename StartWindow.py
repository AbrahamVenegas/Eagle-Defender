import pygame
import sys
import json
from button import Button


pygame.init()  # starts it
Screen = pygame.display.set_mode((1440, 810))  # To set the parameters of the window
pygame.display.set_caption("Eagle Defender")  # Window Title
Background = pygame.image.load("assets/Background.png")  # Sets teh background of the Main Screen


def GetFont(size):  # To return it in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def StartScreen():
    while True:
        pygame.display.set_caption("Inicio de Sesión") # To change the title of the window
        playMousePosition = pygame.mouse.get_pos()
        # To obtain the position of the mouse, this will be changed for the joystick later
        Screen.fill("black")

        playText = GetFont(45).render("This is the LOG IN screen.", True, "White")
        playRectangle = playText.get_rect(center=(720, 260))
        # To add text to the screen
        Screen.blit(playText, playRectangle)

        playBack = Button(image=None, pos=(720, 460),
                           textInput="BACK", font=GetFont(75), baseColor="White", hoveringColor="Green")
        # Button Escape to go back to the last screen
        playBack.ChangeColor(playMousePosition)
        playBack.UpdateScreen(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playBack.CheckForInput(playMousePosition):
                    MainScreen()

        pygame.display.update()

def RegisterScreen():
    while True:

        """
        data = {
            'name': 'abraham',
            'password': '1234',
            'email': 'abravenegas@estudiantec.cr',
            'age': '20',
            'song': 'torero'
        }
        

        with open('register_data.text','w') as register_file:
            json.dump(data, register_file)
        """
        pygame.display.set_caption("Registro")
        registerMousePosition = pygame.mouse.get_pos()

        Screen.fill("white")

        registerText = GetFont(45).render("This is the REGISTER screen.", True, "Black")
        registerRectangle = registerText.get_rect(center=(720, 260))
        Screen.blit(registerText, registerRectangle)

        registerBack = Button(image=None, pos=(50,20),
                               textInput="BACK", font=GetFont(20), baseColor="Black", hoveringColor="Green")

        registerBack.ChangeColor(registerMousePosition)
        registerBack.UpdateScreen(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if registerBack.CheckForInput(registerMousePosition):
                    MainScreen()

        pygame.display.update()

def LeaderboardScreen():
    while True:
        pygame.display.set_caption("Salón de la Fama")
        leaderboardMousePosition = pygame.mouse.get_pos()

        Screen.fill("white")

        leadearboardText = GetFont(45).render("This is the LEADERBOARD screen.", True, "Black")
        leadearboardRectangle = leadearboardText.get_rect(center=(720, 260))
        Screen.blit(leadearboardText, leadearboardRectangle)

        leadearboardBack = Button(image=None, pos=(720, 460),
                                  textInput="BACK", font=GetFont(75), baseColor="Black", hoveringColor="Green")

        leadearboardBack.ChangeColor(leaderboardMousePosition)
        leadearboardBack.UpdateScreen(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if leadearboardBack.CheckForInput(leaderboardMousePosition):
                    MainScreen()

        pygame.display.update()

def HelpScreen():
    while True:
        pygame.display.set_caption("Ayuda")
        helpMousePosition = pygame.mouse.get_pos()

        Screen.fill("black")

        helpText = GetFont(45).render("This is the HELP screen.", True, "White")
        helpRectangle = helpText.get_rect(center=(720, 260))
        Screen.blit(helpText, helpRectangle)

        helpBack = Button(image=None, pos=(720, 460),
                           textInput="BACK", font=GetFont(75), baseColor="White", hoveringColor="Green")

        helpBack.ChangeColor(helpMousePosition)
        helpBack.UpdateScreen(Screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if helpBack.CheckForInput(helpMousePosition):
                    MainScreen()

        pygame.display.update()

def MainScreen():
    while True:
        Screen.blit(Background, (0, 0))

        menuMousePosition = pygame.mouse.get_pos()

        menuText = GetFont(50).render("EAGLE DEFENDER", True, "#b68f40")
        menuRectangle = menuText.get_rect(center=(720, 100))

        playButton = Button(image=pygame.image.load("assets/MediumRectangle.png"), pos=(720, 215),
                            textInput="START", font=GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
        registerButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 340),
                                textInput="¡REGISTER!", font=GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
        leaderboardButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 465),
                                   textInput="LEADERBOARD", font=GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
        helpButton = Button(image=pygame.image.load("assets/MediumRectangle.png"), pos=(720, 590),
                            textInput="HELP", font=GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
        quitButton = Button(image=pygame.image.load("assets/QuitRectangle.png"), pos=(720, 715),
                            textInput="QUIT", font=GetFont(50), baseColor="#d7fcd4", hoveringColor="Purple")
        # Set the button for each Screen

        Screen.blit(menuText, menuRectangle)

        for button in [playButton, registerButton, leaderboardButton, quitButton, helpButton]:
            button.ChangeColor(menuMousePosition)
            button.UpdateScreen(Screen)
        # Changes the color when the mouse is on top of the text

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.CheckForInput(menuMousePosition):
                    StartScreen()
                if registerButton.CheckForInput(menuMousePosition):
                    RegisterScreen()
                if leaderboardButton.CheckForInput(menuMousePosition):
                    LeaderboardScreen()
                if helpButton.CheckForInput(menuMousePosition):
                    HelpScreen()
                if quitButton.CheckForInput(menuMousePosition):
                    pygame.quit()
                    sys.exit()
                # When the text is clicked it goes to the specific page
        pygame.display.update()


MainScreen()
