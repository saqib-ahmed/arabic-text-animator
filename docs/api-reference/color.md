# Color

::: arabic_animations.core.color.Color
    handler: python
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

::: arabic_animations.core.color.Style
    handler: python
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

## Usage Examples

### Creating Colors
```python
from arabic_animations.core.color import Color, Colors

# From RGB (0-1)
red = Color.from_rgb(1.0, 0.0, 0.0)

# From RGB (0-255)
blue = Color.from_rgb255(0, 0, 255)

# From hex
gold = Color.from_hex("#FFD700")

# From HSL
green = Color.from_hsl(120, 1.0, 0.5)
```

### Using Predefined Colors
```python
# Basic colors
black = Colors.BLACK
white = Colors.WHITE

# UI colors
primary = Colors.PRIMARY
warning = Colors.WARNING

# Paper colors
background = Colors.PAPER_CREAM
```

### Creating Styles
```python
from arabic_animations.core.color import Style

# Basic style
style = Style(
    stroke_color=Colors.BLACK,
    fill_color=Colors.BLUE
)

# Complex style
style = Style(
    stroke_color=Colors.PRIMARY,
    gradient=(Colors.PRIMARY, Colors.SECONDARY),
    glow_color=Colors.WHITE.with_alpha(0.6),
    glow_radius=3.0
)
```