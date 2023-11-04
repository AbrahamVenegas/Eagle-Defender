import pygame


class Timer:
    def __init__(self, screen, x, y, font, time_limit_seconds):
        self.screen = screen
        self.x = x
        self.y = y
        self.font = font
        self.time = time_limit_seconds
        self.time_elapsed = 0
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def reset(self, newTime):
        self.time = newTime

    def update(self):
        if self.running:
            actual_Time = pygame.time.get_ticks() // 1000
            past_time = actual_Time - self.time_elapsed
            if past_time >= 1 and self.time >= 1:
                self.time -= 1
                self.time_elapsed = actual_Time

    def draw(self):
        text = self.font.render(f"Tiempo: {self.time}s", True, "White")
        self.screen.blit(text, (self.x, self.y))
