""" Fancy text objects using `pyfiglet`"""

from pyfiglet import figlet_format
from colorama import Fore

from _object import Object
import _exceptions

def get_fancy_text(text, font="big"):
    if not font in supported_fonts.keys():
        raise _exceptions.FontNotSupported(f"Sorry, but the {font} font is not supported by console_games. Suggest adding it via GitHub Issues: https://github.com/hamdivazim/Console-Games/issues/new?template=add-font-request.md")
    else:
        return figlet_format(text, font=font)

class Text(Object):
    def __init__(self, color=Fore.LIGHTBLACK_EX, refresh_rate=30, text=None, font="big"):
        if text == None:
            raise _exceptions.NoCurrentTextProvided()
        else:
            super().__init__(color=color, refresh_rate=refresh_rate, current_sprite=get_fancy_text(text=text, font=font))
            self.text = text

    def change_text(self, new_text, font="big"):
        self.text = new_text
        self.current_sprite = get_fancy_text(new_text, font=font)
        self.current_game.refresh()

# Supported fonts - fonts currently supported in console_games and their pyfiglet names
supported_fonts = {
    "big":"big",
    "block":"block",
    "slant":"smslant",
    "shadow":"shadow"
}