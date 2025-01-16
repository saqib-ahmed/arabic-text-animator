import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
import math
import traceback
import logging

logger = logging.getLogger('arabic_animations')

class Text:
    def __init__(self, text, position=(0, 0), font_name="DecoType Thuluth",
                 font_size=72, color=(0, 0, 0), stroke_width=2.0,
                 write_duration=1.0):
        self.text = text
        self.position = position
        self.font_name = font_name
        self.font_size = font_size
        self.color = color
        self.stroke_width = stroke_width
        self.duration = write_duration
        self._init_path()

    def _init_path(self):
        """Initialize the text path"""
        try:
            logger.debug(f"Initializing text: {self.text}")
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
            ctx = cairo.Context(surface)

            logger.debug("Creating Pango layout...")
            layout = PangoCairo.create_layout(ctx)
            font_desc = Pango.FontDescription(f"{self.font_name} {self.font_size}")
            logger.debug(f"Using font: {self.font_name}")
            layout.set_font_description(font_desc)
            layout.set_text(self.text, -1)
            layout.set_alignment(Pango.Alignment.RIGHT)
            layout.set_auto_dir(True)

            # Get text extents to verify layout
            ink_rect, logical_rect = layout.get_pixel_extents()
            logger.debug(f"Text extents - ink: {ink_rect}, logical: {logical_rect}")

            if logical_rect.width == 0 or logical_rect.height == 0:
                raise ValueError("Text layout has zero size - font might not be available")

            ctx.move_to(*self.position)
            PangoCairo.layout_path(ctx, layout)
            path = ctx.copy_path_flat()

            # Group into strokes
            self.strokes = self._group_strokes(path)
            logger.debug(f"Created {len(self.strokes)} strokes")
            self.stroke_lengths = self._calculate_lengths()
            self.total_length = sum(self.stroke_lengths)

        except Exception as e:
            logger.error(f"Error initializing text: {e}")
            logger.error(traceback.format_exc())
            raise

    def _group_strokes(self, path):
        """Group path elements into continuous strokes"""
        path_elements = list(path)
        strokes = []
        current_stroke = []

        for i in range(len(path_elements)):
            elem = path_elements[i]
            if elem[0] == cairo.PATH_MOVE_TO:
                if current_stroke:
                    strokes.append(current_stroke)
                current_stroke = [elem]
            else:
                current_stroke.append(elem)
        if current_stroke:
            strokes.append(current_stroke)

        # Sort strokes from right to left
        strokes.sort(key=lambda s: -s[0][1][0])  # Sort by x-coordinate in reverse
        return strokes

    def _calculate_lengths(self):
        """Calculate the length of each stroke"""
        lengths = []
        for stroke in self.strokes:
            length = 0
            for i in range(1, len(stroke)):
                if stroke[i][0] == cairo.PATH_LINE_TO:
                    x1, y1 = stroke[i-1][1]
                    x2, y2 = stroke[i][1]
                    length += math.sqrt((x2-x1)**2 + (y2-y1)**2)
            lengths.append(length)
        return lengths

    def render(self, ctx, t):
        """Render the text at time t"""
        if t > self.duration:
            t = self.duration

        progress = t / self.duration
        target_length = progress * self.total_length
        current_length = 0

        ctx.set_source_rgb(*self.color)
        ctx.set_line_width(self.stroke_width)

        for stroke_idx, stroke in enumerate(self.strokes):
            if current_length >= target_length:
                break

            ctx.new_path()
            ctx.move_to(*stroke[0][1])

            stroke_length = self.stroke_lengths[stroke_idx]

            for i in range(1, len(stroke)):
                if stroke[i][0] == cairo.PATH_LINE_TO:
                    x1, y1 = stroke[i-1][1]
                    x2, y2 = stroke[i][1]
                    segment_length = math.sqrt((x2-x1)**2 + (y2-y1)**2)

                    if current_length + segment_length <= target_length:
                        ctx.line_to(x2, y2)
                        current_length += segment_length
                    else:
                        remaining = target_length - current_length
                        t = remaining / segment_length
                        new_x = x1 + (x2 - x1) * t
                        new_y = y1 + (y2 - y1) * t
                        ctx.line_to(new_x, new_y)
                        break

            ctx.stroke()

    @staticmethod
    def list_available_fonts():
        """List all available Pango fonts"""
        try:
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
            ctx = cairo.Context(surface)
            layout = PangoCairo.create_layout(ctx)

            # Get font map
            font_map = PangoCairo.font_map_get_default()
            families = font_map.list_families()

            print("Available fonts:")
            for family in families:
                print(f"- {family.get_name()}")
        except Exception as e:
            print(f"Error listing fonts: {e}")
            print(traceback.format_exc())