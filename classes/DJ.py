import pygame


class DJ:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DJ, cls).__new__(cls)
        return cls._instance

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

    def isPlaying(self):
        return pygame.mixer.music.get_busy()

    def PlayLobbyMusic(self):
        pygame.mixer.music.load("assets/Music/Lobby_music.mp3")
        pygame.mixer.music.play(-1)
