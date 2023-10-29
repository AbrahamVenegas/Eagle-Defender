from abc import ABC
import pygame

from classes.Bullet import Bullet


class WaterBullet(Bullet, ABC):
    sprite0 = pygame.image.load("assets/Water_rocket.png")
    sprite = sprite0
    type = None
    maxRange = 256
    speed = 10
    tankX = tankY = 0
    bulletX = bulletY = 0
    rect = sprite.get_rect()

    def __init__(self, tankX, tankY, direction, surface):
        self.type = "Water"
        self.tankX = tankX
        self.tankY = tankY
        self.tankDirection = direction
        self.screen = surface
        self.RotateSprite()
        self.collideSound = pygame.mixer.Sound('assets/Explosion.mp3')
        self.collideSound.set_volume(0.5)

    def RotateSprite(self):
        if self.tankDirection == "left":
            self.sprite = self.sprite0
            self.rect = self.sprite.get_rect()
            self.rect.x = self.tankX - 10
            self.rect.y = self.tankY + 5

        elif self.tankDirection == "right":
            self.sprite = pygame.transform.rotate(self.sprite0, 180)
            self.rect = self.sprite.get_rect()
            self.rect.x = self.tankX + 60 + 10
            self.rect.y = self.tankY + 10

        elif self.tankDirection == "up":
            self.sprite = pygame.transform.rotate(self.sprite0, 270)
            self.rect = self.sprite.get_rect()
            self.rect.x = self.tankX + 44
            self.rect.y = self.tankY - 20

        elif self.tankDirection == "down":
            self.sprite = pygame.transform.rotate(self.sprite0, 90)
            self.rect = self.sprite.get_rect()
            self.rect.x = self.tankX + 44
            self.rect.y = self.tankY + 45

    def Trajectory(self):
        if self.tankDirection == "left":
            if self.BorderCollision():
                return False
            else:
                self.rect.x -= self.speed
        elif self.tankDirection == "right":
            if self.BorderCollision():
                return False
            else:
                self.rect.x += self.speed
        elif self.tankDirection == "up":
            if self.BorderCollision():
                return False
            else:
                self.rect.y -= self.speed
        elif self.tankDirection == "down":
            if self.BorderCollision():
                return False
            else:
                self.rect.y += self.speed
        return True

    def is_Collision(self, objectRect):
        return self.rect.colliderect(objectRect)

    def BorderCollision(self):
        if self.rect.x < self.tankX - self.maxRange or self.rect.x < 50:  # Max trajectory + border collision
            return True
        elif self.rect.x > self.tankX + self.maxRange or self.rect.x > 800:
            return True
        elif self.rect.y < self.tankY - self.maxRange or self.rect.y < 100:
            return True
        elif self.rect.y > self.tankY + self.maxRange or self.rect.y > 476:
            return True
        else:
            return False

    def DrawBullet(self):
        self.screen.blit(self.sprite, self.rect)

    def CollisionSound(self):
        self.collideSound.set_volume(0.1)
        self.collideSound.play()
