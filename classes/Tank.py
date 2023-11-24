import pygame
import serial
import threading

tank_sprites = [
    pygame.image.load("assets/Tank/tank1.png"),
    pygame.image.load("assets/Tank/tank2.png"),
    pygame.image.load("assets/Tank/tank3.png"),
    pygame.image.load("assets/Tank/tank4.png"),
    pygame.image.load("assets/Tank/tank5.png"),
    pygame.image.load("assets/Tank/tank6.png"),
    pygame.image.load("assets/Tank/tank7.png"),
    pygame.image.load("assets/Tank/tank8.png")
]

bullet_sprites = [
    pygame.image.load("assets/Weapons/Fire_rocket.png"),
    pygame.image.load("assets/Weapons/Water_rocket.png"),
    pygame.image.load("assets/Weapons/Bomb_rocket.png")
]


class Tank:
    images = {
        "left": pygame.image.load("assets/Tank/tank1.png"),
        "right": pygame.image.load("assets/Tank/tank5.png"),
        "up": pygame.image.load("assets/Tank/tank7.png"),
        "down": pygame.image.load("assets/Tank/tank3.png"),
        "up_right": pygame.image.load("assets/Tank/tank6.png"),
        "up_left": pygame.image.load("assets/Tank/tank8.png"),
        "down_right": pygame.image.load("assets/Tank/tank4.png"),
        "down_left": pygame.image.load("assets/Tank/tank2.png")
    }
    index = 0
    direction = "left"
    image = pygame.transform.scale(images[direction], (100, 60))
    rect = image.get_rect()
    rect.x = 700
    rect.y = 260
    speed_x = 0  # Velocidad horizontal
    speed_y = 0  # Velocidad vertical
    acceleration = 0.5  # Aceleración del movimiento
    friction = 0.2  # Fricción para el movimiento suave
    shootingSound = None
    def __int__(self, x, y):
        super().__init__()
        self.images = {
            "left": pygame.image.load("assets/Tank/tank1.png"),
            "right": pygame.image.load("assets/Tank/tank5.png"),
            "up": pygame.image.load("assets/Tank/tank7.png"),
            "down": pygame.image.load("assets/Tank/tank3.png"),
            "up_right": pygame.image.load("assets/Tank/tank6.png"),
            "up_left": pygame.image.load("assets/Tank/tank8.png"),
            "down_right": pygame.image.load("assets/Tank/tank4.png"),
            "down_left": pygame.image.load("assets/Tank/tank2.png")
        }
        self.index = 0
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        self.speed_x = 0  # Velocidad horizontal
        self.speed_y = 0  # Velocidad vertical
        self.acceleration = 0.2  # Aceleración del movimiento
        self.friction = 0.1  # Fricción para el movimiento suave
        self.direction = "left"
        self.image = self.images[self.direction]


    def update(self):
        # Aplicar fricción para el movimiento suave
        self.speed_x *= (1 - self.friction)
        self.speed_y *= (1 - self.friction)

        # Actualizar posición basada en la velocidad
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.image = self.images[self.direction]

    def playSound(self):
        self.shootingSound = pygame.mixer.Sound('assets/SoundEffects/Launch.mp3')
        self.shootingSound.set_volume(0.03)
        self.shootingSound.play()

    def stopSound(self):
        if self.shootingSound is not None:
            self.shootingSound.stop()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def Movement(self, keys, signal):
        if keys[pygame.K_w] or "up" in str(signal):
            self.speed_y -= self.acceleration
            self.direction = "up"
            return "ready"
        if keys[pygame.K_s] or "down" in str(signal):
            self.speed_y += self.acceleration
            self.direction = "down"
            return "ready"
        if keys[pygame.K_a] or "left" in str(signal):
            self.speed_x -= self.acceleration
            if keys[pygame.K_w]:
                self.direction = "up_left"
                return "None"
            elif keys[pygame.K_s] or "right" in str(signal):
                self.direction = "down_left"
                return "None"
            else:
                self.direction = "left"
                return "ready"
        if keys[pygame.K_d]:
            self.speed_x += self.acceleration
            if keys[pygame.K_w]:
                self.direction = "up_right"
                return "None"
            elif keys[pygame.K_s]:
                self.direction = "down_right"
                return "None"
            else:
                self.direction = "right"
                return "ready"
        return "ready"

    def BorderCollide(self, width, height):
        if self.rect.left < 50:
            self.rect.left = 50
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 100:
            self.rect.top = 100
        if self.rect.bottom > height - 100:
            self.rect.bottom = height - 100

    def blockCollide(self):
        if self.speed_x > 0:
            self.rect.x -= self.speed_x
        if self.speed_x < 0:
            self.rect.x -= self.speed_x
        if self.speed_y > 0:
            self.rect.y -= self.speed_y
        if self.speed_y < 0:
            self.rect.y -= self.speed_y
