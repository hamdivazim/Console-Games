"""
Console Games
"""

import console_games

if __name__ == "__main__":
    import animations
    import fancy_text

    game = console_games.Game()

    game.figure.animate_offset(x=7, y=4)

    game.figure.refresh()

    game.figure.animate(animations.FigureAnimations.run(), loops=2)

    game.figure.reset()
    game.figure.refresh()

    game.figure.offset(x=-5, y=-2)

    game.figure.delay(1)

    title = fancy_text.Text(text="Cool title!")

    title.animate_offset(y=7)

    title.refresh()