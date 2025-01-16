# Quick Start

## Basic Usage

Create a new Python script (e.g., `my_animation.py`):

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

## Command Line Interface

The library provides a command-line tool `arabic-animate` with the following commands:

```bash
# Live preview during development
arabic-animate render my_animation.py --preview

# Enable verbose output for debugging
arabic-animate render my_animation.py --preview -v

# Render to video file
arabic-animate render my_animation.py --output video.mp4
```

## Preview Controls

When using the preview window:
- Space: Play/Pause
- R: Reset to beginning
- Q: Quit preview