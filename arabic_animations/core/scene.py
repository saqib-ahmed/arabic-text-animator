import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
import numpy as np
from .color import Colors

class Scene:
    def __init__(self, width=1920, height=1080, fps=60):
        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0
        self.objects = []
        self.serial = False

    def add(self, *objects, serial=False):
        """
        Add objects to the scene

        Args:
            *objects: Objects to add
            serial: If True, objects will animate one after another
        """
        self.serial = serial
        current_delay = 0

        for obj in objects:
            # Set proper positioning for each object
            if hasattr(obj, 'set_scene_dimensions'):
                obj.set_scene_dimensions(self.width, self.height)

            if serial:
                obj.start_time = current_delay
                current_delay += obj.duration
            else:
                obj.start_time = 0

            self.objects.append(obj)

        self.duration = current_delay if serial else max(obj.duration for obj in objects)

    def render_frame(self, t):
        """Render a single frame at time t"""
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(surface)

        # Clear background with specified color
        bg_color = getattr(self, 'background_color', Colors.PAPER_WHITE)
        ctx.set_source_rgba(*bg_color.to_rgb())
        ctx.paint()

        # Render all objects
        for obj in self.objects:
            if hasattr(obj, 'render'):
                # Only render if within object's time window
                if t >= obj.start_time and t <= obj.start_time + obj.duration:
                    obj.render(ctx, t - obj.start_time)
                elif t > obj.start_time + obj.duration:
                    # Render final state for completed animations
                    obj.render(ctx, obj.duration)

        # Convert to numpy array
        data = surface.get_data()
        arr = np.ndarray(shape=(self.height, self.width, 4),
                        dtype=np.uint8,
                        buffer=data)
        return arr