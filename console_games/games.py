""" Baseclass Game """

from os import system as cmd
from time import sleep as wait

import colorama
from colorama import Fore

import keyboard

colorama.init()

class Game:
    def __init__(self):
        global current_game

        self.refresh_rate = 30

        self.children = []

        self._colors = [Fore.LIGHTRED_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]

        self._key_frame = 10
    
    def change_refresh_rate(self, new_rate):
        """ Changes the game's refresh rate. """

        self.refresh_rate = new_rate
        for child in self.children:
            child.refresh_rate = new_rate

    def add_to_children(self, object):
        """ Adds the given object to the game's children. """

        self.children.append(object)
        object.current_game = self

    def __add__(self, object):
        """ Adds the given object to the game's children. """

        self.children.append(object)
        object.current_game = self

    def refresh(self):
        """ Refreshes the screen. """

        cmd("cls")

        sortedChildren = sorted(self.children, key=lambda x: x.offsetY, reverse=False)

        offsetIndexY = 0

        self._key_frame += 1

        for child in sortedChildren:
            sprite = "\n"*(child.offsetY-offsetIndexY)

            if child._is_selector:
                if keyboard.is_pressed("right") and self._key_frame > 10:
                    child._selector_index += 1
                    child._update_selector(child._selector_index)
                    self._key_frame = 0
                if keyboard.is_pressed("left") and self._key_frame > 10:
                    child._selector_index -= 1
                    child._update_selector(child._selector_index)
                    self._key_frame = 0

            for line in child.current_sprite.splitlines(True):
                sprite += "  "*child.offsetX
                sprite += line

            if child.multicolor_enabled:
                print(f"{self._colors[child._current_color % len(self._colors)]}{sprite}")
                child._current_color += 1
            else:
                if child._is_selector:
                    print(f"{sprite}")
                else:
                    print(f"{child.color}{sprite}")

            offsetIndexY += 1

    def tick(self):
        """ Updates the game. """

        self.refresh()
        wait(1/self.refresh_rate)

    def delay(self, seconds):
        """ Delays the game. """

        for i in range(self.refresh_rate*seconds):
            self.tick()

    def wait_for_keypress(self, key="space"):
        """ Delays until the given key is pressed. """

        while not keyboard.is_pressed(key):
            self.tick()

    def _remove(self, obj):
        """ Removes the given object from the game. """

        self.children.remove(obj)
        self.refresh()

    def clear_screen(self):
        """ Removes all child objects from the screen. """

        for child in self.children:
            self._remove(child)