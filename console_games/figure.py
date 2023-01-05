from time import sleep as wait
from os import system as cmd

import colorama
from colorama import Fore

class Figure:
    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30):
        self._default = R"""
 O
/|\
 |
/ \ """

        self.current_sprite = self._default
        self.refresh_rate = refresh_rate
        self.color = color

    def color(self, color):
        self.color = color

    def refresh(self):
        cmd("cls")
        print(f"{self.color}{self.current_sprite}")

    def reset(self):
        self.current_sprite = self._default

    def animate(self, animation, loops=1):
        for i in range(loops):
            for ani in animation:
                for i in range(5):
                    self.current_sprite = ani
                    self.refresh()
                    wait(1/self.refresh_rate)

    def delay(self, seconds):
        for i in range(self.refresh_rate*seconds):
            self.refresh()
            wait(1/self.refresh_rate)
        