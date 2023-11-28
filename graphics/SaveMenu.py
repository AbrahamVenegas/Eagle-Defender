import pygame
import sys
from REST_API.JSONAdapter import JSONAdapter
from REST_API import REST_API

class SaveMenu:
    screen = None

    def __init__(self):
        self.width = 800
        self.height = 576
        self.font = None
        self.title = None
        self.pointer = 0
        self.adapter = JSONAdapter()

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def showMenu(self, player, email, flag):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.title = self.GetFont(64)
        self.font = self.GetFont(24)
        saving = True
        while saving:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        REST_API.save_game(email, str(self.adapter.saveData()))
                        saving = False
                        return ["Pause", player, email]
                    elif event.key == pygame.K_y:
                        flag = False
                    elif event.key == pygame.K_n:
                        saving = False
                        return ["Pause", player, email]

            self.showGames(player, flag)
            pygame.display.update()

    def showGames(self, player, flag):
        padding = 0
        self.screen.fill(color=0)

        player = self.font.render(f"PLAYER: {player}", True, 'White')
        playerRect = player.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(player, playerRect)
        titles = ["GAME SAVED", "WARNING"]

        if flag:
            padding = 75
            text = self.title.render(titles[1], True, 'Red')
            save = self.font.render("WOULD YOU LIKE TO DELETE ", True, "White")
            saveRect = save.get_rect(center=(self.width // 2, self.height // 2 + 37))
            self.screen.blit(save, saveRect)
            save2 = self.font.render("THE OLDEST GAME SAVED?", True, "White")
            saveRect2 = save2.get_rect(center=(self.width // 2, self.height // 2 + 75))
            self.screen.blit(save2, saveRect2)

            resume_text = self.font.render("YES [Y]           NO [N]", True, "White")
            resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 75 + padding))
            self.screen.blit(resume_text, resume_rect)
        else:
            text = self.title.render(titles[0], True, "White")

            resume_text = self.font.render("BACK [ESC]", True, "White")
            resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 75 + padding))
            self.screen.blit(resume_text, resume_rect)

        titleRect = text.get_rect(center=(420, 100))
        self.screen.blit(text, titleRect)
