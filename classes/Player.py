import pygame
import sys


class Player:
    username = None
    password = None
    email = None
    age = None
    photo = None
    song = None

    def __init__(self, username, password, email, age, photo, song):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.photo = photo
        self.song = song

    def display_info(self):
        print("Username:", self.username)
        print("Password:", self.password)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Photo:", self.photo)
        print("Song:", self.song)
