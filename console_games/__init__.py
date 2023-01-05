"""
Console Games
"""

import console_games

if __name__ == "__main__":
    import animations

    game = console_games.Game()

    game.figure.refresh()

    game.figure.animate(animations.FigureAnimations.run(), loops=2)

    game.figure.reset()
    game.figure.refresh()

    game.figure.delay(1)