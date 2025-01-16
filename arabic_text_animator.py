import cairo
import gi
gi.require_version('Pango', '1.0')
gi.require_version('PangoCairo', '1.0')
from gi.repository import Pango, PangoCairo
import math
import numpy as np
import cv2

class ArabicTextAnimator:
    def __init__(self, width=1920, height=1080, fps=60):
        self.width = width
        self.height = height
        self.fps = fps

    def create_animation(self, text, font_name, font_size=128, duration=3,
                        color=(0, 0, 0), stroke_width=2.0):
        """
        Creates an animation of Arabic text being written

        Args:
            text: Arabic text to animate
            font_name: Name of the font to use
            font_size: Font size in points
            duration: Duration of animation in seconds
            color: RGB tuple for text color (0-1 range)
            stroke_width: Width of the stroke

        Returns:
            List of numpy arrays representing frames
        """
        # Calculate number of frames
        n_frames = int(duration * self.fps)
        frames = []

        # Create surface and context
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(surface)

        # Setup Pango layout
        layout = PangoCairo.create_layout(ctx)
        font_desc = Pango.FontDescription(f"{font_name} {font_size}")
        layout.set_font_description(font_desc)

        # Set text and get its logical extents
        layout.set_text(text, -1)
        layout.set_alignment(Pango.Alignment.RIGHT)  # RTL alignment
        layout.set_auto_dir(True)
        ink_rect, logical_rect = layout.get_pixel_extents()

        # Center the text
        text_x = (self.width - logical_rect.width) / 2
        text_y = (self.height - logical_rect.height) / 2

        # Get the path of the text
        ctx.move_to(text_x, text_y)
        PangoCairo.layout_path(ctx, layout)
        path = ctx.copy_path_flat()
        path_elements = list(path)

        # Group path elements by continuous strokes
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

        # Calculate total length of all strokes
        total_length = 0
        stroke_lengths = []

        for stroke in strokes:
            stroke_length = 0
            for i in range(1, len(stroke)):
                if stroke[i][0] == cairo.PATH_LINE_TO:
                    x1, y1 = stroke[i-1][1]
                    x2, y2 = stroke[i][1]
                    stroke_length += math.sqrt((x2-x1)**2 + (y2-y1)**2)
            stroke_lengths.append(stroke_length)
            total_length += stroke_length

        # Sort strokes from right to left based on their starting x-coordinate
        strokes_with_index = [(i, s) for i, s in enumerate(strokes)]
        strokes_with_index.sort(key=lambda x: -x[1][0][1][0])  # Sort by x-coordinate in reverse
        stroke_order = [i for i, _ in strokes_with_index]

        # Create frames
        for frame in range(n_frames):
            # Clear surface
            ctx.save()
            ctx.set_source_rgb(1, 1, 1)
            ctx.paint()
            ctx.restore()

            # Set drawing style
            ctx.set_source_rgb(*color)
            ctx.set_line_width(stroke_width)

            progress = frame / (n_frames - 1)
            target_length = progress * total_length
            current_length = 0

            ctx.new_path()

            # Draw strokes in right-to-left order
            for stroke_idx in stroke_order:
                stroke = strokes[stroke_idx]
                stroke_length = stroke_lengths[stroke_idx]

                if current_length >= target_length:
                    break

                ctx.move_to(*stroke[0][1])

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
                ctx.new_path()

            # Convert to numpy array and append to frames
            data = surface.get_data()
            arr = np.ndarray(shape=(self.height, self.width, 4),
                           dtype=np.uint8,
                           buffer=data)
            frame_bgr = cv2.cvtColor(arr, cv2.COLOR_BGRA2BGR)
            frames.append(frame_bgr)

        return frames

    def save_video(self, frames, output_path):
        """Saves frames as MP4 video"""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, self.fps,
                            (self.width, self.height))

        for frame in frames:
            out.write(frame)

        out.release()
