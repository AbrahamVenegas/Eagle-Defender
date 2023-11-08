import pygame
import sys


class PauseWindow:

    def __init__(self, screen, width, height, titleFont, font):
        self.screen = screen
        self.width = width
        self.height = height
        self.titleFont = titleFont
        self.font = font

    def pause_game(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Si se presiona "esc" nuevamente, reanuda el juego y sale de la función de pausa
                        paused = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_s:
                        paused = False
                        ## TODO
            # Lógica para mostrar la ventana de pausa en la pantalla
            self.show_paused_window()
            pygame.display.update()

    def show_paused_window(self):
        self.screen.fill(color=0)
        PausedGame = self.titleFont.render('PAUSED ', True, "White")
        PausedGameRect = PausedGame.get_rect(center=(440, 100))
        self.screen.blit(PausedGame, PausedGameRect)

        quit_text = self.font.render("QUIT GAME [Q]", True, "White")
        quit_rect = quit_text.get_rect(center=(self.width // 2, self.height // 2 + 25))
        self.screen.blit(quit_text, quit_rect)

        resume_text = self.font.render("RESUME GAME [ESC]", True, "White")
        resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 95))
        self.screen.blit(resume_text, resume_rect)

        save_text = self.font.render("SAVE GAME [S]", True, "White")
        save_rect = save_text.get_rect(center=(self.width // 2, self.height // 2 + 165))
        self.screen.blit(save_text, save_rect)
