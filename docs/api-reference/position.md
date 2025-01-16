# Position

::: arabic_animations.core.position.Position
    handler: python
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

::: arabic_animations.core.position.Padding
    handler: python
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

## Usage Examples

### Using Positions
```python
from arabic_animations.core.position import Position, Padding

# Center position
text = Text("Hello", position=Position.CENTER)

# Top with padding
text = Text(
    "Hello",
    position=Position.TOP,
    padding=Padding(top=50)
)

# Custom padding
text = Text(
    "Hello",
    position=Position.TOP_RIGHT,
    padding=Padding(top=20, right=30)
)
```

### Padding Helpers
```python
# All sides equal
padding = Padding.all(20)

# Horizontal padding
padding = Padding.horizontal(50)

# Vertical padding
padding = Padding.vertical(30)
```