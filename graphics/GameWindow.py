import pygame
import random
import os
import sys
import json
from classes.Player import Player
from classes.Tank import Tank
from classes.Turn import Turn
from classes.Tank import bullet_sprites
from classes.BulletFactory import BulletFactory
from classes.BlockFactory import BlockFactory
from classes.Eagle import Eagle


class GameWindow:
    _instance = None
    baseFont = None
    screen = None
    background = None
    player1 = None
    player2 = None
    songRoute = None
    gameTurn = None
    index = 0
    timeElapsed = 0
    selectionX = 380
    selectionY = 2
    bulletFactory = BulletFactory()
    bullet = None
    bulletSelected = "Fire"
    fire = "ready"
    selectionCount = 1
    block = None
    BlockFactory = BlockFactory()
    setBlock = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.width = 800
        self.height = 576
        self.player1 = Player(None, None, None, None, None, None, None)
        self.player2 = Player(None, None, None, None, None, None, None)
        self.gameTurn = Turn(None, None)
        self.tank = Tank()
        self.fireAmmo = 5
        self.waterAmmo = 5
        self.bombAmmo = 5
        self.fireText = self.waterText = self.bombText = None
        self.selectSprites = None
        self.Eagle = Eagle()

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
        self.player1.song = "priv/songs/" + datos["song"]

    def FillPlayer2Info(self):
        with open("json/player2.json", "r") as jsonFile:
            datos = json.load(jsonFile)

        self.player2.username = datos["username"]
        self.player2.password = datos["password"]
        self.player2.email = datos["email"]
        self.player2.age = datos["age"]
        self.player2.photo = datos["photo"]
        self.player2.song = "priv/songs/" + datos["song"]

    def AmmoImg(self):
        fireAmmoImg = bullet_sprites[0]
        waterAmmoImg = bullet_sprites[1]
        bombAmmoImg = bullet_sprites[2]
        fireAmmoImg = pygame.transform.rotate(fireAmmoImg, 270)
        waterAmmoImg = pygame.transform.rotate(waterAmmoImg, 270)
        bombAmmoImg = pygame.transform.rotate(bombAmmoImg, 270)

        fireRect = fireAmmoImg.get_rect(center=(400, 20))
        self.screen.blit(fireAmmoImg, fireRect)
        waterRect = waterAmmoImg.get_rect(center=(480, 20))
        self.screen.blit(waterAmmoImg, waterRect)
        bombRect = bombAmmoImg.get_rect(center=(320, 20))
        self.screen.blit(bombAmmoImg, bombRect)


    def AmmoCounters(self):
        fontSize = 16
        self.fireText = self.GetFont(fontSize).render(":" + str(self.fireAmmo), True, "White")
        self.waterText = self.GetFont(fontSize).render(":" + str(self.waterAmmo), True, "White")
        self.bombText = self.GetFont(fontSize).render(":" + str(self.bombAmmo), True, "White")

        fireRect = self.fireText.get_rect(center=(430, 20))
        waterRect = self.fireText.get_rect(center=(510, 20))
        bombRect = self.fireText.get_rect(center=(350, 20))
        self.screen.blit(self.fireText, fireRect)
        self.screen.blit(self.waterText, waterRect)
        self.screen.blit(self.bombText, bombRect)

    def loadSelectionAnimation(self):
        self.selectSprites = [
            pygame.image.load("assets/Select_01.png"),
            pygame.image.load("assets/Select_02.png"),
            pygame.image.load("assets/Select_03.png"),
            pygame.image.load("assets/Select_04.png"),
            pygame.image.load("assets/Select_05.png"),
            pygame.image.load("assets/Select_06.png"),
            pygame.image.load("assets/Select_07.png"),
            pygame.image.load("assets/Select_08.png"),
        ]

    def SelectionAnimation(self):
        clock = pygame.time.Clock()
        selectionImg = self.selectSprites[self.index]
        selectionRect = selectionImg.get_rect()
        selectionRect.x = self.selectionX
        selectionRect.y = self.selectionY
        self.screen.blit(selectionImg, selectionRect)
        deltaTime = clock.tick(60) / 1000.0
        self.timeElapsed += deltaTime

        if self.timeElapsed >= 1 / 15.0:
            self.timeElapsed -= 1 / 15.0
            self.index = (self.index + 1) % len(self.selectSprites)

    def SelectBullet(self):
        if self.selectionCount == 1:
            self.selectionX = 380
            self.bulletSelected = "Fire"

        elif self.selectionCount == 2:
            self.selectionX = 380 + 80
            self.bulletSelected = "Water"

        elif self.selectionCount == 3:
            self.selectionX = 380 - 80
            self.bulletSelected = "Bomb"

    def OutOfAmmo(self):
        if self.selectionCount == 1:
            return self.fireAmmo == 0
        elif self.selectionCount == 2:
            return self.waterAmmo == 0
        elif self.selectionCount == 3:
            return self.bombAmmo == 0

    def UpdateAmmo(self):
        if self.bulletSelected == "Fire":
            self.fireAmmo -= 1
        elif self.bulletSelected == "Water":
            self.waterAmmo -= 1
        elif self.bulletSelected == "Bomb":
            self.bombAmmo -= 1

    def Start(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.baseFont = pygame.font.Font(None, 25)
        self.background = pygame.image.load("assets/Mapa2 grid.png")
        pygame.display.set_caption("Eagle Defender")
        self.FillPlayer1Info()
        self.FillPlayer2Info()
        
        self.loadSelectionAnimation()
        ''' 
        playlistRoute = "DefaultPlaylist"
        playlist = os.listdir(playlistRoute)
        randomSong = random.choice(playlist)
        randomSongPath = os.path.join(playlistRoute, randomSong)
        '''
        self.songRoute = self.player1.song
        pygame.mixer.music.load(self.songRoute)

        # Reproduce la canción de fondo en bucle (-1 significa bucle infinito)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        fps = 120

        # Always play first the defensor (player 1)
        self.gameTurn.player = "Defensor"
        # print(self.gameTurn.player)
        self.gameTurn.time = int(pygame.mixer.Sound(self.player1.song).get_length())
        # print(self.gameTurn.time)
        time_elapsed = 0
        # print(seconds)

        while True:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Eagle.sprite, self.Eagle.rect)
            self.tank.draw(self.screen)
            p1Name = self.GetFont(14).render(self.player1.username, True, "White")  # Name of the player one
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

            turnText = self.GetFont(14).render("Turno:", True, "White")
            turnTextRectangle = turnText.get_rect(center=(70, 556))
            self.screen.blit(turnText, turnTextRectangle)

            playerTurnText = self.GetFont(14).render(self.gameTurn.player, True, "White")
            playerTurnTextRectangle = playerTurnText.get_rect(center=(170, 556))
            self.screen.blit(playerTurnText, playerTurnTextRectangle)

            actual_time = pygame.time.get_ticks() // 1000
            past_time = actual_time - time_elapsed

            if past_time >= 1 and self.gameTurn.time >= 1:
                self.gameTurn.time -= 1
                time_elapsed = actual_time

            TurnTimeText = self.GetFont(14).render('Tiempo: ', True, "White")
            TurnTimeTextRectangle = TurnTimeText.get_rect(center=(690, 556))
            self.screen.blit(TurnTimeText, TurnTimeTextRectangle)

            TurnTime = self.GetFont(14).render(str(self.gameTurn.time), True, "White")
            TurnTimeRectangle = TurnTime.get_rect(center=(750, 556))
            self.screen.blit(TurnTime, TurnTimeRectangle)

            if self.gameTurn.CheckTurn(self.gameTurn.time):
                self.gameTurn.player, self.gameTurn.time = self.gameTurn.ChangeTurn(self.gameTurn.player, self.player1.song, self.player2.song)
                if self.gameTurn.player == "Defensor":
                    pygame.mixer.music.stop()
                    self.songRoute = self.player1.song
                    pygame.mixer.music.load(self.songRoute)
                    pygame.mixer.music.play(-1)
                if self.gameTurn.player == "Atacante":
                    pygame.mixer.music.stop()
                    self.songRoute = self.player2.song
                    pygame.mixer.music.load(self.songRoute)
                    pygame.mixer.music.play(-1)
            self.AmmoCounters()
            self.AmmoImg()
            self.SelectionAnimation()

            if self.tank.rect.left < 50:
                self.tank.rect.left = 50
                self.tank.update()
            if self.tank.rect.right > self.width:
                self.tank.rect.right = self.width
                self.tank.update()
            if self.tank.rect.top < 100:
                self.tank.rect.top = 100
                self.tank.update()
            if self.tank.rect.bottom > self.height-100:
                self.tank.rect.bottom = self.height-100
                self.tank.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_1:
                        pygame.mixer.music.stop()
                        self.songRoute = self.player1.song
                        pygame.mixer.music.load("priv/songs/" + self.songRoute)
                        pygame.mixer.music.play(-1)

                    elif event.key == pygame.K_2:
                        pygame.mixer.music.stop()
                        self.songRoute = self.player2.song
                        pygame.mixer.music.load("priv/songs/" + self.songRoute)
                        pygame.mixer.music.play(-1)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        self.block = self.BlockFactory.CreateBlock("Concrete", x, y, self.screen)
                        self.block.SetPosition(x, y)
                        self.setBlock = "set"

                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.tank.speed_y -= self.tank.acceleration
                    self.tank.direction = "up"
                if keys[pygame.K_s]:
                    self.tank.speed_y += self.tank.acceleration
                    self.tank.direction = "down"
                if keys[pygame.K_a]:
                    self.tank.speed_x -= self.tank.acceleration
                    if keys[pygame.K_w]:
                        self.tank.direction = "up_left"
                    elif keys[pygame.K_s]:
                        self.tank.direction = "down_left"
                    else:
                        self.tank.direction = "left"

                if keys[pygame.K_d]:
                    self.tank.speed_x += self.tank.acceleration
                    if keys[pygame.K_w]:
                        self.tank.direction = "up_right"
                    elif keys[pygame.K_s]:
                        self.tank.direction = "down_right"
                    else:
                        self.tank.direction = "right"

                if keys[pygame.K_z] and self.fire == "ready":
                    self.selectionCount += 1
                    if self.selectionCount > 3:
                        self.selectionCount = 1
                    self.SelectBullet()

                if keys[pygame.K_SPACE]:
                    if self.fire == "ready" and not self.OutOfAmmo():
                        self.bullet = self.bulletFactory.CreateBullet(
                            self.bulletSelected, self.tank.rect.x, self.tank.rect.y, self.tank.direction, self.screen)
                        self.fire = "fire"

                self.tank.update()

            if self.fire == "fire":
                self.bullet.DrawBullet()
                if not self.bullet.Trajectory() or self.bullet.is_Collision(self.Eagle.rect):
                    self.UpdateAmmo()
                    self.fire = "ready"
            if self.setBlock == "set":
                self.block.DrawBlock()

            pygame.display.update()
            clock.tick(fps)
