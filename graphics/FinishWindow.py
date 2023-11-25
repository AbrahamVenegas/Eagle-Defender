from classes.DJ import DJ
import pygame
import sys
from REST_API import REST_API
from classes.button import Button

class FinishWindow:
    screen = None
    titleFont = font = None

    def __init__(self):
        self.dj = DJ()
        self.button = None
        self.width = 800
        self.height = 576

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def FinishGame(self, winner, looser, time):
        pygame.init()
        response = REST_API.insert_leaderboard(winner, time)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.dj.NewSong("DefaultPlaylist/FinishSong.mp3")
        while True:
            mousePos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.CheckForInput(mousePos):
                        self.dj.Stop()
                        pygame.quit()
                        return ["Start"]
            self.show_finish_window(winner, looser)
            self.LeaderboardMsg(response)
            self.button.ChangeColor(mousePos)
            self.button.UpdateScreen(self.screen)
            pygame.display.update()

    def LeaderboardMsg(self, Flag):
        if Flag:
            text = self.font.render("New record! :D", True, "White")
            self.screen.blit(text, (280, 360))
        else:
            text = self.font.render("Try your best next time :(", True, "White")
            self.screen.blit(text, (200, 360))

    def show_finish_window(self, winner, looser):
        self.screen.fill(color=0)
        self.titleFont = self.GetFont(50)
        self.font = self.GetFont(16)
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
