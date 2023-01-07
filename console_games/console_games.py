import figure
import fancy_text


class Game:
    def __init__(self):
        self._scene = """"""

        _game_object = self

        self.figure = figure.Figure(refresh_rate=30, current_sprite=R"""
 O
/|\
 |
/ \ """, current_game=_game_object)
        self.refresh_rate = 30
    
    def refresh_rate(self, new_rate):
        self.refresh_rate = new_rate
        self.figure.refresh_rate = new_rate

    def write(self, data):
        print(fancy_text.get_fancy_text(data))