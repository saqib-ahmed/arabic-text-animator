# Text

::: arabic_animations.core.text.Text
    handler: python
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

## Usage Examples

### Basic Text Creation
```python
from arabic_animations.core.text import Text
from arabic_animations.core.position import Position
from arabic_animations.core.color import Style, Colors

# Simple text
text = Text("Hello")

# Positioned text
text = Text(
    "Hello",
    position=Position.CENTER,
    font_name="Arial",
    font_size=72
)

# Styled text
text = Text(
    "Hello",
    style=Style(
        stroke_color=Colors.BLACK,
        fill_color=Colors.BLUE,
        stroke_width=2.0
    )
)
```

### Font Management
```python
# List available fonts
Text.list_available_fonts()
```