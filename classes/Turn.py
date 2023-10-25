import pygame

class Turn:
    time = None
    player = None

    def __init__(self, time, player):
        self.time = time
        self.player = player

    def ChangeTurn(self, player, songRoute1, songRoute2):
        if player == "Defensor":
            return "Atacante", int(pygame.mixer.Sound(songRoute2).get_length())
        elif player == "Atacante":
            return "Defensor", int(pygame.mixer.Sound(songRoute1).get_length())

    def CheckTurn(self, time):
        if time == 0:
            return True