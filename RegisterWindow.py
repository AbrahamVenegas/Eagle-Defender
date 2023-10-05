import pygame
from button import Button
from StartWindow import StartWindow
import json
import sys

class RegisterWindow:
    Screen = None

    def GetFont(self, size):  # To return it in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def RegisterScreen(self):
        pygame.init()  # starts it
        self.Screen = pygame.display.set_mode((1440, 810))  # To set the parameters of the window
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
            font = self.GetFont(36)
            clock = pygame.time.Clock()
            saveButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 715),
                                textInput="Register", font=self.GetFont(50), baseColor="Black",
                                hoveringColor="Green")
            registerBack = Button(image=None, pos=(75, 30),
                                  textInput="BACK", font=self.GetFont(30), baseColor="Black", hoveringColor="Red")

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
                            startWindow = StartWindow._instance
                            startWindow.MainScreen()
                            data = {f'text{i + 1}': texts[i] for i in range(6)}
                            save_to_file(data)
                        elif registerBack.CheckForInput(registerMousePosition):
                            startWindow = StartWindow._instance
                            startWindow.MainScreen()
                            texts = [''] * 6

                self.Screen.fill(("white"))

                for i in range(6):
                    registerText = self.GetFont(25).render(input_texts[i], True, "Black")
                    registerRectangle = registerText.get_rect(center=(720, input_box_dimensions[i].y - 30))
                    self.Screen.blit(registerText, registerRectangle)

                    txt_surface = font.render(texts[i], True, colors[i])
                    width = max(300, txt_surface.get_width() + 10)
                    input_box_dimensions[i].w = width
                    self.Screen.blit(txt_surface, (input_box_dimensions[i].x + 5, input_box_dimensions[i].y + 5))
                    pygame.draw.rect(self.Screen, colors[i], input_box_dimensions[i], 2)

                saveButton.ChangeColor(registerMousePosition)
                saveButton.UpdateScreen(self.Screen)
                registerBack.ChangeColor(registerMousePosition)
                registerBack.UpdateScreen(self.Screen)
                pygame.display.flip()
                clock.tick(30)
