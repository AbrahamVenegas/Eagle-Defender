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
from classes.button import Button


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
    blockSelected = "Wood"
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
        self.GbuttonImage = pygame.transform.scale(pygame.image.load("assets/Buttons/GreenButton.png"), (110, 50))
        self.readyButton = None
        self.tank = Tank()
        self.fireAmmo = 5
        self.waterAmmo = 5
        self.bombAmmo = 5
        self.ironAmmo = 10
        self.concreteAmmo = 10
        self.woodAmmo = 10
        self.ironBlocks = []
        self.concreteBlocks = []
        self.woodBlocks = []
        self.coordinates = []
        self.text1 = self.text2 = self.text3 = None
        self.selectSprites = None
        self.Eagle = Eagle()
        self.reloadFlag = 0
        self.aim = "ready"
        self.keyState = {}

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
        image1 = None
        image2 = None
        image3 = None

        if self.gameTurn.player == "Atacante":
            image1 = bullet_sprites[0]
            image2 = bullet_sprites[1]
            image3 = bullet_sprites[2]
            image1 = pygame.transform.rotate(image1, 270)
            image2 = pygame.transform.rotate(image2, 270)
            image3 = pygame.transform.rotate(image3, 270)

        elif self.gameTurn.player == "Defensor":
            image1 = pygame.image.load("assets/Blocks/Wood1.png")
            image2 = pygame.image.load("assets/Blocks/Concrete1.png")
            image3 = pygame.image.load("assets/Blocks/Iron1.png")

        rect1 = image1.get_rect(center=(400, 20))
        rect2 = image2.get_rect(center=(480, 20))
        rect3 = image3.get_rect(center=(320, 20))
        self.screen.blit(image1, rect1)
        self.screen.blit(image2, rect2)
        self.screen.blit(image3, rect3)

    def AmmoCounters(self):
        fontSize = 16
        if self.gameTurn.player == "Atacante":
            self.text1 = self.GetFont(fontSize).render(":" + str(self.fireAmmo), True, "White")
            self.text2 = self.GetFont(fontSize).render(":" + str(self.waterAmmo), True, "White")
            self.text3 = self.GetFont(fontSize).render(":" + str(self.bombAmmo), True, "White")

        elif self.gameTurn.player == "Defensor":
            self.text1 = self.GetFont(fontSize).render(":" + str(self.woodAmmo), True, "White")
            self.text2 = self.GetFont(fontSize).render(":" + str(self.concreteAmmo), True, "White")
            self.text3 = self.GetFont(fontSize).render(":" + str(self.ironAmmo), True, "White")

        rect1 = self.text1.get_rect(center=(430, 20))
        rect2 = self.text1.get_rect(center=(510, 20))
        rect3 = self.text1.get_rect(center=(350, 20))
        self.screen.blit(self.text1, rect1)
        self.screen.blit(self.text2, rect2)
        self.screen.blit(self.text3, rect3)

    def loadSelectionAnimation(self):
        self.selectSprites = [
            pygame.image.load("assets/SelectionAnimation/Select_01.png"),
            pygame.image.load("assets/SelectionAnimation/Select_02.png"),
            pygame.image.load("assets/SelectionAnimation/Select_03.png"),
            pygame.image.load("assets/SelectionAnimation/Select_04.png"),
            pygame.image.load("assets/SelectionAnimation/Select_05.png"),
            pygame.image.load("assets/SelectionAnimation/Select_06.png"),
            pygame.image.load("assets/SelectionAnimation/Select_07.png"),
            pygame.image.load("assets/SelectionAnimation/Select_08.png"),
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

    def SelectIcon(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and not self.keyState.get(pygame.K_z, False):
            self.keyState[pygame.K_z] = True
            self.selectionCount += 1
            if self.selectionCount > 3:
                self.selectionCount = 1
        if not keys[pygame.K_z]:
            self.keyState[pygame.K_z] = False

        if self.selectionCount == 1:
            if self.gameTurn.player == "Atacante":
                self.selectionX = 380
                self.bulletSelected = "Fire"
            elif self.gameTurn.player == "Defensor":
                self.selectionX = 380
                self.blockSelected = "Wood"
        elif self.selectionCount == 2:
            if self.gameTurn.player == "Atacante":
                self.selectionX = 380 + 80
                self.bulletSelected = "Water"
            elif self.gameTurn.player == "Defensor":
                self.selectionX = 380 + 80
                self.blockSelected = "Concrete"
        elif self.selectionCount == 3:
            if self.gameTurn.player == "Atacante":
                self.selectionX = 380 - 80
                self.bulletSelected = "Bomb"
            elif self.gameTurn.player == "Defensor":
                self.selectionX = 380 - 80
                self.blockSelected = "Iron"

    def OutOfAmmo(self):
        if self.selectionCount == 1:
            if self.gameTurn.player == "Atacante":
                return self.fireAmmo == 0
            if self.gameTurn.player == "Defensor":
                return self.woodAmmo == 0
        elif self.selectionCount == 2:
            if self.gameTurn.player == "Atacante":
                return self.waterAmmo == 0
            if self.gameTurn.player == "Defensor":
                return self.concreteAmmo == 0
        elif self.selectionCount == 3:
            if self.gameTurn.player == "Atacante":
                return self.bombAmmo == 0
            if self.gameTurn.player == "Defensor":
                return self.ironAmmo == 0

    def UpdateAmmo(self):
        if self.gameTurn.player == "Atacante":
            if self.bulletSelected == "Fire":
                self.fireAmmo -= 1
            elif self.bulletSelected == "Water":
                self.waterAmmo -= 1
            elif self.bulletSelected == "Bomb":
                self.bombAmmo -= 1
        elif self.gameTurn.player == "Defensor":
            if self.blockSelected == "Wood":
                self.woodAmmo -= 1
            elif self.blockSelected == "Concrete":
                self.concreteAmmo -= 1
            elif self.blockSelected == "Iron":
                self.ironAmmo -= 1

    def ReloadAmmo(self):
        if self.reloadFlag == 0:
            self.bombAmmo += 5
            self.fireAmmo += 5
            self.waterAmmo += 5
            self.reloadFlag += 1

    def Player1Turn(self):
        self.SelectIcon()
        self.readyButton = Button(self.GbuttonImage, pos=(400, 550),
               textInput="Ready", font=self.GetFont(12), baseColor="White", hoveringColor="Purple")

    def Player2Turn(self):
        self.tank.draw(self.screen)
        keys = pygame.key.get_pressed()
        self.Player2Movement(keys)
        self.Player2Shooting(keys)
        self.tank.update()
        self.SelectIcon()
        """  --------------------- COLLISIONS ---------------------------------------------- """
        if self.tank.rect.left < 50:
            self.tank.rect.left = 50
            self.tank.update()
        if self.tank.rect.right > self.width:
            self.tank.rect.right = self.width
            self.tank.update()
        if self.tank.rect.top < 100:
            self.tank.rect.top = 100
            self.tank.update()
        if self.tank.rect.bottom > self.height - 100:
            self.tank.rect.bottom = self.height - 100

        for block_list in [self.woodBlocks, self.concreteBlocks, self.ironBlocks]:
            for block in block_list:
                if block.isCollision(self.tank.rect):
                    if self.tank.speed_x > 0:
                        self.tank.rect.x -= self.tank.speed_x
                    if self.tank.speed_x < 0:
                        self.tank.rect.x -= self.tank.speed_x
                    if self.tank.speed_y > 0:
                        self.tank.rect.y -= self.tank.speed_y
                    if self.tank.speed_y < 0:
                        self.tank.rect.y -= self.tank.speed_y

                if self.fire == "fire":
                    if block.isCollision(self.bullet.rect):
                        self.tank.stopSound()
                        block.playSound()
                        self.UpdateAmmo()
                        self.fire = "ready"
                        if self.bullet.type == "Bomb":
                            if block in self.woodBlocks:
                                self.woodBlocks.remove(block)
                            if block in self.concreteBlocks:
                                block.updateHP(3)
                                if block.hp <= 0:
                                    self.concreteBlocks.remove(block)
                            if block in self.ironBlocks:
                                block.updateHP(3)
                                if block.hp <= 0:
                                    self.ironBlocks.remove(block)
                        if self.bullet.type == "Fire":
                            if block in self.woodBlocks:
                                self.woodBlocks.remove(block)
                            if block in self.concreteBlocks:
                                block.updateHP(2)
                                if block.hp <= 0:
                                    self.concreteBlocks.remove(block)
                            if block in self.ironBlocks:
                                block.updateHP(3)
                                if block.hp <= 0:
                                    self.ironBlocks.remove(block)
                        if self.bullet.type == "Water":
                            if block in self.woodBlocks:
                                self.woodBlocks.remove(block)
                            if block in self.concreteBlocks:
                                block.updateHP(1)
                                if block.hp <= 0:
                                    self.concreteBlocks.remove(block)
                            if block in self.ironBlocks:
                                block.updateHP(2)
                                if block.hp <= 0:
                                    self.ironBlocks.remove(block)

        if self.fire == "fire":
            self.bullet.DrawBullet()
            if not self.bullet.Trajectory() or self.bullet.is_Collision(self.Eagle.rect):
                self.tank.stopSound()
                self.bullet.CollisionSound()
                self.UpdateAmmo()
                self.fire = "ready"
        """  --------------------- COLLISIONS ---------------------------------------------- """
        if self.gameTurn.time % 30 == 0:
            self.ReloadAmmo()
        else:
            self.reloadFlag = 0

    def Player2Shooting(self, keys):
        if keys[pygame.K_SPACE]:
            if self.fire == "ready" and not self.OutOfAmmo() and self.aim == "ready":
                self.bullet = self.bulletFactory.CreateBullet(
                    self.bulletSelected, self.tank.rect.x, self.tank.rect.y, self.tank.direction, self.screen)
                self.fire = "fire"
                self.tank.playSound()

    def Player2Movement(self, keys):
        if keys[pygame.K_w]:
            self.tank.speed_y -= self.tank.acceleration
            self.tank.direction = "up"
            self.aim = "ready"
        if keys[pygame.K_s]:
            self.tank.speed_y += self.tank.acceleration
            self.tank.direction = "down"
            self.aim = "ready"
        if keys[pygame.K_a]:
            self.tank.speed_x -= self.tank.acceleration
            if keys[pygame.K_w]:
                self.tank.direction = "up_left"
                self.aim = "None"
            elif keys[pygame.K_s]:
                self.tank.direction = "down_left"
                self.aim = "None"
            else:
                self.tank.direction = "left"
                self.aim = "ready"
        if keys[pygame.K_d]:
            self.tank.speed_x += self.tank.acceleration
            if keys[pygame.K_w]:
                self.tank.direction = "up_right"
                self.aim = "None"
            elif keys[pygame.K_s]:
                self.tank.direction = "down_right"
                self.aim = "None"
            else:
                self.tank.direction = "right"
                self.aim = "ready"

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
        self.gameTurn.player = "Defensor"
        self.gameTurn.time = int(pygame.mixer.Sound(self.songRoute).get_length())
        pygame.mixer.music.load(self.songRoute)
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        fps = 60

        time_elapsed = 0
        # print(seconds)

        while True:
            """  --------------------- PLAYERS INFO ---------------------------------------------- """
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Eagle.sprite, self.Eagle.rect)
            x, y = pygame.mouse.get_pos()
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
            """  --------------------- PLAYERS INFO ---------------------------------------------- """

            """  --------------------- TIMER ----------------------------------------------------- """
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
            """  --------------------- TIMER ----------------------------------------------------- """

            """  --------------------- COUNTERS AND ANIMATIONS ----------------------------------------------------- """
            self.AmmoCounters()
            self.AmmoImg()
            self.SelectionAnimation()
            """  --------------------- COUNTERS AND ANIMATIONS ----------------------------------------------------- """

            if self.gameTurn.CheckTurn(self.gameTurn.time):
                self.gameTurn.player, self.gameTurn.time = self.gameTurn.ChangeTurn(self.gameTurn.player,
                                                                                    self.player1.song,
                                                                                    self.player2.song)
                if self.gameTurn.player == "Defensor":
                    pygame.mixer.music.stop()
                    self.songRoute = self.player1.song
                    pygame.mixer.music.load(self.songRoute)
                    pygame.mixer.music.set_volume(0.02)
                    pygame.mixer.music.play(-1)
                if self.gameTurn.player == "Atacante":
                    pygame.mixer.music.stop()
                    self.songRoute = self.player2.song
                    pygame.mixer.music.load(self.songRoute)
                    pygame.mixer.music.set_volume(0.02)
                    pygame.mixer.music.play(-1)

            if self.gameTurn.player == "Atacante":
                self.Player2Turn()

            elif self.gameTurn.player == "Defensor":
                self.Player1Turn()
                self.readyButton.ChangeColor((x, y))
                self.readyButton.UpdateScreen(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.gameTurn.player == "Defensor":

                            if self.readyButton.CheckForInput((x, y)):
                                self.gameTurn.player, self.gameTurn.time = self.gameTurn.ChangeTurn(self.gameTurn.player
                                                                                                    , self.player1.song,
                                                                                                    self.player2.song)
                                pygame.mixer.music.stop()
                                self.songRoute = self.player1.song
                                pygame.mixer.music.load(self.songRoute)
                                pygame.mixer.music.set_volume(0.02)
                                pygame.mixer.music.play(-1)

                            if not self.OutOfAmmo():
                                block = self.BlockFactory.CreateBlock(self.blockSelected, x, y, self.screen)
                                if self.blockSelected == "Wood":
                                    if block.flag and (block.BlockX, block.BlockY) not in self.coordinates:
                                        self.coordinates.append((block.BlockX, block.BlockY))
                                        self.woodBlocks.append(block)
                                        self.UpdateAmmo()
                                if self.blockSelected == "Iron":
                                    if block.flag and (block.BlockX, block.BlockY) not in self.coordinates:
                                        self.coordinates.append((block.BlockX, block.BlockY))
                                        self.ironBlocks.append(block)
                                        self.UpdateAmmo()
                                if self.blockSelected == "Concrete":
                                    if block.flag and (block.BlockX, block.BlockY) not in self.coordinates:
                                        self.coordinates.append((block.BlockX, block.BlockY))
                                        self.concreteBlocks.append(block)
                                        self.UpdateAmmo()

            for block in self.woodBlocks:
                block.DrawBlock()
            for block in self.concreteBlocks:
                block.DrawBlock()
            for block in self.ironBlocks:
                block.DrawBlock()

            pygame.display.update()
            clock.tick(fps)
