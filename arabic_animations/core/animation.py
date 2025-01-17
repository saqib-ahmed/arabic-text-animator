from enum import Enum

class Animation(Enum):
    INSTANT = "instant"
    WRITE = "write"
    TYPEWRITER = "typewriter"
    REVEAL = "reveal"

class Transition(Enum):
    NONE = "none"
    FADE_IN = "fade_in"
    FADE_OUT = "fade_out"
    SLIDE_IN = "slide_in"
    SLIDE_OUT = "slide_out"
    SCALE_IN = "scale_in"
    SCALE_OUT = "scale_out"