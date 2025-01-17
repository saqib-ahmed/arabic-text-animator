from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding
from arabic_animations.core.color import Color, Colors, Style

# Create scene
scene = Scene(width=1920, height=1080)
scene.background_color = Colors.PAPER_SEPIA  # Set sepia background

# Create styled text
title_style = Style(
    stroke_color=Color.from_hex("#000000"),  # Dark golden color
    fill_color=Color.from_hex("#FFD700"),    # Golden fill
    stroke_width=3.0,
    # shadow_color=Color.from_hex("#00000066"),  # Semi-transparent black
    shadow_offset=(5, 5),
    shadow_blur=2.0
)

subtitle_style = Style(
    stroke_color=Colors.PRIMARY,
    gradient=(Colors.PRIMARY, Colors.SECONDARY),
    gradient_direction=(0, 50),  # Vertical gradient over 50 pixels
    stroke_width=2.0,
    glow_color=Color.from_hex("#FFFFFF99"),
    glow_radius=3.0
)

text1 = Text(
    "بسم الله الرحمن الرحيم",
    position=Position.TOP,
    padding=Padding(top=50),
    font_name="DecoType Thuluth II",
    font_size=128,
    style=title_style,
    write_duration=10.0
)

text2 = Text(
    "السلام عليكم",
    position=Position.CENTER,
    font_name="DecoType Thuluth II",
    font_size=72,
    style=subtitle_style,
    write_duration=1.5
)

scene.add(text1, text2, serial=True)