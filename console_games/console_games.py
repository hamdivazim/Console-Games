import figure


class Game:
    def __init__(self):
        self.figure = figure.Figure(refresh_rate=30)
        self.refresh_rate = 30
    
    def refresh_rate(self, new_rate):
        self.refresh_rate = new_rate
        self.figure.refresh_rate = new_rate