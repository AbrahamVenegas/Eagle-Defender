import pygame
import sys
from REST_API.JSONAdapter import JSONAdapter
from REST_API import REST_API
from REST_API.Loader import Loader


class PauseWindow:
    screen = None
    varList = []

    def __init__(self):
        self.width = 800
        self.height = 576
        self.titleFont = None
        self.font = None
        self.adapter = JSONAdapter()
        self.loader = Loader()

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def VerifySave(self, player, email):
        response = REST_API.check_save_limit(str(email))
        if response:
            #REST_API.save_game(email, str(self.adapter.saveData()))
            self.varList = [player, email, False]
            #self.saveMenu.showMenu(player, False)
        else:
            self.varList = [player, email, True]

    def pause_game(self, player, email):  # username
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.titleFont = self.GetFont(64)
        self.font = self.GetFont(24)
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Si se presiona "esc" nuevamente, reanuda el juego y sale de la función de pausa
                        return [], '0', "Game"
                    if event.key == pygame.K_q:
                        return [], "Back", "Start"
                    if event.key == pygame.K_s:
                        self.VerifySave(player, email)
                        return self.varList, "No", "SaveMenu"
                    if event.key == pygame.K_l:
                        self.loader.getJSON(email)

            # Lógica para mostrar la ventana de pausa en la pantalla
            self.show_paused_window(player)
            pygame.display.update()

    def show_paused_window(self, player):
        self.screen.fill(color=0)
        PausedGame = self.titleFont.render('PAUSED ', True, "White")
        PausedGameRect = PausedGame.get_rect(center=(440, 100))
        self.screen.blit(PausedGame, PausedGameRect)

        player = self.font.render(f"PLAYER: {player}", True, 'White')
        playerRect = player.get_rect(center=(self.width // 2, self.height // 2 - 70))
        self.screen.blit(player, playerRect)

        quit_text = self.font.render("QUIT GAME [Q]", True, "White")
        quit_rect = quit_text.get_rect(center=(self.width // 2, self.height // 2 + 25))
        self.screen.blit(quit_text, quit_rect)

        resume_text = self.font.render("RESUME GAME [ESC]", True, "White")
        resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 95))
        self.screen.blit(resume_text, resume_rect)

        save_text = self.font.render("SAVE GAME [S]", True, "White")
        save_rect = save_text.get_rect(center=(self.width // 2, self.height // 2 + 165))
        self.screen.blit(save_text, save_rect)

        load_text = self.font.render("LOAD GAME [L]", True, "White")
        load_rect = load_text.get_rect(center=(self.width // 2, self.height // 2 + 165 + 70))
        self.screen.blit(load_text, load_rect)
