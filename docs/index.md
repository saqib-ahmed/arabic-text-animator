# Arabic Animations

A Python library for creating Arabic text writing animations, similar to Manim but specialized for Arabic calligraphy and text animations.

## Features

- Create smooth writing animations for Arabic text
- Support for RTL text rendering
- Live preview during development
- Export to MP4 video files
- Customizable text properties (font, size, color, stroke width)
- Multiple text elements with different timings
- Command-line interface with preview and render options

## Quick Example

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding
from arabic_animations.core.color import Color, Colors, Style

# Create scene
scene = Scene(width=1920, height=1080)

# Create text with styling
text = Text(
    "بسم الله الرحمن الرحيم",
    position=Position.TOP,
    padding=Padding(top=50),
    style=Style(
        stroke_color=Color.from_hex("#B8860B"),
        fill_color=Color.from_hex("#FFD700"),
        stroke_width=3.0
    ),
    write_duration=2.0
)

scene.add(text)
```