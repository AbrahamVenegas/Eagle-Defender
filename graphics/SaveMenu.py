import pygame
import sys

class SaveMenu:

    def __init__(self, screen, width, height, font, titleFont):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = font
        self.title = titleFont
        self.pointer = 0

    def showMenu(self, player):
        saving = True
        while saving:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        saving = False

            self.showGames(player)
            pygame.display.update()

    def showGames(self, player):
        self.screen.fill(color=0)
        title = self.title.render('GAME SAVED', True, "White")
        titleRect = title.get_rect(center=(420, 100))
        self.screen.blit(title, titleRect)

        player = self.font.render(f"PLAYER: {player}", True, 'White')
        playerRect = player.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(player, playerRect)

        resume_text = self.font.render("BACK [ESC]", True, "White")
        resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 75))
        self.screen.blit(resume_text, resume_rect)
