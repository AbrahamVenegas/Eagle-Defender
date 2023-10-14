import pygame
import random
import os
import sys
import json
from Player import Player
from Tank import Tank


class GameWindow:

    _instance = None
    baseFont = None
    screen = None
    background = None
    player1 = None
    player2 = None
    songRoute = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.width = 800
        self.height = 576
        self.player1 = Player(None, None, None, None, None, None)
        self.player2 = Player(None, None, None, None, None, None)
        self.tank = Tank()

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def FillPlayer1Info(self):
        with open("player1.json", "r") as jsonFile:
            datos = json.load(jsonFile)

        self.player1.username = datos["username"]
        self.player1.password = datos["password"]
        self.player1.email = datos["email"]
        self.player1.age = datos["age"]
        self.player1.photo = datos["photo"]
        self.player1.song = datos["song"]

    def FillPlayer2Info(self):
        with open("player2.json", "r") as jsonFile:
            datos = json.load(jsonFile)

        self.player2.username = datos["username"]
        self.player2.password = datos["password"]
        self.player2.email = datos["email"]
        self.player2.age = datos["age"]
        self.player2.photo = datos["photo"]
        self.player2.song = datos["song"]

    def Start(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.baseFont = pygame.font.Font(None, 25)
        self.background = pygame.image.load("assets/Mapa2 grid.png")
        pygame.display.set_caption("Eagle Defender")
        self.FillPlayer1Info()
        self.FillPlayer2Info()

        playlistRoute = "DefaultPlaylist"
        playlist = os.listdir(playlistRoute)
        randomSong = random.choice(playlist)
        randomSongPath = os.path.join(playlistRoute, randomSong)

        self.songRoute = randomSongPath
        pygame.mixer.music.load(self.songRoute)

        # Reproduce la canción de fondo en bucle (-1 significa bucle infinito)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        fps = 120

        while True:
            clock.tick(fps)
            self.screen.blit(self.background, (0, 0))
            self.tank.draw(self.screen)
            p1Name = self.GetFont(14).render(self.player1.username, True, "White") # Name of the player one
            p1Rectangle = p1Name.get_rect(center=(170, 20))
            self.screen.blit(p1Name, p1Rectangle)

            p2Name = self.GetFont(14).render(self.player2.username, True, "White")  # Name of the player two
            p2NameRectangle = p2Name.get_rect(center=(630, 20))
            self.screen.blit(p2Name, p2NameRectangle)

            p1Photo = pygame.image.load("priv/photos/" + self.player1.photo).convert()
            p1Photo = pygame.transform.scale(p1Photo, (50, 50))
            p1PhotoRectangle = p1Photo.get_rect(center=(50, 20))
            self.screen.blit(p1Photo, p1PhotoRectangle)

            p2Photo = pygame.image.load("priv/photos/" + self.player2.photo).convert()
            p2Photo = pygame.transform.scale(p2Photo, (50, 50))
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
                    if event.key == pygame.K_1:
                        pygame.mixer.music.stop()
                        self.songRoute = self.player1.song
                        pygame.mixer.music.load("priv/songs/" + self.songRoute)
                        pygame.mixer.music.play(-1)

                    if event.key == pygame.K_2:
                        pygame.mixer.music.stop()
                        self.songRoute = self.player2.song
                        pygame.mixer.music.load("priv/songs/" + self.songRoute)
                        pygame.mixer.music.play(-1)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.tank.speed_y -= self.tank.acceleration
                if keys[pygame.K_s]:
                    self.tank.speed_y += self.tank.acceleration
                if keys[pygame.K_a]:
                    self.tank.speed_x -= self.tank.acceleration
                if keys[pygame.K_d]:
                    self.tank.speed_x += self.tank.acceleration
                self.tank.update()

            pygame.display.update()
