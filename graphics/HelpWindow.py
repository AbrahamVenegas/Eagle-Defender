import pygame
from classes.button import Button
import sys


class HelpWindow:
    _instance = None
    Screen = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def GetFont(self, size):  # To return it in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def HelpScreen(self):
        pygame.init()  # starts it
        self.Screen = pygame.display.set_mode((1440, 810))  # To set the parameters of the window
        pygame.display.set_caption("Eagle Defender")  # Window Title

        while True:
            pygame.display.set_caption("Ayuda")
            helpMousePosition = pygame.mouse.get_pos()

            self.Screen.fill("black")

            helpText = self.GetFont(45).render("Sección de Ayuda", True, "White")
            helpRectangle = helpText.get_rect(center=(720, 100))
            self.Screen.blit(helpText, helpRectangle)

            howToplay = Button(image=None, pos=(720, 350), textInput="¿Cómo se juega?", font=self.GetFont(35),
                               baseColor="White",
                               hoveringColor="Green")
            howToplay.ChangeColor(helpMousePosition)
            howToplay.UpdateScreen(self.Screen)

            howToWin = Button(image=None, pos=(720, 450), textInput="¿Cómo se gana?", font=self.GetFont(35),
                              baseColor="White",
                              hoveringColor="Green")
            howToWin.ChangeColor(helpMousePosition)
            howToWin.UpdateScreen(self.Screen)

            helpBack = Button(image=None, pos=(720, 710), textInput="BACK", font=self.GetFont(75), baseColor="White",
                              hoveringColor="Green")
            helpBack.ChangeColor(helpMousePosition)
            helpBack.UpdateScreen(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if howToplay.CheckForInput(helpMousePosition):
                        self.HelpHTP()
                    if howToWin.CheckForInput(helpMousePosition):
                        self.HelpHTW()
                    if helpBack.CheckForInput(helpMousePosition):
                        return ["Start"]

            pygame.display.update()

    def HelpHTP(self):
        while True:
            pygame.display.set_caption("Ayuda")
            helpHTPMousePosition = pygame.mouse.get_pos()

            self.Screen.fill("black")

            helpHTPText = self.GetFont(45).render("¿Cómo se juega?", True, "White")
            helpHTPRectangle = helpHTPText.get_rect(center=(720, 50))
            self.Screen.blit(helpHTPText, helpHTPRectangle)

            attackerText = self.GetFont(20).render("Jugador Atacante", True, "Purple")
            attackerRectangle = attackerText.get_rect(center=(200, 100))
            self.Screen.blit(attackerText, attackerRectangle)

            defensorText = self.GetFont(20).render("Jugador Defensor", True, "Purple")
            defensorRectangle = defensorText.get_rect(center=(1240, 100))
            self.Screen.blit(defensorText, defensorRectangle)

            helpHTPBack = Button(image=None, pos=(720, 710), textInput="BACK", font=self.GetFont(75), baseColor="White",
                                 hoveringColor="Green")
            helpHTPBack.ChangeColor(helpHTPMousePosition)
            helpHTPBack.UpdateScreen(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if helpHTPBack.CheckForInput(helpHTPMousePosition):
                        self.HelpScreen()
                        break

            pygame.display.update()

    def HelpHTW(self):
        while True:
            pygame.display.set_caption("Ayuda")
            helpHTPMousePosition = pygame.mouse.get_pos()

            self.Screen.fill("black")

            helpHTWText = self.GetFont(45).render("¿Cómo se gana?", True, "White")
            helpHTWRectangle = helpHTWText.get_rect(center=(720, 50))
            self.Screen.blit(helpHTWText, helpHTWRectangle)

            attackerTitle = self.GetFont(20).render("Jugador Atacante", True, "Purple")
            attackerTitleRectangle = attackerTitle.get_rect(center=(200, 100))
            self.Screen.blit(attackerTitle, attackerTitleRectangle)

            textOne = ("Intenta destruir el águila sobre el mapa.\n"
                       "Para esto dispones de un tanque, el cual\n"
                       "puedes moverlo por todo el mapa, y tienes 3\n"
                       "tipos de arma:\n"
                       "1. Bomba\n"
                       "2. Bola de agua\n"
                       "3. Bola de fuego\n"
                       "Toma en cuenta que un bloque de concreto,\n"
                       "se destruye con 1 bomba, 2 bolas de fuego,\n"
                       "o 3 de agua. Un bloque de acero se destruye\n"
                       "con 1 bomba, 1 bola de fuego, o 2 de agua.\n"
                       "y un bloque de Madera, con cualquier ataque.\n"
                       "Además, el alcance máximo de los ataques del\n"
                       "tanque es de 8 bloques. Inicialmente tienes\n"
                       "5 cargas de cada tipo de ataque, y se recargan\n"
                       "cada 30 segundos. Ganarás si destruyes el\n"
                       "águila.")

            textLinesOne = []
            linesOne = textOne.split('\n')
            for line in linesOne:
                ActualLine = self.GetFont(15).render(line, True, "White")
                textLinesOne.append(ActualLine)

            y = 200
            for ActualLine in textLinesOne:
                self.Screen.blit(ActualLine, (45, y))
                y += ActualLine.get_height() + 10

            defensorTitle = self.GetFont(20).render("Jugador Defensor", True, "Purple")
            defensorTitleRectangle = defensorTitle.get_rect(center=(1240, 100))
            self.Screen.blit(defensorTitle, defensorTitleRectangle)

            textTwo = ("        Intenta construir sobre el mapa.\n"
                       "Para esto dispones de 3 tipos  de bloque\n"
                       "                         los cuales son:\n"
                       "                                1. Acero\n"
                       "                             2. Concreto\n"
                       "                               3. madera\n"
                       "Toma en cuenta que un bloque de concreto\n"
                       "     se destruye con 1 bomba, 2 bolas de\n"
                       "fuego o 3 de agua, un bloque de acero se\n"
                       "  destruye con 1 bomba, 1 bola de fuego,\n"
                       " o 2 de agua, y un bloque de Madera, con\n"
                       "                       cualquier ataque.\n"
                       )

            textLinesTwo = []
            linesTwo = textTwo.split('\n')
            for line in linesTwo:
                ActualLine = self.GetFont(15).render(line, True, "White")
                textLinesTwo.append(ActualLine)

            y = 200
            for ActualLine in textLinesTwo:
                self.Screen.blit(ActualLine, (800, y))
                y += ActualLine.get_height() + 10

            helpHTPBack = Button(image=None, pos=(720, 710), textInput="BACK", font=self.GetFont(75), baseColor="White",
                                 hoveringColor="Green")
            helpHTPBack.ChangeColor(helpHTPMousePosition)
            helpHTPBack.UpdateScreen(self.Screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if helpHTPBack.CheckForInput(helpHTPMousePosition):
                        self.HelpScreen()
                        break

            pygame.display.update()
