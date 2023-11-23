import pygame


class Eagle:

    def __init__(self):
        self.lifePoints = 1
        self.img = pygame.image.load("assets/Eagle.png")
        self.sprite = pygame.transform.flip(self.img, True, False)
        self.rect = self.sprite.get_rect()
        self.rect.x = 130
        self.rect.y = 225
