# Basic Examples

## Simple Text Animation

The most basic example showing a single animated text:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position

# Create scene
scene = Scene(width=1920, height=1080)

# Create and add text
text = Text(
    "بسم الله الرحمن الرحيم",
    position=Position.CENTER,
    font_name="DecoType Thuluth II",
    font_size=128,
    write_duration=2.0
)

scene.add(text)
```

## Multiple Text Elements

Example showing multiple text elements animating serially:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position, Padding

# Create scene
scene = Scene(width=1920, height=1080)

# Create text objects
title = Text(
    "بسم الله الرحمن الرحيم",
    position=Position.TOP,
    padding=Padding(top=50),
    font_size=128,
    write_duration=2.0
)

subtitle = Text(
    "السلام عليكم",
    position=Position.CENTER,
    font_size=72,
    write_duration=1.5
)

# Add texts serially (one after another)
scene.add(title, subtitle, serial=True)
```

## Basic Styling

Example showing basic text styling:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position
from arabic_animations.core.color import Style, Colors

# Create scene
scene = Scene(width=1920, height=1080)

# Create styled text
text = Text(
    "بسم الله",
    position=Position.CENTER,
    style=Style(
        stroke_color=Colors.BLACK,
        fill_color=Colors.BLUE,
        stroke_width=2.0
    ),
    write_duration=2.0
)

scene.add(text)
```

## Custom Background

Example showing how to set a custom background color:

```python
from arabic_animations.core.scene import Scene
from arabic_animations.core.text import Text
from arabic_animations.core.color import Colors

# Create scene with custom background
scene = Scene(width=1920, height=1080)
scene.background_color = Colors.PAPER_CREAM

# Create text
text = Text(
    "بسم الله",
    write_duration=2.0
)

scene.add(text)
```