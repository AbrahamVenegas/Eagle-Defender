import pygame


class DJ:

    def __init__(self, songRoute):
        pygame.mixer.init()
        self.song = songRoute
        pygame.mixer.music.set_volume(0.02)

    def Stop(self):
        pygame.mixer.stop()

    def Play(self):
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(-1)

    def NewSong(self, song):
        self.song = song
        self.Play()

    def PauseSong(self):
        pygame.mixer.music.pause()

    def Continue(self):
        pygame.mixer.music.unpause()
