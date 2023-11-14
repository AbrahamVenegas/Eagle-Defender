import sys

import pygame


class LoadMenu:

    def __init__(self, screen):
        self.screen = screen
        self.width = 800
        self.height = 576

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def showLoadMenu(self):
        self.screen.fill(color=0)
        loading = True
        while loading:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.LoadingInfo()
            pygame.display.update()

    def LoadingInfo(self):
        title = self.GetFont(64).render("LOAD GAME", True, 'White')
        titleRect = title.get_rect(center=(420, 100))
        self.screen.blit(title, titleRect)

        slotImg = pygame.image.load("assets/LoadSlot.png")
        slot1 = pygame.transform.scale(slotImg, (500, 130))
        self.screen.blit(slot1, (50, 250))
