import sys
import pygame
from REST_API.Loader import Loader


class LoadMenu:

    def __init__(self, screen):
        self.screen = screen
        self.width = 800
        self.height = 576
        self.rect1 = self.rect2 = self.rect3 = None
        self.loader = Loader()

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if self.rect1.collidepoint(mouseX, mouseY):
                        self.loader.slot = 1
                        loading = False
                        return "Load"
                    elif self.rect2.collidepoint(mouseX, mouseY):
                        self.loader.slot = 2
                        loading = False
                        return "Load"
                    elif self.rect3.collidepoint(mouseX, mouseY):
                        self.loader.slot = 3
                        loading = False
                        return "Load"
                if event.type == pygame.K_ESCAPE:
                    loading = False
            self.LoadingInfo()
            pygame.display.update()

    def LoadingInfo(self):
        title = self.GetFont(64).render("LOAD GAME", True, 'White')
        titleRect = title.get_rect(center=(420, 100))
        self.screen.blit(title, titleRect)

        slotImg = pygame.image.load("assets/LoadSlot.png")
        slot1 = pygame.transform.scale(slotImg, (500, 120))
        self.rect1 = slot1.get_rect(center=(400, 170+60))
        self.rect2 = slot1.get_rect(center=(400, 170+120+60))
        self.rect3 = slot1.get_rect(center=(400, 170+120*2+60))
        self.screen.blit(slot1, self.rect1)
        self.screen.blit(slot1, self.rect2)
        self.screen.blit(slot1, self.rect3)

        yPadding = 0
        for date in self.loader.date:
            date1 = self.GetFont(18).render(date, True, 'White')
            email = self.GetFont(18).render(self.loader.email, True, 'White')
            self.screen.blit(date1, (250, 200+yPadding))
            self.screen.blit(email, (250, 235+yPadding))
            yPadding += 120

