""" Baseclass Object """

from time import sleep as wait
from os import system as cmd
from multiprocessing import Process

import colorama
from colorama import Fore

import _exceptions

import platform

class Object:
    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30, current_sprite=None, current_game=None):
        """ Initialiser """

        colorama.init()

        if current_sprite == None:
            raise _exceptions.NoCurrentSpriteProvided()
        else:
            self._default = current_sprite

            self._scene = current_game

            self.current_sprite = self._default
            self.refresh_rate = refresh_rate
            self.color = color

            self.current_game = None

            self.offsetX = 0
            self.offsetY = 0

    def color(self, color):
        """ Changes the color of the object using colorama. """

        self.color = color

    def refresh(self):
        """ Refreshes the screen. """

        if platform.system() == "Windows":
            cmd("cls")
        else:
            cmd("clear")

        sprite = "\n"*self.offsetY

        for line in self.current_sprite.splitlines(True):
            sprite += "  "*self.offsetX
            sprite += line

        print(f"{self.color}{sprite}")

    def reset(self):
        """ Resets the object. """

        self.current_sprite = self._default

    def offset(self, x=None, y=None):
        if x != None:
            self.offsetX = x
        if y != None:
            self.offsetY = y
        
        self.current_game.refresh()

    def animate_offset(self, x=None, y=None):
        if x == None:
            x = 0
        if y == None:
            y = 0

        if abs(x) == abs(y):
            for i in range(abs(y)):
                if x >= 0:
                    self.offsetX += 1
                else:
                    self.offsetX -= 1
                if y >= 0:
                    self.offsetY += 1
                else:
                    self.offsetY -= 1
                self.current_game.refresh()
                wait(5/self.refresh_rate)

        if abs(x) > abs(y):
            for i in range(abs(y)):
                if x >= 0:
                    self.offsetX += 1
                else:
                    self.offsetX -= 1
                if y >= 0:
                    self.offsetY += 1
                else:
                    self.offsetY -= 1
                self.current_game.refresh()
                wait(5/self.refresh_rate)
            for i in range(abs(x)-abs(y)):
                if x >= 0:
                    self.offsetX += 1
                else:
                    self.offsetX -= 1
                self.current_game.refresh()
                wait(5/self.refresh_rate)

        if abs(y) > abs(x):
            for i in range(abs(x)):
                if x >= 0:
                    self.offsetX += 1
                else:
                    self.offsetX -= 1
                if y >= 0:
                    self.offsetY += 1
                else:
                    self.offsetY -= 1
                self.current_game.refresh()
                wait(5/self.refresh_rate)
            for i in range(abs(y)-abs(x)):
                if y >= 0:
                    self.offsetY += 1
                else:
                    self.offsetY -= 1
                self.current_game.refresh()
                wait(5/self.refresh_rate)
        
        self.current_game.refresh()