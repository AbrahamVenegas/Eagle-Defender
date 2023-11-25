import sys
import pygame
from classes.Timer import Timer
from classes.button import Button


class SettingsWindow:
    Timer = None
    Background = pygame.image.load("assets/Background.png")
    Screen = None
    addButton = lowerButton = None
    reset = back = None
    defenderButton = attackerButton = None
    Time = 0

    def GetFont(self, size):  # To return it in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def showSettings(self):
        running = True
        pygame.init()
        self.Timer = Timer()
        self.Screen = pygame.display.set_mode((800, 576))
        pygame.display.set_caption("Eagle Defender")
        self.Background = pygame.transform.scale(self.Background, (800, 576))
        selectImg = pygame.image.load("assets/MediumRectangle.png")
        selectImg = pygame.transform.scale(selectImg, (60, 60))
        self.defenderButton = Button(selectImg, (300, 370), "X", self.GetFont(30), "White", "Purple")
        self.attackerButton = Button(selectImg, (300, 480), "X", self.GetFont(30), "White", "Purple")

        while running:
            mousePos = pygame.mouse.get_pos()
            self.Screen.blit(self.Background, (0, 0))
            self.settingsComps()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.defenderButton.CheckForInput(mousePos) and self.defenderButton.base_color != "Purple":
                        self.defenderButton.base_color = "Purple"
                        self.attackerButton.base_color = "White"
                        self.Time = self.Timer.defender

                    elif self.attackerButton.CheckForInput(mousePos) and self.attackerButton.base_color != "Purple":
                        self.attackerButton.base_color = "Purple"
                        self.defenderButton.base_color = "White"
                        self.Time = self.Timer.attacker

                    elif self.addButton.CheckForInput(mousePos):
                        if self.defenderButton.base_color == "Purple":
                            self.Timer.setDefenderTime(10)
                            self.Time = self.Timer.defender
                        elif self.attackerButton.base_color == "Purple":
                            self.Timer.setAttackerTime(10)
                            self.Time = self.Timer.attacker

                    elif self.lowerButton.CheckForInput(mousePos):
                        if self.defenderButton.base_color == "Purple":
                            self.Timer.setDefenderTime(-10)
                            self.Time = self.Timer.defender
                        elif self.attackerButton.base_color == "Purple":
                            self.Timer.setAttackerTime(-10)
                            self.Time = self.Timer.attacker

                    elif self.reset.CheckForInput(mousePos):
                        if self.defenderButton.base_color == "Purple":
                            self.Timer.defender = 0
                            self.Time = self.Timer.defender
                        elif self.attackerButton.base_color == "Purple":
                            self.Timer.attacker = 0
                            self.Time = self.Timer.attacker

                    elif self.back.CheckForInput(mousePos):
                        return ["Start"]

            pygame.display.update()

    def settingsComps(self):
        mousePos = pygame.mouse.get_pos()
        textBox = pygame.image.load("assets/MediumRectangle.png")
        textBox = pygame.transform.scale(textBox, (450, 70))
        self.Screen.blit(textBox, (190, 100))
        text = self.GetFont(30).render(f"TURN TIME: {self.Time}s", True, "White")
        self.Screen.blit(text, (200, 120))

        addImg = pygame.image.load("assets/MediumRectangle.png")
        addImg = pygame.transform.scale(addImg, (100, 80))
        self.addButton = Button(addImg, (240, 240), "+10",
                           self.GetFont(30), "#d7fcd4", "Purple")
        self.addButton.ChangeColor(mousePos)
        self.addButton.UpdateScreen(self.Screen)

        self.lowerButton = Button(addImg, (590, 240), "-10",
                           self.GetFont(30), "#d7fcd4", "Purple")
        self.lowerButton.ChangeColor(mousePos)
        self.lowerButton.UpdateScreen(self.Screen)

        resetImg = pygame.transform.scale(pygame.image.load("assets/MediumRectangle.png"), (160, 80))
        self.reset = Button(resetImg, (415, 240), "RESET",
                             self.GetFont(30), "#d7fcd4", "Purple")
        self.reset.ChangeColor(mousePos)
        self.reset.UpdateScreen(self.Screen)

        self.back = Button(None, (60, 30), "BACK", self.GetFont(24), "White", "Purple")
        self.back.ChangeColor(mousePos)
        self.back.UpdateScreen(self.Screen)

        self.defenderButton.ChangeColor(mousePos)
        self.defenderButton.UpdateScreen(self.Screen)
        defenderText = self.GetFont(28).render("DEFENDER", True, "#d7fcd4")
        self.Screen.blit(defenderText, (350, 360))

        self.attackerButton.ChangeColor(mousePos)
        self.attackerButton.UpdateScreen(self.Screen)
        attackerText = self.GetFont(28).render("ATTACKER", True, "#d7fcd4")
        self.Screen.blit(attackerText, (350, 470))
