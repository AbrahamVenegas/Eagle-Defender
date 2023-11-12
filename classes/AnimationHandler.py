import pygame
import os


class AnimationHandler:
    def __init__(self, screen, animation_folder, x, y, animation_speed):
        self.screen = screen
        self.animation_folder = animation_folder
        self.x = x
        self.y = y
        self.play = False
        self.animation_speed = animation_speed
        self.animation_sprites = self.loadAnimation()
        self.current_frame = 0
        self.last_frame_time = pygame.time.get_ticks()

    def loadAnimation(self):
        animation_sprites = []
        for filename in os.listdir(self.animation_folder):
            if filename.endswith(".png"):
                image_path = os.path.join(self.animation_folder, filename)
                animation_sprites.append(pygame.image.load(image_path))
        return animation_sprites

    def playAnimation(self):
        self.play = True
        animation_img = self.animation_sprites[self.current_frame]
        animation_rect = animation_img.get_rect()
        animation_rect.x = self.x
        animation_rect.y = self.y
        self.screen.blit(animation_img, animation_rect)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.animation_speed:
            self.last_frame_time = current_time
            self.current_frame = (self.current_frame + 1) % len(self.animation_sprites)
            if self.current_frame == 0:
                self.play = False

    def updatePos(self, posx, posy):
        self.x = posx
        self.y = posy
