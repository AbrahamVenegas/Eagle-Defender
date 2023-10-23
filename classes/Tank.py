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
    pygame.image.load("assets/Fire_rocket.png"),
    pygame.image.load("assets/Water_rocket.png"),
    pygame.image.load("assets/Bomb_rocket.png")
]


class Tank:
    RIGHT = LEFT = UP = DOWN = False
    Directions = {"RIGHT": RIGHT, "LEFT": LEFT, "UP": UP, "DOWN": DOWN}
    images = tank_sprites
    index = 0
    image = pygame.transform.scale(images[index], (100, 60))
    rect = image.get_rect()
    rect.x = 500
    rect.y = 260
    speed_x = 0  # Velocidad horizontal
    speed_y = 0  # Velocidad vertical
    acceleration = 0.5  # Aceleración del movimiento
    friction = 0.2  # Fricción para el movimiento suave

    def __int__(self, x, y):
        self.images = tank_sprites
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0  # Velocidad horizontal
        self.speed_y = 0  # Velocidad vertical
        self.acceleration = 0.2  # Aceleración del movimiento
        self.friction = 0.1  # Fricción para el movimiento suave

    def update(self):
        # Aplicar fricción para el movimiento suave
        self.speed_x *= (1 - self.friction)
        self.speed_y *= (1 - self.friction)

        # Actualizar posición basada en la velocidad
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        #self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def directionFlags(self, direction):
        for item in self.Directions:
            if item == direction:
                self.Directions[direction] = True
            else:
                self.Directions[item] = False



