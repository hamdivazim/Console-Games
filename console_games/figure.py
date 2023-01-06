import _object
from time import sleep as wait

class Figure(_object.Object):
    def animate(self, animation, loops=1):
        for i in range(loops):
            for ani in animation:
                self.current_sprite = ani
                self.refresh()
                wait(5/self.refresh_rate)
        