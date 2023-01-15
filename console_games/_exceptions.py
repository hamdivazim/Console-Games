""" Exceptions """

class NoCurrentSpriteProvided(Exception): # If a default sprite is provided in _object.Object()
    pass

class NoCurrentTextProvided(Exception): # If default text is not found in fancy_text.Text()
    pass

class NoSceneProvided(Exception): # If the current game is not found for any reason in _object.Object()
    pass

class SelectorsCannotBeEmpty(Exception): # If no options are given in selector.Selector()
    pass

class FontNotSupported(Exception): # If the font is not supported in fancy_text.Text()
    pass

class NoAnimationProvided(Exception): # If an animation isn't given in animations.CustomAnimation()
    pass