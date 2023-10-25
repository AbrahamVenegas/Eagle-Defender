import pygame

tank_sprites = [
    pygame.image.load("assets/tank1.png"),
    pygame.image.load("assets/tank2.png"),
    pygame.image.load("assets/tank3.png"),
    pygame.image.load("assets/tank4.png"),
    pygame.image.load("assets/tank5.png"),
    pygame.image.load("assets/tank6.png"),
    pygame.image.load("assets/tank7.png"),
    pygame.image.load("assets/tank8.png")
]

bullet_sprites = [
    pygame.image.load("assets/Fire_rocket_left.png"),
    pygame.image.load("assets/Water_rocket.png"),
    pygame.image.load("assets/Bomb_rocket.png")
]


class Tank:
    images = {
        "left": pygame.image.load("assets/tank1.png"),
        "right": pygame.image.load("assets/tank5.png"),
        "up": pygame.image.load("assets/tank7.png"),
        "down": pygame.image.load("assets/tank3.png"),
        "up_right": pygame.image.load("assets/tank6.png"),
        "up_left": pygame.image.load("assets/tank8.png"),
        "down_right": pygame.image.load("assets/tank4.png"),
        "down_left": pygame.image.load("assets/tank2.png")
    }
    index = 0
    direction = "left"
    image = pygame.transform.scale(images[direction], (100, 60))
    rect = image.get_rect()
    rect.x = 500
    rect.y = 260
    speed_x = 0  # Velocidad horizontal
    speed_y = 0  # Velocidad vertical
    acceleration = 0.5  # Aceleración del movimiento
    friction = 0.2  # Fricción para el movimiento suave

    def __int__(self, x, y):
        super().__init__()
        self.images = {
            "left": pygame.image.load("assets/tank1.png"),
            "right": pygame.image.load("assets/tank5.png"),
            "up": pygame.image.load("assets/tank7.png"),
            "down": pygame.image.load("assets/tank3.png"),
            "up_right": pygame.image.load("assets/tank6.png"),
            "up_left": pygame.image.load("assets/tank8.png"),
            "down_right": pygame.image.load("assets/tank4.png"),
            "down_left": pygame.image.load("assets/tank2.png")
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

    def draw(self, surface):
        surface.blit(self.image, self.rect)
