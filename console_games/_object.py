""" Baseclass Object """

from time import sleep as wait

import colorama
from colorama import Fore

import _exceptions

class Object:
    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30, current_sprite=None, current_game=None, _selector_options=()):
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

            self.multicolor_enabled = False
            self._current_color = 0

            self._is_selector = False
            self._selector_index = 0
            self._selector_options = _selector_options
            self._select_highlight = Fore.BLUE

            if not current_game == None:
                self.current_game = current_game

            self.offsetX = 0
            self.offsetY = 0

    def remove(self):
        """ Removes the object from the game. """

        self.current_game._remove(self)

    def color(self, color):
        """ Changes the color of the object using colorama. """

        self.color = color

    def reset(self):
        """ Resets the object to the original sprite. """

        self.current_sprite = self._default

    def offset(self, x=None, y=None):
        """ Offsets the object by x and y. """

        if x != None:
            self.offsetX = x
        if y != None:
            self.offsetY = y
        
        self.current_game.refresh()

    def animate_offset(self, x=None, y=None):
        """ Animates the offset of the object by x and y. """

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

    def toggle_multicolor(self):
        """ Toggles multicolor in the object. """

        self.multicolor_enabled = not self.multicolor_enabled

    def _update_selector(self, index, perform_refresh=False):
        """ Updates the selector's sprite based the the current chosen option. """

        string = ""

        for i, option in enumerate(self._selector_options):
            string += "          "
            if i == (index % len(self._selector_options)):
                string += f"{self._select_highlight}{option}"
            else:
                string += f"{Fore.LIGHTBLACK_EX}{option}"

        self.current_sprite = string

        if perform_refresh:
            self.current_game.refresh()