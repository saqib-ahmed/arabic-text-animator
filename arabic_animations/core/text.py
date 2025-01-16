from typing import Tuple, Optional, List
import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
import math
import traceback
import logging
from .position import Position, Padding, calculate_position
from .color import Color, Colors, Style

logger = logging.getLogger('arabic_animations')

class Text:
    """
    A text object that can be animated.

    Args:
        text: The text to display
        position: Position enum value or tuple of coordinates
        padding: Padding object for spacing
        font_name: Name of the font to use
        font_size: Size of the font in points
        style: Style object for visual appearance
        write_duration: Duration of the writing animation in seconds
    """
    def __init__(self,
                 text: str,
                 position: Position = Position.CENTER,
                 padding: Optional[Padding] = None,
                 font_name: str = "DecoType Thuluth",
                 font_size: int = 72,
                 style: Optional[Style] = None,
                 write_duration: float = 1.0):
        self.text = text
        self.position_type = position if isinstance(position, Position) else Position.CENTER
        self.padding = padding if padding else Padding()
        self.font_name = font_name
        self.font_size = font_size
        self.style = style if style else Style()
        self.duration = write_duration
        self._position: Tuple[float, float] = (0, 0)
        self._init_path()

    def _init_path(self) -> None:
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

            # Get text extents to calculate position
            ink_rect, logical_rect = layout.get_pixel_extents()
            logger.debug(f"Text extents - ink: {ink_rect}, logical: {logical_rect}")

            if logical_rect.width == 0 or logical_rect.height == 0:
                raise ValueError("Text layout has zero size - font might not be available")

            # Store text dimensions for scene calculations
            self.width = logical_rect.width
            self.height = logical_rect.height

            # Position will be set by scene when adding the text
            self._layout = layout
            self._calculate_path()

        except Exception as e:
            logger.error(f"Error initializing text: {e}")
            logger.debug(traceback.format_exc())
            raise

    def _calculate_path(self) -> None:
        """Calculate the path based on current position"""
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
        ctx = cairo.Context(surface)

        ctx.move_to(*self._position)
        PangoCairo.layout_path(ctx, self._layout)
        path = ctx.copy_path_flat()

        self.strokes = self._group_strokes(path)
        logger.debug(f"Created {len(self.strokes)} strokes")
        self.stroke_lengths = self._calculate_lengths()
        self.total_length = sum(self.stroke_lengths)

    def _group_strokes(self, path: List[Tuple[int, Tuple[float, float]]]) -> List[List[Tuple[int, Tuple[float, float]]]]:
        """
        Group path elements into continuous strokes

        Args:
            path: List of path elements from cairo

        Returns:
            List of strokes, where each stroke is a list of path elements
        """
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

    def _calculate_lengths(self) -> List[float]:
        """
        Calculate the length of each stroke

        Returns:
            List of stroke lengths
        """
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

    def render(self, ctx: cairo.Context, t: float) -> None:
        """
        Render the text at time t

        Args:
            ctx: Cairo context to draw on
            t: Time in seconds
        """
        if t > self.duration:
            t = self.duration

        progress = t / self.duration
        target_length = progress * self.total_length

        # Apply shadow if specified
        if self.style.shadow_color:
            ctx.save()
            ctx.translate(*self.style.shadow_offset)
            self._render_strokes(ctx, target_length, self.style.shadow_color)
            ctx.restore()

        # Apply glow if specified
        if self.style.glow_color and self.style.glow_radius > 0:
            for i in range(3):
                ctx.save()
                ctx.set_line_width(self.style.stroke_width + self.style.glow_radius * (i+1)/3)
                glow_alpha = self.style.glow_color.a * (3-i)/3
                glow = self.style.glow_color.with_alpha(glow_alpha)
                self._render_strokes(ctx, target_length, glow)
                ctx.restore()

        # Render fill if specified
        if self.style.fill_color:
            ctx.save()
            self._render_strokes(ctx, target_length, self.style.fill_color, True)
            ctx.restore()

        # Render stroke
        ctx.set_line_width(self.style.stroke_width)
        self._render_strokes(ctx, target_length, self.style.stroke_color)

    def _render_strokes(self, ctx: cairo.Context, target_length: float, color: Color, fill: bool = False) -> None:
        """
        Helper method to render strokes

        Args:
            ctx: Cairo context to draw on
            target_length: Target length to draw up to
            color: Color to use for rendering
            fill: Whether to fill the path instead of stroking
        """
        current_length = 0

        # Handle gradient if specified
        if self.style.gradient and not fill:
            pat = cairo.LinearGradient(0, 0,
                                     *self.style.gradient_direction or (0, self.height))
            pat.add_color_stop_rgba(0, *self.style.gradient[0].to_rgb())
            pat.add_color_stop_rgba(1, *self.style.gradient[1].to_rgb())
            ctx.set_source(pat)
        else:
            ctx.set_source_rgba(*color.to_rgb())

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

    def set_scene_dimensions(self, width: int, height: int) -> None:
        """Update position based on scene dimensions"""
        self._position = calculate_position(
            self.width, self.height,
            width, height,
            self.position_type,
            self.padding
        )
        self._calculate_path()

    @staticmethod
    def list_available_fonts() -> None:
        """List all available Pango fonts to stdout"""
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