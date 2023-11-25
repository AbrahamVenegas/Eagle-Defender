import pygame
import sys
import json
from classes.Player import Player
from classes.Tank import Tank
from classes.Turn import Turn
from classes.Tank import bullet_sprites
from classes.Bullets.BulletFactory import BulletFactory
from classes.Blocks.BlockFactory import BlockFactory
from classes.Eagle import Eagle
from classes.button import Button
from classes.Timer import Timer
from classes.DJ import DJ
from graphics.PauseWindow import PauseWindow
from classes.AnimationHandler import AnimationHandler
from REST_API.JSONAdapter import JSONAdapter
from REST_API.Loader import Loader
from classes.Cursor import Cursor


class GameWindow:
    screen = None
    background = None
    player1 = None
    player2 = None
    gameTurn = None
    timer = None
    selectionX = 380
    selectionY = 2
    bulletFactory = BulletFactory()
    bullet = None
    bulletSelected = "Fire"
    blockSelected = "Wood"
    fire = "ready"
    selectionCount = 1
    BlockFactory = BlockFactory()
    loader = Loader()
    dj = None
    ironBlocks = []
    concreteBlocks = []
    woodBlocks = []
    fireAmmo = 5
    waterAmmo = 5
    bombAmmo = 5
    ironAmmo = 10
    concreteAmmo = 10
    woodAmmo = 10
    gameState = True
    gameTime = 0

    def __init__(self):
        self.width = 800
        self.height = 576
        self.player1 = Player(None, None, None, None, None, None, None)
        self.player2 = Player(None, None, None, None, None, None, None)
        self.selectAnimation = None
        self.explosionAnimation = None
        self.explosionFlag = False
        self.gameTurn = Turn(None, None)
        self.GbuttonImage = pygame.transform.scale(pygame.image.load("assets/Buttons/GreenButton.png"), (110, 50))
        self.RbuttonImage = pygame.transform.scale(pygame.image.load("assets/Buttons/RedButton.png"), (110, 50))
        self.readyButton = None
        self.tank = Tank()
        self.cursor = Cursor()
        self.coordinates = []
        self.blocksCollector = []
        self.text1 = self.text2 = self.text3 = None
        self.selectSprites = None
        self.Eagle = Eagle()
        self.reloadFlag = self.blocksDestroyed = 0
        self.foraneo = 1
        self.aim = "ready"
        self.keyState = {}
        self.score = 0
        self.adapter = JSONAdapter()

    def Reset(self):
        self.ironBlocks = []
        self.concreteBlocks = []
        self.woodBlocks = []
        self.tank.rect.x = 700
        self.tank.rect.y = 260

    def GetFont(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def FillPlayer1Info(self):
        with open("json/player1.json", "r") as jsonFile:
            datos = json.load(jsonFile)
        self.player1.SetData(datos)

    def FillPlayer2Info(self):
        with open("json/player2.json", "r") as jsonFile:
            datos = json.load(jsonFile)
        self.player2.SetData(datos)

    def LoadGame(self):
        self.woodBlocks.clear()
        self.ironBlocks.clear()
        self.concreteBlocks.clear()
        json = self.loader.loadGame()
        count = 0
        woodLife = eval(json['woodLife'])
        ironLife = eval(json['ironLife'])
        concreteLife = eval(json['concreteLife'])
        bullets = json['Bullets']
        tankPos = json['Tank']
        if json is not None:
            for block in eval(json['wood']):
                self.woodBlocks.append(self.BlockFactory.CreateBlock('Wood', block[0]*32, block[1]*32, self.screen))
                self.woodBlocks[count].updateHP(3-(int(woodLife[count])))
                count += 1
            count = 0
            for block in eval(json['iron']):
                self.ironBlocks.append(self.BlockFactory.CreateBlock('Iron', block[0]*32, block[1]*32, self.screen))
                self.ironBlocks[count].updateHP(3-(int(ironLife[count])))
                count += 1
            count = 0
            for block in eval(json['concrete']):
                self.concreteBlocks.append(self.BlockFactory.CreateBlock('Concrete', block[0] * 32, block[1] * 32, self.screen))
                self.concreteBlocks[count].updateHP(3-(int(concreteLife[count])))
                count += 1
        self.woodAmmo = json['woodCounter']
        self.ironAmmo = json['ironCounter']
        self.concreteAmmo = json['concreteCounter']
        self.gameTurn.player = json['turn']
        self.timer.reset(int(json['time']))
        self.tank.rect.x = int(tankPos[0])
        self.tank.rect.y = int(tankPos[1])
        self.bombAmmo = int(bullets[0])
        self.fireAmmo = int(bullets[1])
        self.waterAmmo = int(bullets[2])


    def SetScore(self):
        scoreText = self.GetFont(16).render("Score: " + str(self.score), True, "White")
        self.screen.blit(scoreText, (360, 545))

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
        font = self.GetFont(fontSize)
        if self.gameTurn.player == "Atacante":
            self.text1 = font.render(":" + str(self.fireAmmo), True, "White")
            self.text2 = font.render(":" + str(self.waterAmmo), True, "White")
            self.text3 = font.render(":" + str(self.bombAmmo), True, "White")

        elif self.gameTurn.player == "Defensor":
            self.text1 = font.render(":" + str(self.woodAmmo), True, "White")
            self.text2 = font.render(":" + str(self.concreteAmmo), True, "White")
            self.text3 = font.render(":" + str(self.ironAmmo), True, "White")

        rect1 = self.text1.get_rect(center=(430, 20))
        rect2 = self.text1.get_rect(center=(510, 20))
        rect3 = self.text1.get_rect(center=(350, 20))
        self.screen.blit(self.text1, rect1)
        self.screen.blit(self.text2, rect2)
        self.screen.blit(self.text3, rect3)

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

    def ForaneoBuff(self, flag):
        if self.foraneo == 0 and flag:
            self.waterAmmo += self.dj.BeneficioForaneo()
        elif self.foraneo == 0 and not flag:
            self.waterAmmo -= self.dj.BeneficioForaneo()
        self.foraneo += 1

    def Player1Turn(self):
        keys = pygame.key.get_pressed()
        self.cursor.Movement(keys)
        if self.cursor.flag:
            self.readyButton = Button(self.GbuttonImage, pos=(730, 80),
                                      textInput="Ready", font=self.GetFont(12), baseColor="White",
                                      hoveringColor="Purple")
        else:
            self.readyButton = Button(self.RbuttonImage, pos=(730, 80),
                                      textInput="Ready", font=self.GetFont(12), baseColor="White",
                                      hoveringColor="Purple")
        self.cursor.draw(self.screen)
        self.SelectIcon()

    def showMusicInfo(self):
        font = self.GetFont(12)
        tempo = font.render(f"Tempo: {self.dj.tempo}", True, 'White')
        pop = font.render(f"Pop: {self.dj.popularidad}", True, 'White')
        baila = font.render(f"Bailabilidad: {self.dj.bailabilidad}", True, 'White')
        acustico = font.render(f"Acustico: {self.dj.acustico}", True, 'White')
        title = font.render("MUSICA", True, 'White')
        image = pygame.image.load("assets/MediumRectangle.png")
        box = pygame.transform.scale(image, (200, 100))

        self.screen.blit(box, (10, 60))
        self.screen.blit(title, (10, 65))
        self.screen.blit(tempo, (10, 85))
        self.screen.blit(pop, (10, 100))
        self.screen.blit(baila, (10, 115))
        self.screen.blit(acustico, (10, 130))


    def Player2Turn(self):
        self.tank.draw(self.screen)
        keys = pygame.key.get_pressed()
        self.aim = self.tank.Movement(keys)
        self.Player2Shooting(keys)
        self.tank.update()
        self.SelectIcon()
        self.showMusicInfo()
        """  --------------------- COLLISIONS ---------------------------------------------- """
        self.tank.BorderCollide(self.width, self.height)

        for block_list in [self.woodBlocks, self.concreteBlocks, self.ironBlocks]:
            for block in block_list:
                if block.isCollision(self.tank.rect):
                    self.tank.blockCollide()
                if self.fire == "fire":
                    if block.isCollision(self.bullet.rect):
                        self.explosionFlag = True
                        self.explosionAnimation.updatePos(block.rect.x - 80, block.rect.y - 80)
                        self.tank.stopSound()
                        block.playSound()
                        self.score += 10
                        self.UpdateAmmo()
                        self.blocksDestroyed += 1
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
            if not self.bullet.Trajectory():
                self.tank.stopSound()
                self.bullet.CollisionSound()
                self.UpdateAmmo()
                self.fire = "ready"
            if self.bullet.is_Collision(self.Eagle.rect):
                self.tank.stopSound()
                self.bullet.CollisionSound()
                self.UpdateAmmo()
                self.fire = "ready"
                self.Eagle.lifePoints -= 1
        """  --------------------- COLLISIONS ---------------------------------------------- """
        if self.timer.attacker == 0:
            self.gameTime = 60
        else:
            self.gameTime = self.timer.attacker
        if (self.gameTime - self.timer.time) % 30 == 0 and self.timer.time != 60:
            halfBlocks = int((30 - (self.ironAmmo + self.concreteAmmo + self.woodAmmo))/2)
            if self.blocksDestroyed <= halfBlocks:
                self.ForaneoBuff(True)
            self.ReloadAmmo()
        elif self.timer.time == 20:
            self.ForaneoBuff(False)
        else:
            self.reloadFlag = 0
            self.foraneo = 0

        if self.timer.attacker == 0:
            if (60 - self.timer.time) % 25 == 0:
                for block in self.blocksCollector:
                    block.ResetHP()
                    if block.type == "Wood" and block not in self.woodBlocks:
                        self.woodBlocks.append(block)
                    if block.type == "Concrete" and block not in self.concreteBlocks:
                        self.concreteBlocks.append(block)
                    if block.type == "Iron" and block not in self.ironBlocks:
                        self.ironBlocks.append(block)
        else:
            if (self.timer.attacker - self.timer.time) % 25 == 0:
                for block in self.blocksCollector:
                    block.ResetHP()
                    if block.type == "Wood" and block not in self.woodBlocks:
                        self.woodBlocks.append(block)
                    if block.type == "Concrete" and block not in self.concreteBlocks:
                        self.concreteBlocks.append(block)
                    if block.type == "Iron" and block not in self.ironBlocks:
                        self.ironBlocks.append(block)

    def Player2Shooting(self, keys):
        if keys[pygame.K_SPACE]:
            if self.fire == "ready" and not self.OutOfAmmo() and self.aim == "ready":
                self.bullet = self.bulletFactory.CreateBullet(
                    self.bulletSelected, self.tank.rect.x, self.tank.rect.y, self.tank.direction, self.screen)
                self.fire = "fire"
                self.tank.playSound()

    def Start(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("assets/Mapa2 grid.png")
        pygame.display.set_caption("Eagle Defender")
        self.FillPlayer1Info()
        self.FillPlayer2Info()
        self.selectAnimation = AnimationHandler(self.screen, "assets/SelectionAnimation/", self.selectionX
                                                , self.selectionY, 300)
        self.explosionAnimation = AnimationHandler(self.screen, "assets/ExplosionAnimation/", 0, 0,
                                                   16)
        if self.gameState:
            self.timer = Timer()
            self.timer.defenderTime()
            self.timer.start()
            self.dj = DJ()
            self.dj.NewSong(self.player1.song)
            self.gameTurn.player = "Defensor"
        else:
            self.dj.Continue()

        clock = pygame.time.Clock()
        fps = 60

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

            """  --------------------- COUNTERS AND ANIMATIONS ----------------------------------------------------- """
            self.AmmoCounters()
            self.AmmoImg()
            self.selectAnimation.updatePos(self.selectionX, self.selectionY)

            self.selectAnimation.playAnimation()
            self.SetScore()
            """  --------------------- COUNTERS AND ANIMATIONS ----------------------------------------------------- """

            """  --------------------- TIMER ----------------------------------------------------- """
            self.timer.update()
            self.timer.draw(self.screen, self.GetFont(14), 630, 545)
            """  --------------------- TIMER ----------------------------------------------------- """

            if self.gameTurn.CheckTurn(self.timer.time):
                if self.gameTurn.player == "Defensor":
                    self.gameTurn.player, self.gameTurn.time = self.gameTurn.ChangeTurn(self.gameTurn.player,
                                                                                    self.player1.song,
                                                                                    self.player2.song)
                    self.timer.attackTime()
                if self.gameTurn.player == "Defensor":
                    self.dj.Stop()
                    self.dj.NewSong(self.player1.song)
                elif self.gameTurn.player == "Atacante":
                    self.dj.Stop()
                    self.dj.NewSong(self.player2.song)

            for block in self.woodBlocks:
                block.DrawBlock()
            for block in self.concreteBlocks:
                block.DrawBlock()
            for block in self.ironBlocks:
                block.DrawBlock()

            if self.gameTurn.player == "Atacante":
                self.Player2Turn()
                if self.Eagle.lifePoints == 0:
                    self.dj.Stop()
                    if self.timer.attacker == 0:  # Default time
                        return ["Finish", self.player2.username, self.player1.username,
                                60 - self.timer.time]
                    else:
                        return ["Finish", self.player2.username, self.player1.username,
                                self.timer.attacker - self.timer.time]

                if self.timer.time == 0:
                    self.dj.Stop()
                    if self.timer.attacker == 0:
                        return ["Finish", self.player1.username, self.player2.username, 60 - self.timer.time]
                    else:
                        return ["Finish", self.player1.username, self.player2.username, self.timer.attacker]

                if self.explosionFlag:
                    self.explosionAnimation.playAnimation()
                    self.explosionFlag = self.explosionAnimation.play

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
                        self.gameState = False
                        self.dj.PauseSong()
                        self.adapter.clear()
                        self.adapter.getBlocksInfo([self.woodBlocks, self.concreteBlocks, self.ironBlocks],
                                                   [self.woodAmmo, self.ironAmmo, self.concreteAmmo])
                        self.adapter.getPlayersInfo(self.gameTurn.player, self.timer.time)
                        self.adapter.getTankInfo(self.tank.rect.x, self.tank.rect.y)
                        self.adapter.getAmmoInfo(self.bombAmmo, self.fireAmmo, self.waterAmmo)
                        load = ""
                        if self.gameTurn.player == "Defensor":
                            return ["Pause", self.player1.username, self.player1.email]
                        elif self.gameTurn.player == "Atacante":
                            return ["Pause", self.player2.username, self.player2.email]
                        self.dj.Continue()
                        if load == "Load":
                            self.LoadGame()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        if self.gameTurn.player == "Defensor":
                            if self.cursor.flag:
                                cursorX, cursorY = self.cursor.GetPos()
                                if not self.OutOfAmmo():
                                    block = self.BlockFactory.CreateBlock(self.blockSelected, cursorX, cursorY, self.screen)
                                    if (block.BlockX, block.BlockY) not in self.coordinates and block.flag:
                                        if self.blockSelected == "Wood":
                                            self.coordinates.append((block.BlockX, block.BlockY))
                                            self.woodBlocks.append(block)
                                            self.blocksCollector.append(block)
                                            self.UpdateAmmo()
                                        if self.blockSelected == "Iron":
                                            self.coordinates.append((block.BlockX, block.BlockY))
                                            self.ironBlocks.append(block)
                                            self.blocksCollector.append(block)
                                            self.UpdateAmmo()
                                        if self.blockSelected == "Concrete":
                                            self.coordinates.append((block.BlockX, block.BlockY))
                                            self.concreteBlocks.append(block)
                                            self.blocksCollector.append(block)
                                            self.UpdateAmmo()
                                    else:
                                        cursorX = cursorX // 32
                                        cursorY = cursorY // 32
                                        if (cursorX, cursorY) in self.coordinates:
                                            for blockType in [self.woodBlocks, self.concreteBlocks, self.ironBlocks]:
                                                for block in blockType:
                                                    if block.BlockX == cursorX and block.BlockY == cursorY:
                                                        blockType.remove(block)
                                                        self.coordinates.remove((block.BlockX, block.BlockY))
                                                        if block.type == "Wood":
                                                            self.woodAmmo += 1
                                                        if block.type == "Iron":
                                                            self.ironAmmo += 1
                                                        if block.type == "Concrete":
                                                            self.concreteAmmo += 1
                            else:
                                self.gameTurn.player, self.gameTurn.time = self.gameTurn.ChangeTurn(
                                    self.gameTurn.player
                                    , self.player1.song,
                                    self.player2.song)
                                self.timer.attackTime()
                                self.dj.Stop()
                                self.dj.NewSong(self.player2.song)

            pygame.display.update()
            clock.tick(fps)
