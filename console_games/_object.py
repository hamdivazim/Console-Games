""" Baseclass Object """

from time import sleep as wait
from os import system as cmd
from multiprocessing import Process

import colorama
from colorama import Fore

import _exceptions

class Object:
    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30, current_sprite=None):
        """ Initialiser """

        colorama.init()

        if current_sprite == None:
            raise _exceptions.NoCurrentSpriteProvided()
        else:
            self._default = current_sprite

            self.current_sprite = self._default
            self.refresh_rate = refresh_rate
            self.color = color

            self.offsetX = 0
            self.offsetY = 0

    def color(self, color):
        """ Changes the color of the object using colorama. """

        self.color = color

    def refresh(self):
        """ Refreshes the screen. """

        cmd("cls")

        sprite = "\n"*self.offsetY

        for line in self.current_sprite.splitlines(True):
            sprite += "  "*self.offsetX
            sprite += line

        print(f"{self.color}{sprite}")

    def reset(self):
        """ Resets the object. """

        self.current_sprite = self._default

    def delay(self, seconds):
        """ Delays the game. """

        for i in range(self.refresh_rate*seconds):
            self.refresh()
            wait(1/self.refresh_rate)

    def offset(self, x=None, y=None):
        if x != None:
            self.offsetX = x
        if y != None:
            self.offsetY = y
        
        self.refresh()

    def animate_offset(self, x=None, y=None):
        if x == None:
            x = 0
        if y == None:
            y = 0

        def animate_x():
            for i in range(abs(x)):
                if x >= 0:
                    self.offsetX += 1
                else:
                    self.offsetX -= 1
                self.refresh()
                wait(5/self.refresh_rate)
            

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
                self.refresh()
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
                self.refresh()
                wait(5/self.refresh_rate)
            for i in range(abs(x)-abs(y)):
                if x >= 0:
                    self.offsetX += 1
                else:
                    self.offsetX -= 1
                self.refresh()
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
                self.refresh()
                wait(5/self.refresh_rate)
            for i in range(abs(y)-abs(x)):
                if y >= 0:
                    self.offsetY += 1
                else:
                    self.offsetY -= 1
                self.refresh()
                wait(5/self.refresh_rate)
        
        self.refresh()