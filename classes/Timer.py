import pygame


class Timer:
    _instance = None
    time = 60
    defender = attacker = 0

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Timer, cls).__new__(cls)
        return cls._instance

    def __init__(self):
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

    def setDefenderTime(self, time):
        if self.defender + time < 0:
            pass
        else:
            self.defender += time

    def setAttackerTime(self, time):
        if self.attacker + time < 0:
            pass
        else:
            self.attacker += time

    def attackTime(self):
        if self.attacker == 0:
            self.time = 60
        else:
            self.time = self.attacker

    def defenderTime(self):
        if self.defender == 0:
            self.time = 60
        else:
            self.time = self.defender

    def draw(self, screen, font, x, y):
        text = font.render(f"Tiempo: {self.time}s", True, "White")
        screen.blit(text, (x, y))
