import cairo
import gi
from typing import List, Any, Optional
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
import numpy as np
from .color import Colors, Color

class Scene:
    """
    A scene represents a complete animation with one or more text objects.

    Args:
        width: Width of the scene in pixels
        height: Height of the scene in pixels
        fps: Frames per second for the animation
    """
    def __init__(self, width: int = 1920, height: int = 1080, fps: int = 60):
        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0
        self.objects: List[Any] = []
        self.serial = False
        self.background_color: Color = Colors.PAPER_WHITE

    def add(self, *objects: Any, serial: bool = False) -> None:
        """
        Add objects to the scene.

        Args:
            *objects: One or more objects to add to the scene
            serial: If True, objects will animate one after another. If False, they animate simultaneously.
        """
        self.serial = serial
        current_delay = 0

        for obj in objects:
            if hasattr(obj, 'set_scene_dimensions'):
                obj.set_scene_dimensions(self.width, self.height)

            if serial:
                obj.start_time = current_delay
                current_delay += obj.duration
            else:
                obj.start_time = 0

            self.objects.append(obj)

        self.duration = current_delay if serial else max(obj.duration for obj in objects)

    def render_frame(self, t: float) -> np.ndarray:
        """
        Render a single frame at time t.

        Args:
            t: Time in seconds

        Returns:
            A numpy array representing the frame in RGBA format
        """
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(surface)

        # Clear background with specified color
        ctx.set_source_rgba(*self.background_color.to_rgb())
        ctx.paint()

        # Render all objects
        for obj in self.objects:
            if hasattr(obj, 'render'):
                if t >= obj.start_time and t <= obj.start_time + obj.duration:
                    obj.render(ctx, t - obj.start_time)
                elif t > obj.start_time + obj.duration:
                    obj.render(ctx, obj.duration)

        # Convert to numpy array
        data = surface.get_data()
        arr = np.ndarray(shape=(self.height, self.width, 4),
                        dtype=np.uint8,
                        buffer=data)
        return arr