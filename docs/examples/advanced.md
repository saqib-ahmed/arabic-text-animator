# Advanced Examples

## Complex Styling

Example showing advanced text styling with gradients, shadows, and glow effects:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding
from arabic_animations.core.color import Color, Colors, Style

# Create scene with sepia background
scene = Scene(width=1920, height=1080)
scene.background_color = Colors.PAPER_SEPIA

# Create golden title with shadow
title_style = Style(
    stroke_color=Color.from_hex("#B8860B"),  # Dark golden color
    fill_color=Color.from_hex("#FFD700"),    # Golden fill
    stroke_width=3.0,
    shadow_color=Color.from_hex("#00000066"),  # Semi-transparent black
    shadow_offset=(5, 5),
    shadow_blur=2.0
)

# Create subtitle with gradient and glow
subtitle_style = Style(
    stroke_color=Colors.PRIMARY,
    gradient=(Colors.PRIMARY, Colors.SECONDARY),
    gradient_direction=(0, 50),  # Vertical gradient over 50 pixels
    stroke_width=2.0,
    glow_color=Color.from_hex("#FFFFFF99"),
    glow_radius=3.0
)

# Create text objects
title = Text(
    "بسم الله الرحمن الرحيم",
    position=Position.TOP,
    padding=Padding(top=50),
    font_name="DecoType Thuluth II",
    font_size=128,
    style=title_style,
    write_duration=2.0
)

subtitle = Text(
    "السلام عليكم",
    position=Position.CENTER,
    font_name="DecoType Thuluth II",
    font_size=72,
    style=subtitle_style,
    write_duration=1.5
)

scene.add(title, subtitle, serial=True)
```

## Complex Layout

Example showing complex text positioning and timing:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding
from arabic_animations.core.color import Color, Colors, Style

# Create scene
scene = Scene(width=1920, height=1080)

# Create styles
header_style = Style(
    stroke_color=Colors.PRIMARY,
    fill_color=Colors.PRIMARY.with_alpha(0.3),
    stroke_width=2.0
)

body_style = Style(
    stroke_color=Colors.BLACK,
    stroke_width=1.5
)

footer_style = Style(
    stroke_color=Colors.SECONDARY,
    gradient=(Colors.SECONDARY, Colors.PRIMARY),
    gradient_direction=(0, 30)
)

# Create text objects with different positions
header = Text(
    "العنوان الرئيسي",
    position=Position.TOP,
    padding=Padding(top=50),
    style=header_style,
    font_size=96,
    write_duration=1.5
)

body1 = Text(
    "النص الأول",
    position=Position.TOP_LEFT,
    padding=Padding(top=200, left=100),
    style=body_style,
    font_size=48,
    write_duration=1.0
)

body2 = Text(
    "النص الثاني",
    position=Position.TOP_RIGHT,
    padding=Padding(top=200, right=100),
    style=body_style,
    font_size=48,
    write_duration=1.0
)

footer = Text(
    "النص الختامي",
    position=Position.BOTTOM,
    padding=Padding(bottom=50),
    style=footer_style,
    font_size=72,
    write_duration=1.2
)

# Add all elements with specific timing
scene.add(header, body1, body2, footer, serial=True)
```

## Animation Showcase

Example showing different animation timings and effects:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding
from arabic_animations.core.color import Color, Colors, Style

# Create scene
scene = Scene(width=1920, height=1080)

# Create texts with different durations and styles
texts = [
    Text(
        "بسم الله",
        position=Position.TOP,
        padding=Padding(top=50),
        style=Style(
            stroke_color=Colors.PRIMARY,
            glow_color=Colors.PRIMARY.with_alpha(0.6),
            glow_radius=3.0
        ),
        write_duration=1.0
    ),
    Text(
        "الرحمن",
        position=Position.CENTER,
        style=Style(
            stroke_color=Colors.SECONDARY,
            fill_color=Colors.SECONDARY.with_alpha(0.3)
        ),
        write_duration=0.8
    ),
    Text(
        "الرحيم",
        position=Position.BOTTOM,
        padding=Padding(bottom=50),
        style=Style(
            gradient=(Colors.PRIMARY, Colors.SECONDARY),
            gradient_direction=(0, 40)
        ),
        write_duration=1.2
    )
]

# Add all texts serially
scene.add(*texts, serial=True)
```