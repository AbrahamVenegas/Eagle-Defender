import sys
import pygame
from classes.Timer import Timer
from classes.button import Button


class SettingsWindow:
    Timer = None
    Background = pygame.image.load("assets/Background.png")
    Screen = None

    def GetFont(self, size):  # To return it in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def showSettings(self):
        running = True
        pygame.init()
        self.Timer = Timer()
        self.Screen = pygame.display.set_mode((800, 576))
        pygame.display.set_caption("Eagle Defender")
        self.Background = pygame.transform.scale(self.Background, (800, 576))

        while running:
            self.Screen.blit(self.Background, (0, 0))
            self.settingsComps()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def settingsComps(self):
        textBox = pygame.image.load("assets/MediumRectangle.png")
        textBox = pygame.transform.scale(textBox, (450, 70))
        self.Screen.blit(textBox, (190, 100))
        text = self.GetFont(30).render(f"TURN TIME: {self.Timer.time}s", True, "White")
        self.Screen.blit(text, (200, 120))

        addImg = pygame.image.load("assets/MediumRectangle.png")
        addImg = pygame.transform.scale(addImg, (100, 80))
        addButton = Button(addImg, (240, 240), "+10",
                           self.GetFont(30), "#d7fcd4", "Purple")
        addButton.ChangeColor(pygame.mouse.get_pos())
        addButton.UpdateScreen(self.Screen)

        lowerButton = Button(addImg, (590, 240), "-10",
                           self.GetFont(30), "#d7fcd4", "Purple")
        lowerButton.ChangeColor(pygame.mouse.get_pos())
        lowerButton.UpdateScreen(self.Screen)

        resetImg = pygame.transform.scale(pygame.image.load("assets/MediumRectangle.png"), (160, 80))
        reset = Button(resetImg, (415, 240), "RESET",
                             self.GetFont(30), "#d7fcd4", "Purple")
        reset.ChangeColor(pygame.mouse.get_pos())
        reset.UpdateScreen(self.Screen)

