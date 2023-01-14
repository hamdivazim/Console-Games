"""
Console Games
"""

import games
import os

__version__ = "0.03.1-alpha"

def test():
    """ You can run this if you want to test console_games. """

    import animations
    import fancy_text
    import sound
    import figure
    import selector

    game = games.Game()
    audio = sound.AudioPlayer()

    audio.play('test.mp3')

    game.delay(2)

    title = fancy_text.Text(text="Super Mario Bros.", font="shadow")
    game.add_to_children(title)

    title.offset(x=1, y=1)
    title.toggle_multicolor()

    game.delay(2)

    figure_sprite = animations.FigureAnimations.default_position()
    figure = figure.Figure(current_sprite=figure_sprite)
    game.add_to_children(figure)

    figure.offset(y=4)

    figure.animate(animation=animations.FigureAnimations.run(), loop_offset_x=1)

    figure.current_sprite = figure_sprite

    game.delay(1)

    figure.animate(animation=animations.FigureAnimations.wave(), loops=2)
    figure.current_sprite = figure_sprite

    game.delay(3)

    figure.remove()

    title.toggle_multicolor()

    selector = selector.Selector(("GAME 1 ( 100% )", "GAME 2", "GAME 3"), current_game=game)

    selector.offset(y=4)

    game.wait_for_keypress("enter")
    
    game.clear_screen()
    selector.remove()

    header = fancy_text.Text(text=selector.get_current_option())

    game.add_to_children(header)

    header.toggle_multicolor()

    game.delay(2)

if __name__ == "__main__":
    test()