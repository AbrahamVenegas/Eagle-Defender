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

    def showMenu(self, player, flag):
        saving = True
        while saving:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        saving = False
                    elif event.key == pygame.K_y:
                        saving = False
                        return True
                    elif event.key == pygame.K_n:
                        saving = False
                        return False

            self.showGames(player, flag)
            pygame.display.update()

    def showGames(self, player, flag):
        padding = 0
        self.screen.fill(color=0)
        title = self.title.render('GAME SAVED', True, "White")
        titleRect = title.get_rect(center=(420, 100))
        self.screen.blit(title, titleRect)

        player = self.font.render(f"PLAYER: {player}", True, 'White')
        playerRect = player.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(player, playerRect)

        if flag:
            padding = 75
            save = self.font.render("WOULD YOU LIKE TO DELETE ", True, "White")
            saveRect = save.get_rect(center=(self.width // 2, self.height // 2 + 37))
            self.screen.blit(save, saveRect)
            save2 = self.font.render("THE OLDEST GAME SAVED?", True, "White")
            saveRect2 = save2.get_rect(center=(self.width // 2, self.height // 2 + 75))
            self.screen.blit(save2, saveRect2)

        resume_text = self.font.render("YES [Y]           NO [N]", True, "White")
        resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 75 + padding))
        self.screen.blit(resume_text, resume_rect)
