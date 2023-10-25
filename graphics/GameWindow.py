import pygame
import random
import os
import sys
import json
import time
from classes.Player import Player
from classes.Tank import Tank
from classes.Block import Block

class GameWindow:

    _instance = None
    baseFont = None
    screen = None
    background = None
    player1 = None
    player2 = None
    songRoute = None
    block_images = [
        pygame.image.load("assets/Wood.png"),
        pygame.image.load("assets/Concrete.png"),
        pygame.image.load("assets/Iron.png"),
    ]
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
        self.block = Block()
        self.index = 0
        self.image = self.block_images[self.index]
        self.blocks = []
        self.block_counts = [0, 0, 0]
        self.block_limits = [10, 10, 10]
        self.active_block = None
        self.reset_time = 10
        self.last_reset = time.time()
        self.current_time = time.time()

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def FillPlayer1Info(self):
        with open("json/player1.json", "r") as jsonFile:
            datos = json.load(jsonFile)

        self.player1.username = datos["username"]
        self.player1.password = datos["password"]
        self.player1.email = datos["email"]
        self.player1.age = datos["age"]
        self.player1.photo = datos["photo"]
        self.player1.song = datos["song"]

    def FillPlayer2Info(self):
        with open("json/player2.json", "r") as jsonFile:
            datos = json.load(jsonFile)

        self.player2.username = datos["username"]
        self.player2.password = datos["password"]
        self.player2.email = datos["email"]
        self.player2.age = datos["age"]
        self.player2.photo = datos["photo"]
        self.player2.song = datos["song"]

    def reset_block_counts(self):
        for i in range(len(self.block_counts)):
            self.block_counts[i] = 0

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
        current_time = time.time()
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Botón izquierdo del ratón
                        if self.active_block is not None:
                            x, y = event.pos
                            # self.block.set_active_block("assets/Wood.png")
                            block_type = self.block_images.index(self.active_block)
                            if self.block_counts[block_type] < self.block_limits[block_type]:
                                # Crear un bloque como un diccionario que almacena la imagen y la posición
                                block = {"image": self.active_block, "rect": self.active_block.get_rect(center=(x, y))}
                                self.blocks.append(block)
                                self.block_counts[block_type] += 1
                                print("Bloque agregado")
                    elif event.button == 3:  # Botón derecho del ratón
                        x, y = event.pos
                        for block in self.blocks:
                            if block["rect"].collidepoint(x, y):
                                block_type = self.block_images.index(block["image"])
                                self.block_counts[block_type] -= 1
                                self.blocks.remove(block)
                                print("Bloque eliminado")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, image in enumerate(self.block_images):
                        x, y = event.pos
                        if pygame.Rect(50 + i * 100, 540, image.get_width(), image.get_height()).collidepoint(event.pos):
                            self.active_block = self.block_images[i]

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


            if  self.current_time - self.last_reset >= self.reset_time:
                self.block.reset_block_counts()
                self.last_reset =  self.current_time
                print(time.time())

            for block in self.blocks:
                self.screen.blit(block["image"], block["rect"])

            # Dibujar los botones con imágenes y la cantidad restante
            for i, image in enumerate(self.block_images):
                self.screen.blit(image, (50 + i * 100, 540))
                text = f": {self.block_limits[i] - self.block_counts[i]}"
                text_render = self.baseFont.render(text, True, (0, 0, 0))
                text_x = 75 + i * 100
                text_y = 523 + image.get_height()
                self.screen.blit(text_render, (text_x, text_y))

            self.block.update()
            self.block.draw(self.screen)
            pygame.display.flip()
            pygame.display.update()
