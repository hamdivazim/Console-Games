from pyfiglet import figlet_format
import colorama
from colorama import Fore

from _object import Object
import _exceptions

def get_fancy_text(text):
    return figlet_format(text, font='big')

class Text(Object):
    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30, text=None):
        if text == None:
            raise _exceptions.NoCurrentTextProvided()
        else:
            super().__init__(color=color, refresh_rate=refresh_rate, current_sprite=get_fancy_text(text=text))
            self.text = text

    def change_text(self, new_text):
        self.text = new_text
        self.current_sprite = get_fancy_text(new_text)
        self.refresh()
