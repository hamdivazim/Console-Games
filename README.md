# Console-Games
Welcome to ConsoleGames, a great Python module to make great console games!

## How does it work?

First, you need to initialise an instance of `Game`:
```
import console_games

game = console_games.Game()
```

`Game` is a container for all child objects. As of `0.03`, you can add `figure.Figure`, `fancy_text.Text()` and `selector.Selector()`

The `_object.Object` class (from which all of these inherit) has these functions:
```
game.figure.reset() # Resets the object to its original sprite

game.figure.offset(x=3, y=3) # Offsets the object

game.figure.animate_offset(x=3, y=3) # Animates the offset

game.figure.color(Fore.BLUE) # Colors the object in the specified color using colorama
```

To initialise an object:
```
figure = figure.Figure()

game.add_to_children(figure)
```

## `figure.Figure()`
`Figure` has the `animate` function, which takes the animation to be executed, amount of loops, and 2 parameters for offset during animation.
```
figure.animate(animation=animations.FigureAnimations.run(), loop_offset_x=1)
```

## `fancy_text.Text()`
`Text` generates a plain object but using fancy text characters using [`pyfiglet`](https://github.com/pwaller/pyfiglet).

```
title = fancy_text.Text(text="Super Mario Bros.")

game.add_to_children(title)

title.toggle_multicolor() # Toggles whether the object is multicoloured.
```

## `selector.Selector()`
`Selector` is **NOT** an object. It contains a private property `_object` that holds the actual object used in the game. You can, however use `offset()` and `remove()` normally. To get the current selected option, use `get_current_option()`.
```
selector = selector.Selector(("GAME 1 ( 100% )", "GAME 2", "GAME 3"), current_game=game)

selector.offset(y=4)
```

## When can I use it?

As of now, console_games is _very_ early into development. When it is the _very_ best I can make it, I will release it on PyPi :)


## License
console_games is under the [Apache-2.0 license](https://github.com/hamdivazim/Console-Games/blob/main/LICENSE).