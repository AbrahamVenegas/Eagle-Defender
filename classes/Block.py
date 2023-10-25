import pygame
import time
import random


class Block:
    images = [
        pygame.image.load("assets/Wood.png"),
        pygame.image.load("assets/Concrete.png"),
        pygame.image.load("assets/Iron.png"),
    ]

    def __init__(self):
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.acceleration = 0.2
        self.block_limit = 10
        self.block_counts = [0, 0, 0]
        self.blocks = []
        self.last_regeneration_time = time.time()
        self.active_block = None
        self.screen = None
        self.reset_time = 25
        self.last_reset = time.time()

    def update(self):
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

    def draw(self, screen):
        for block in self.blocks:
            self.screen.blit(block["image"], block["rect"])

    def set_active_block(self, image_path):
        self.images = [
            pygame.image.load(image_path)
        ]
        self.index = 0
        self.image = self.images[self.index]

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and len(self.blocks) < self.block_limit:
                x, y = event.pos
                block = {"image": self.image, "rect": self.image.get_rect(center=(x, y))}
                self.blocks.append(block)
            elif event.button == 3:
                x, y = event.pos
                for block in self.blocks:
                    if block["rect"].collidepoint(x, y):
                        self.blocks.remove(block)

    def reset_block_counts(self):
        for i in range(len(self.block_counts)):
            self.block_counts[i] = 0