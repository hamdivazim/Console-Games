import _object
from time import sleep as wait

class Figure(_object.Object):
    """ Premade object for a figure. """

    def animate(self, animation, loops=1, loop_offset_x=0, loop_offset_y=0):
        """ Animates the figure using an instance of animations.CustomAnimation() """

        for _ in range(loops):
            for ani in animation.animation:
                self.current_sprite = ani
                self.current_game.refresh()
                wait(5/self.refresh_rate)
                self.offsetX += loop_offset_x
                self.offsetY += loop_offset_y
        