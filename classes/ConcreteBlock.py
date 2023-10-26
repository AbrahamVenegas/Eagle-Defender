from abc import ABC
import pygame

from classes.Block import Block


class ConcreteBlock(Block, ABC):
    sprite = None
    type = None
    rect = None

    def __init__(self, BlockX, BlockY, surface):
        self.type = "Concrete"
        self.BlockX = BlockX
        self.BlockY = BlockY
        self.screen = surface
        self.sprite = pygame.image.load("assets/Concrete.png")
        self.rect = self.sprite.get_rect()
        self.flag = False
        self.SetPosition()

    def SetPosition(self):
        row = (self.BlockY // 32)
        column = (self.BlockX // 32)
        if 8 <= row <= 10 and 3 <= column <= 6:
            self.flag = False
        elif 3 < row < 15 and column > 1:
            self.rect.x = column * 32
            self.rect.y = row * 32
            self.flag = True

    def DrawBlock(self):
        if self.flag:
            self.screen.blit(self.sprite, self.rect)

    def isCollision(self, object):
        return self.rect.colliderect(object)