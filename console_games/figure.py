import _object
from time import sleep as wait

class Figure(_object.Object):
    def animate(self, animation, loops=1, loop_offset_x=0, loop_offset_y=0):
        for i in range(loops):
            for ani in animation.animation:
                self.current_sprite = ani
                self.current_game.refresh()
                wait(5/self.refresh_rate)
                self.offsetX += loop_offset_x
                self.offsetY += loop_offset_y
        