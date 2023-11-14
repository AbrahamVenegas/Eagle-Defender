from classes.DJ import DJ
import pygame
import sys
from classes.button import Button

class FinishWindow:

    def __init__(self, screen, titleFont, font):
        self.screen = screen
        self.titleFont = titleFont
        self.font = font
        self.dj = DJ(None)
        self.button = None

    def FinishGame(self, winner, looser):
        self.dj.NewSong("DefaultPlaylist/FinishSong.mp3")
        while True:
            mousePos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.CheckForInput(mousePos):
                        pygame.quit()
                        sys.exit()
            self.show_finish_window(winner, looser)
            self.button.ChangeColor(mousePos)
            self.button.UpdateScreen(self.screen)
            pygame.display.update()

    def show_finish_window(self, winner, looser):
        self.screen.fill(color=0)
        winnerTitle = self.titleFont.render('WINNER', True, "Green")
        winnerTitleRect = winnerTitle.get_rect(center=(200, 150))
        self.screen.blit(winnerTitle, winnerTitleRect)

        looserTitle = self.titleFont.render('lOOSER', True, "Red")
        looserTitleRect = looserTitle.get_rect(center=(600, 150))
        self.screen.blit(looserTitle, looserTitleRect)

        winner_text = self.font.render("Congratulations:", True, 'White')
        winner_text_Rect = winner_text.get_rect(center=(200, 220))
        self.screen.blit(winner_text, winner_text_Rect)

        winner_name = self.font.render(winner, True, 'White')
        winner_name_Rect = winner_name.get_rect(center=(200, 270))
        self.screen.blit(winner_name, winner_name_Rect)

        winner_text2 = self.font.render("You are the GOAT!", True, 'White')
        winner_text_Rect2 = winner_text2.get_rect(center=(200, 320))
        self.screen.blit(winner_text2, winner_text_Rect2)

        looser_text = self.font.render("Sorry for you:", True, 'White')
        looser_text_Rect = looser_text.get_rect(center=(600, 220))
        self.screen.blit(looser_text, looser_text_Rect)

        looser_name = self.font.render(looser, True, 'White')
        looser_name_Rect = looser_name.get_rect(center=(600, 270))
        self.screen.blit(looser_name, looser_name_Rect)

        looser_text2 = self.font.render("Keep trying!", True, 'White')
        looser_text_Rect2 = looser_text2.get_rect(center=(600, 320))
        self.screen.blit(looser_text2, looser_text_Rect2)

        self.button = Button(image=None, pos=(400, 460),
               textInput="EXIT", font=pygame.font.Font("assets/font.ttf", 30),
               baseColor="White", hoveringColor="Purple")
