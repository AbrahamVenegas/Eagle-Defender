from abc import ABC
import pygame

from classes.Block import Block


class WoodBlock(Block, ABC):
    sprite = None
    type = None
    rect = None
    woodSound = None

    def __init__(self, BlockX, BlockY, surface):
        self.type = "Wood"
        self.BlockX = BlockX
        self.BlockY = BlockY
        self.screen = surface
        self.images = ["assets/Blocks/Wood3.png", "assets/Blocks/Wood2.png", "assets/Blocks/Wood1.png"]
        self.hp = 3
        self.sprite = pygame.image.load(self.images[self.hp - 1])
        self.rect = self.sprite.get_rect()
        self.flag = False
        self.SetPosition()

    def SetPosition(self):
        self.BlockY = self.BlockY // 32
        self.BlockX = self.BlockX // 32
        if (8 <= self.BlockY <= 10 and 3 <= self.BlockX <= 6) or (7 <= self.BlockY <= 10 and 21 <= self.BlockX <= 24):
            self.flag = False
        elif 3 < self.BlockY < 15 and self.BlockX > 1:
            self.rect.x = self.BlockX * 32
            self.rect.y = self.BlockY * 32
            self.flag = True

    def DrawBlock(self):
        if self.flag:
            self.screen.blit(self.sprite, self.rect)

    def isCollision(self, Object):
        return self.rect.colliderect(Object)

    def updateHP(self, damage):
        self.hp -= damage
        if self.hp > 0:
            self.sprite = pygame.image.load(self.images[self.hp - 1])

    def playSound(self):
        self.woodSound = pygame.mixer.Sound('assets/SoundEffects/WoodCracking.mp3')
        self.woodSound.set_volume(0.1)
        self.woodSound.play()
