import figure
import fancy_text

from os import system as cmd
from time import sleep as wait

class Game:
    def __init__(self):
        global current_game

        self.figure = figure.Figure(refresh_rate=30, current_sprite=R"""
 O
/|\
 |
/ \ """)
        self.refresh_rate = 30

        self.children = []

        self.add_to_children(self.figure)
    
    def refresh_rate(self, new_rate):
        self.refresh_rate = new_rate
        for child in self.children:
            child.refresh_rate = new_rate

    def add_to_children(self, object):
        self.children.append(object)
        object.current_game = self

    def __add__(self, object):
        self.children.append(object)
        object.current_game = self

    def refresh(self):
        """ Refreshes the screen. """

        cmd("cls")

        sortedChildren = sorted(self.children, key=lambda x: x.offsetY, reverse=False)

        offsetIndexY = 0

        for child in sortedChildren:
            sprite = "\n"*(child.offsetY-offsetIndexY)

            for line in child.current_sprite.splitlines(True):
                sprite += "  "*child.offsetX
                sprite += line

            print(f"{child.color}{sprite}")

            offsetIndexY += 1

    def delay(self, seconds):
        """ Delays the game. """

        for i in range(self.refresh_rate*seconds):
            self.refresh()
            wait(1/self.refresh_rate)

current_game = Game()