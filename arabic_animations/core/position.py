from enum import Enum
from dataclasses import dataclass

class Position(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"

@dataclass
class Padding:
    top: float = 0
    right: float = 0
    bottom: float = 0
    left: float = 0

    @classmethod
    def all(cls, value: float):
        return cls(value, value, value, value)

    @classmethod
    def horizontal(cls, value: float):
        return cls(0, value, 0, value)

    @classmethod
    def vertical(cls, value: float):
        return cls(value, 0, value, 0)

def calculate_position(text_width: float, text_height: float,
                      scene_width: float, scene_height: float,
                      position: Position, padding: Padding = None) -> tuple[float, float]:
    """
    Calculate the x, y coordinates for text placement based on position and padding
    """
    if padding is None:
        padding = Padding()

    # Calculate available space
    available_width = scene_width - padding.left - padding.right
    available_height = scene_height - padding.top - padding.bottom

    # Calculate base positions
    positions = {
        Position.TOP: (scene_width/2 - text_width/2, padding.top),
        Position.BOTTOM: (scene_width/2 - text_width/2, scene_height - text_height - padding.bottom),
        Position.LEFT: (padding.left, scene_height/2 - text_height/2),
        Position.RIGHT: (scene_width - text_width - padding.right, scene_height/2 - text_height/2),
        Position.CENTER: (scene_width/2 - text_width/2, scene_height/2 - text_height/2),
        Position.TOP_LEFT: (padding.left, padding.top),
        Position.TOP_RIGHT: (scene_width - text_width - padding.right, padding.top),
        Position.BOTTOM_LEFT: (padding.left, scene_height - text_height - padding.bottom),
        Position.BOTTOM_RIGHT: (scene_width - text_width - padding.right,
                              scene_height - text_height - padding.bottom)
    }

    return positions[position]