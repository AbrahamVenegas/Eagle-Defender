import pygame
import pygame_gui
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
        data = {"username": "abraham",
        "password": "1234",
        "email": "abravenegas@estudiantec.cr",
        "age": 20,
        "photo":b'101010101010",
        "song": b'1010101010
        }
        """

        pygame.display.set_caption("Registro")
        font = GetFont(36)
        clock = pygame.time.Clock()
        saveButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 715),
                            textInput="Register", font=GetFont(50), baseColor="Black",
                            hoveringColor="Green")
        registerBack = Button(image=None, pos=(75, 30),
                              textInput="BACK", font=GetFont(30), baseColor="Black", hoveringColor="Red")

        # Define input box dimensions and positions
        input_box_dimensions = [
            pygame.Rect(570, 100, 570, 50),
            pygame.Rect(570, 200, 300, 50),
            pygame.Rect(570, 300, 300, 50),
            pygame.Rect(570, 400, 300, 50),
            pygame.Rect(570, 500, 300, 50),
            pygame.Rect(570, 600, 300, 50)
        ]

        # Texts for the title of each input box
        input_texts = [
            "Insert your Username:",
            "Insert your Password:",
            "Insert your Email:",
            "Insert your Age:",
            "Insert your Photo:",
            "Insert your Song:"
        ]

        colorInactive = [pygame.Color('lightskyblue3')] * 6
        colorActive = pygame.Color('dodgerblue2')
        colors = colorInactive.copy()
        texts = [''] * 6
        actives = [False] * 6

        def save_to_file(data):
            with open('data.json', 'w') as f:
                json.dump(data, f)

        while True:
            registerMousePosition = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for i, box in enumerate(input_box_dimensions):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if box.collidepoint(event.pos):
                            actives = [False] * 6
                            actives[i] = True
                        else:
                            actives[i] = False
                        colors[i] = colorActive if actives[i] else colorInactive[i]

                if event.type == pygame.KEYDOWN:
                    for i, active in enumerate(actives):
                        if active:
                            if event.key == pygame.K_RETURN:
                                print(f"Text {i + 1}: {texts[i]}")
                                data = {f'text{i + 1}': texts[i] for i in range(6)}
                                save_to_file(data)
                            elif event.key == pygame.K_BACKSPACE:
                                texts[i] = texts[i][:-1]
                            else:
                                texts[i] += event.unicode

                # Check button clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if saveButton.CheckForInput(registerMousePosition):
                        MainScreen()
                        data = {f'text{i + 1}': texts[i] for i in range(6)}
                        save_to_file(data)
                    elif registerBack.CheckForInput(registerMousePosition):
                        MainScreen()
                        texts = [''] * 6

            Screen.fill(("white"))

            for i in range(6):
                registerText = GetFont(25).render(input_texts[i], True, "Black")
                registerRectangle = registerText.get_rect(center=(720, input_box_dimensions[i].y - 30))
                Screen.blit(registerText, registerRectangle)

                txt_surface = font.render(texts[i], True, colors[i])
                width = max(300, txt_surface.get_width() + 10)
                input_box_dimensions[i].w = width
                Screen.blit(txt_surface, (input_box_dimensions[i].x + 5, input_box_dimensions[i].y + 5))
                pygame.draw.rect(Screen, colors[i], input_box_dimensions[i], 2)

            saveButton.ChangeColor(registerMousePosition)
            saveButton.UpdateScreen(Screen)
            registerBack.ChangeColor(registerMousePosition)
            registerBack.UpdateScreen(Screen)
            pygame.display.flip()
            clock.tick(30)


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
                            textInput="QUIT", font=GetFont(50), baseColor="#d7fcd4", hoveringColor="Red")
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
