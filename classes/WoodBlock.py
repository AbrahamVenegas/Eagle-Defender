from abc import ABC
import pygame

from classes.Block import Block


class WoodBlock(Block, ABC):
    sprite = pygame.image.load("assets/Wood.png")
    type = None
    BlockX = BlockY = 0
    bulletX = bulletY = 0
    rect = sprite.get_rect()

    def __init__(self, BlockX, BlockY, surface):
        self.type = "Wood"
        self.BlockX = BlockX
        self.BlockY = BlockY
        self.screen = surface

    def SetPosition(self, mouseX, mouseY):
        row = (mouseY // 32)
        column = (mouseX // 32)
        if 8 <= row <= 10 and 3 <= column <= 6:
            pass
        elif 3 < row < 15 and column > 1:
            self.rect.x = column * 32
            self.rect.y = row * 32

    def DrawBlock(self):
        self.screen.blit(self.sprite, self.rect)
