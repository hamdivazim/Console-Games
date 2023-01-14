""" Selector Object """
import _exceptions
import _object

import colorama
from colorama import Fore

colorama.init()

class Selector:
    """Base selector object. """

    def __init__(self, options=(), current_game=None, highlight_color=Fore.BLUE):
        if options == ():
            raise _exceptions.SelectorsCannotBeEmpty()
        else:
            if current_game == None:
                raise _exceptions.NoSceneProvided()
            else:
                self.options = options

                self.current_game = current_game

                self._ofsY = 0
                self._ofsX = 0

                string = ""

                for option in self.options:
                    string += "          "
                    string += option

                self._object = _object.Object(refresh_rate=current_game.refresh_rate, current_game=current_game, current_sprite=string, _selector_options=self.options)

                self._object._select_highlight = highlight_color

                self._object._is_selector = True

                self._object._update_selector(0)

                current_game.add_to_children(self._object)

                self._selected = 0

    def offset(self, x=0, y=0):
        if x != 0:
            self._ofsX = x
        if y != 0:
            self._ofsY = y

        self._object.offset(x=x, y=y)
        
        self.current_game.refresh()

    def remove(self):
        self.current_game._remove(self._object)

    def get_current_option(self):
        return self.options[self._object._selector_index % len(self.options)]
