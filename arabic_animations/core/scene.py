import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
import numpy as np

class Scene:
    def __init__(self, width=1920, height=1080, fps=60):
        self.width = width
        self.height = height
        self.fps = fps
        self.duration = 0
        self.objects = []

    def add(self, *objects):
        """Add objects to the scene"""
        for obj in objects:
            self.objects.append(obj)
            if hasattr(obj, 'duration'):
                self.duration = max(self.duration, obj.duration)

    def render_frame(self, t):
        """Render a single frame at time t"""
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(surface)

        # Clear background
        ctx.set_source_rgb(1, 1, 1)
        ctx.paint()

        # Render all objects
        for obj in self.objects:
            if hasattr(obj, 'render'):
                obj.render(ctx, t)

        # Convert to numpy array
        data = surface.get_data()
        arr = np.ndarray(shape=(self.height, self.width, 4),
                        dtype=np.uint8,
                        buffer=data)
        return arr