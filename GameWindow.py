import pygame
import sys
from Player import Player


class GameWindow:

    baseFont = None
    screen = None
    background = None
    player1 = None
    player2 = None

    def __init__(self):
        self.width = 800
        self.height = 576
        self.player1 = Player(None, None,None,None,None,None)
        self.player2 = Player(None, None, None, None, None, None)

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def FillPlayer1Info(self, username, password, email, age, photo, song):
        self.player1.username = username
        self.player1.password = password
        self.player1.email = email
        self.player1.age = age
        self.player1.photo = photo
        self.player1.song = song

    def Start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.baseFont = pygame.font.Font(None, 25)
        self.background = pygame.image.load("assets/Mapa2 grid.png")
        pygame.display.set_caption("Eagle Defender")


        while True:
            self.screen.blit(self.background, (0, 0))

            p1Name = self.GetFont(14).render(self.player1.username, True, "White") # Name of the player one
            p1Rectangle = p1Name.get_rect(center=(170, 20))
            self.screen.blit(p1Name, p1Rectangle)

            p1Name = self.GetFont(14).render(self.player2.username, True, "White")  # Name of the player two
            p1NameRectangle = p1Name.get_rect(center=(630, 20))
            self.screen.blit(p1Name, p1NameRectangle)

            p1Photo = pygame.image.load("assets/photo.jpeg").convert()
            p1Photo = pygame.transform.scale(p1Photo, (50, 50))
            p1PhotoRectangle = p1Photo.get_rect(center=(50, 20))
            self.screen.blit(p1Photo, p1PhotoRectangle)

            p2Photo = pygame.image.load("assets/photo.jpeg").convert()
            p2Photo = pygame.transform.scale(p1Photo, (50, 50))
            p2PhotoRectangle = p2Photo.get_rect(center=(750, 20))
            self.screen.blit(p2Photo, p2PhotoRectangle)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()