import pygame
from button import Button
from StartWindow import StartWindow
import json
import sys
import requests
import os
import shutil
import easygui
import tkinter as tk
from tkinter import filedialog

class RegisterWindow:
    Screen = None
    username = ''
    password = ''
    email = ''
    age = ''
    photo = ''
    song = ''
    RegisterFlag = False
    songsFolder = "priv/songs"
    photosFolder = "priv/photos"
    def GetFont(self, size):  # To return it in the desired size
        return pygame.font.Font("assets/font.ttf", size)

    def RegisterScreen(self):
        pygame.init()  # starts it
        self.Screen = pygame.display.set_mode((1440, 810))  # To set the parameters of the window
        while True:

            """
            data = {"username": "abraham",
            "password": "1234",
            "email": "abravenegas@estudiantec.cr",
            "age": 20,
            "photo":b'101010101010",
            "song": b'1010101010
            }
            """

            pygame.display.set_caption("Registro")
            font = self.GetFont(36)
            clock = pygame.time.Clock()
            saveButton = Button(image=pygame.image.load("assets/BigRectangle.png"), pos=(720, 715),
                                textInput="Register", font=self.GetFont(50), baseColor="Black",
                                hoveringColor="Green")
            registerBack = Button(image=None, pos=(75, 30),
                                  textInput="BACK", font=self.GetFont(30), baseColor="Black", hoveringColor="Red")
            photoButton = Button(image=None, pos=(720, 500),
                                  textInput="Upload Photo", font=self.GetFont(30), baseColor="Black", hoveringColor="Green")
            songButton = Button(image=None, pos=(720, 600),
                                 textInput="Upload Song", font=self.GetFont(30), baseColor="Black", hoveringColor="Green")


            # Define input box dimensions and positions
            input_box_dimensions = [
                pygame.Rect(570, 100, 570, 50),
                pygame.Rect(570, 200, 300, 50),
                pygame.Rect(570, 300, 300, 50),
                pygame.Rect(570, 400, 300, 50),
            ]

            # Texts for the title of each input box
            input_texts = [
                "Insert your Username:",
                "Insert your Password:",
                "Insert your Email:",
                "Insert your Age:",
                "Insert your Photo:",
                "Insert your Song:"
            ]

            colorInactive = [pygame.Color('lightskyblue3')] * 4
            colorActive = pygame.Color('dodgerblue2')
            colors = colorInactive.copy()
            texts = [''] * 4
            actives = [False] * 4

            def save_to_file(data):
                with open('data.json', 'w') as f:
                    json.dump(data, f)

            while True:
                registerMousePosition = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    for i, box in enumerate(input_box_dimensions):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if box.collidepoint(event.pos):
                                actives = [False] * 4
                                actives[i] = True
                            else:
                                actives[i] = False
                            colors[i] = colorActive if actives[i] else colorInactive[i]

                    if event.type == pygame.KEYDOWN:
                        for i, active in enumerate(actives):
                            if active:
                                if event.key == pygame.K_RETURN:
                                    #print(f"Text {i + 1}: {texts[i]}")
                                    #data = {f'text{i + 1}': texts[i] for i in range(4)}
                                    #save_to_file(data)
                                    #self.username = texts[0]
                                    #self.password = texts[1]
                                    #self.email = texts[2]
                                    #self.age = texts[3]
                                    #self.photo = texts[4]
                                    #self.song = texts[5]
                                    print("Username:" + self.username)
                                elif event.key == pygame.K_BACKSPACE:
                                    texts[i] = texts[i][:-1]
                                else:
                                    texts[i] += event.unicode

                    # Check button clicks
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if saveButton.CheckForInput(registerMousePosition):
                            data = {f'text{i + 1}': texts[i] for i in range(4)}
                            save_to_file(data)
                            self.username = texts[0]
                            self.password = texts[1]
                            self.email = texts[2]
                            self.age = texts[3]
                            self.VerifyRegister()

                            startWindow = StartWindow._instance
                            startWindow.MainScreen()
                        elif photoButton.CheckForInput(registerMousePosition):

                            archivoFoto = self.selectPhoto()
                            if archivoFoto:
                                print(f"Archivo seleccionado: {archivoFoto}")
                                self.photo = archivoFoto
                            else:
                                print("Ningún archivo seleccionado")

                            #self.VerifyRegister()
                            data = {f'text{i + 1}': texts[i] for i in range(4)}
                            save_to_file(data)
                        elif songButton.CheckForInput(registerMousePosition):

                            archivoDestino = self.selectSong()
                            if archivoDestino:
                                print(f"Archivo seleccionado: {archivoDestino}")
                                self.song = archivoDestino
                            else:
                                print("Ningún archivo seleccionado")

                            #self.VerifyRegister()
                            data = {f'text{i + 1}': texts[i] for i in range(4)}
                            save_to_file(data)
                        elif registerBack.CheckForInput(registerMousePosition):
                            startWindow = StartWindow._instance
                            startWindow.MainScreen()
                            texts = [''] * 6

                self.Screen.fill(("white"))

                for i in range(4):
                    registerText = self.GetFont(25).render(input_texts[i], True, "Black")
                    registerRectangle = registerText.get_rect(center=(720, input_box_dimensions[i].y - 30))
                    self.Screen.blit(registerText, registerRectangle)

                    txt_surface = font.render(texts[i], True, colors[i])
                    width = max(300, txt_surface.get_width() + 10)
                    input_box_dimensions[i].w = width
                    self.Screen.blit(txt_surface, (input_box_dimensions[i].x + 5, input_box_dimensions[i].y + 5))
                    pygame.draw.rect(self.Screen, colors[i], input_box_dimensions[i], 2)

                saveButton.ChangeColor(registerMousePosition)
                saveButton.UpdateScreen(self.Screen)
                registerBack.ChangeColor(registerMousePosition)
                registerBack.UpdateScreen(self.Screen)
                songButton.ChangeColor(registerMousePosition)
                songButton.UpdateScreen(self.Screen)
                photoButton.ChangeColor(registerMousePosition)
                photoButton.UpdateScreen(self.Screen)
                pygame.display.flip()
                clock.tick(30)
    def VerifyRegister(self):
        urluser = "http://127.0.0.1:5000/api/register"
        headers = {'Content-Type': 'application/json'}
        data = {
            "username": self.username,
            "password": self.password,
             "email": self.email,
             "age": self.age,
             "photo": self.photo,
             "song": self.song
            }
        print(data)
        response = requests.post(urluser, headers=headers, json=data)
        if response.status_code == 201:
            print(response)


    def selectSong(self):
        root = tk.Tk()
        root.withdraw()  # Oculta la ventana principal de Tkinter

        # Utilizamos filedialog para mostrar la ventana de selección de archivos
        selectedArchive = filedialog.askopenfilename(
            title="Selecciona un archivo de imagen",
            filetypes=[("Song files", ("*.wav", "*.mp3"))]
        )

        if selectedArchive:
            songsFolder = "priv/songs"
            archiveName = os.path.basename(selectedArchive)
            destinePath = os.path.join(songsFolder, archiveName)
            shutil.copy(selectedArchive, destinePath)

        return os.path.basename(selectedArchive)  #Retorna solo el nombre del archivo

    def selectPhoto(self):
        root = tk.Tk()
        root.withdraw()  # Oculta la ventana principal de Tkinter

        # Utilizamos filedialog para mostrar la ventana de selección de archivos
        selectedImage = filedialog.askopenfilename(
            title="Selecciona un archivo de imagen",
            filetypes=[("Image files", ("*.jpg", "*.png"))]
        )

        if selectedImage:
            imagesFolder = "priv/photos"
            imageName = os.path.basename(selectedImage)
            destinePath = os.path.join(imagesFolder, imageName)
            shutil.copy(selectedImage, destinePath)

        return os.path.basename(selectedImage)
