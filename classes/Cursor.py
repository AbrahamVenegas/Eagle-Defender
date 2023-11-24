import pygame


class Cursor:

    def __init__(self):
        self.image = pygame.image.load("assets/SelectionAnimation/Select_0.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 256
        self.flag = True

    def draw(self, surface):
        if self.flag:
            surface.blit(self.image, self.rect)

    def Movement(self, keys):
        if keys[pygame.K_w]:
            if self.verifyPos("up") == "move":
                self.rect.y -= 32
                self.flag = True
            if self.verifyPos("up") == "ready":
                self.flag = False
        if keys[pygame.K_s]:
            if self.verifyPos("down") == "move":
                self.rect.y += 32
                self.flag = True
        if keys[pygame.K_a]:
            if self.verifyPos("left") == "move":
                self.rect.x -= 32
                self.flag = True
        if keys[pygame.K_d]:
            if self.verifyPos("right") == "move":
                self.rect.x += 32
                self.flag = True

    def verifyPos(self, direction):
        posY = self.rect.y // 32
        posX = self.rect.x // 32
        if direction == "up":
            posY -= 1
        elif direction == "down":
            posY += 1
        elif direction == "left":
            posX -= 1
        elif direction == "right":
            posX += 1

        if (8 <= posY <= 10 and 3 <= posX <= 6) or (7 <= posY <= 10 and 21 <= posX <= 24) or posX > 24:
            return "noMove"
        elif posY == 3 and 21 <= posX <= 24:
            return "ready"
        elif 3 < posY < 15 and posX > 1:
            return "move"
    def GetPos(self):
        return self.rect.x, self.rect.y
