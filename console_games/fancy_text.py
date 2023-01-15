""" Fancy text objects using `pyfiglet`"""

from pyfiglet import figlet_format
from colorama import Fore

from _object import Object
import _exceptions

def get_fancy_text(text, font="big"):
    """ Uses `pyfiglet` to return fancy text. """

    if len([i for i in supported_fonts if supported_fonts[i] == font]) == 0:
        raise _exceptions.FontNotSupported(f"Sorry, but the {font} font is not supported by console_games. Suggest adding it via GitHub Issues: https://github.com/hamdivazim/Console-Games/issues/new?template=add-font-request.md")
    else:
        if font == "simple":
            return text
        else:
            return figlet_format(text, font=font)

class Text(Object):
    """ Object for use in games.Game() """

    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30, text=None, font="big"):
        if text == None:
            raise _exceptions.NoCurrentTextProvided()
        else:
            super().__init__(color=color, refresh_rate=refresh_rate, current_sprite=get_fancy_text(text=text, font=supported_fonts[font]))
            self.text = text

            self._orig_font = font

    def change_text(self, new_text="", font=None):
        """ Changes text and/or font"""

        if new_text != "":
            self.text = new_text

        if font == None:
            font = self._orig_font
        elif font != self._orig_font:
            self._orig_font = font

        self.current_sprite = get_fancy_text(self.text, font=supported_fonts[font])
        self.current_game.refresh()

def get_supported_fonts():
    return supported_fonts.keys()

# Supported fonts - fonts currently supported by console_games and their pyfiglet names
supported_fonts = {
    "big":"big",
    "simple":"simple",
    "block":"block",
    "slant":"slant",
    "shadow":"shadow",
    "light":"script",
    "block-slant":"lean",
}