""" Premade animations. """
import _exceptions

# Custom Animation Class
class CustomAnimation:
    def __init__(self, aniList=None):
        if aniList == None:
            raise _exceptions.NoAnimationProvided()
        else:
            self.animation = aniList

# Figure Animations

class FigureAnimations:
    @staticmethod
    def default_position():
        return R"""
 O
/|\
 |
/ \ 
    """

    @staticmethod
    def wave():
        return CustomAnimation(aniList=[
R"""
 O
/|\
 |
/ \
    """,
R"""
 O
/|-
 |
/ \
    """,
R"""
 O/
/|
 |
/ \
    """,
R"""
 O
/|-
 |
/ \
    """,
        ])

    @staticmethod
    def run():
        return  CustomAnimation(aniList=[
R"""
 O
 |<
 |
/ \
    """,
R"""
 O
 |<
 |
- \
    """,
R"""
 O
 |<
\|
  \
    """,
R"""
 O
 |<
\|
 |
    """,
R"""
 O
 |<
 |
 |
    """,
R"""
 O
 |<
 |/
 |
/ 
    """,
R"""
 O
 |<
 |
/ -
    """,
R"""
 O
 |<
 |
/ \
    """,
R"""
 O
 |<
 |
- \
    """,
R"""
 O
 |<
\|
  \
    """,
R"""
 O
 |<
\|
 |
    """,
R"""
 O
 |<
 |
 |
    """,
R"""
 O
 |<
 |/
 |
/ 
    """,
R"""
 O
 |<
 |
/ -
    """,
        ])

    @staticmethod
    def run_left():
        return  CustomAnimation(aniList=[
R"""
 O
>|
 |
/ \
    """,
R"""
 O
>|
 |
/ -
    """,
R"""
 O
>|
 |/
/  
    """,
R"""
 O
>|
 |/
 |
    """,
R"""
 O
>|
 |
 |
    """,
R"""
 O
>|
\|
  \
    """,
R"""
 O
>|
 |
- \
    """,
R"""
 O
>|
 |
/ \
    """,
        ])

    @staticmethod
    def jump():
        return CustomAnimation(aniList=[
R"""
 O
/|\
 |
/ \
""",
R"""
 O
-|-
_|_
 
""",
R"""
\O/
 |
\|/
 
""",
R"""
 O
-|-
_|_
 
""",
        ])