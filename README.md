# Console-Games
Welcome to ConsoleGames, a simple Python module to make great console games!

## How does it work?

First, you need to initialise an instance of `Game`:
```
import console_games

game = console_games.Game()
```

`Game` has a premade instance of `Figure`, an object that can be displayed on the screen. You can make a figure that waves like this:
```
import console_games
from console_games.animations import FigureAnimations

game = console_games.Game(FigureAnimations.wave(), loops=n) # You can also loop the animation n times

game.figure.animate()
```

The `Object` class (from which `Figure` inherits) has these functions:
```
game.figure.reset() # Resets the object to its original sprite

game.figure.refresh() # Redraws the object (TODO: fix this function)

game.figure.delay(n) # Pauses the game for n seconds

game.figure.offset(x=3, y=3) # Offsets the object

game.figure.animate_offset(x=3, y=3) # Animates the offset

game.figure.color(Fore.BLUE) # Colors the object in the specified color using colorama
```
