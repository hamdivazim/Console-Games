"""
Console Games
"""

import games as console_games

if __name__ == "__main__":
    import animations
    import fancy_text

    game = console_games.Game()

    game.figure.animate_offset(x=7, y=7)

    game.refresh()

    game.figure.animate(animations.FigureAnimations.run(), loops=2, loop_offset_x=1)

    game.figure.reset()
    game.refresh()

    game.delay(1)

    title = fancy_text.Text(text="Cool title!")
    game.figure.offset(y=-6)

    game.add_to_children(title)

    game.refresh()

    game.delay(1)

    game.figure.animate(animations.FigureAnimations.run_left(), loops=2, loop_offset_x=-1)