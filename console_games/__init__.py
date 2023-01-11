"""
Console Games
"""

import games as console_games
import os

def test():
    """ You can run this if you want to test console_games. """

    import animations
    import fancy_text
    import sound
    import figure

    game = console_games.Game()

    audio = sound.AudioPlayer()

    audio.play('test.mp3')

    game.delay(2)

    title = fancy_text.Text(text="Super Mario Bros.")

    game.add_to_children(title)

    title.offset(x=1, y=1)
    title.toggle_multicolor()

    game.delay(2)

    figure_sprite = R"""
 O
/|\
 |
/ \ 
    """

    figure = figure.Figure(current_sprite=figure_sprite)

    game.add_to_children(figure)

    figure.offset(y=4)

    figure.animate(animation=animations.FigureAnimations.run(), loop_offset_x=1)

    figure.current_sprite = figure_sprite

    game.delay(1)

    figure.animate(animation=animations.FigureAnimations.wave(), loops=2)

    figure.current_sprite = figure_sprite

    game.delay(3)

if __name__ == "__main__":
    test()