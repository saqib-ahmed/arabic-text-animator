# Styling Text

The Arabic Animations library provides comprehensive styling options through the `Style` class.

## Basic Styling

```python
from arabic_animations.core.color import Style, Color, Colors

# Basic black stroke
style = Style(
    stroke_color=Colors.BLACK,
    stroke_width=2.0
)

# Filled text
style = Style(
    stroke_color=Colors.BLACK,
    fill_color=Colors.BLUE,
    stroke_width=2.0
)
```

## Effects

### Shadows
```python
style = Style(
    stroke_color=Colors.BLACK,
    shadow_color=Color.from_hex("#00000066"),  # Semi-transparent black
    shadow_offset=(5, 5),
    shadow_blur=2.0
)
```

### Glow
```python
style = Style(
    stroke_color=Colors.BLUE,
    glow_color=Color.from_hex("#FFFFFF99"),
    glow_radius=3.0
)
```

### Gradients
```python
style = Style(
    stroke_color=Colors.PRIMARY,
    gradient=(Colors.PRIMARY, Colors.SECONDARY),
    gradient_direction=(0, 50)  # Vertical gradient over 50 pixels
)
```

## Predefined Styles

### Golden Title
```python
title_style = Style(
    stroke_color=Color.from_hex("#B8860B"),
    fill_color=Color.from_hex("#FFD700"),
    stroke_width=3.0,
    shadow_color=Color.from_hex("#00000066"),
    shadow_offset=(5, 5)
)
```

### Neon Text
```python
neon_style = Style(
    stroke_color=Colors.CYAN,
    glow_color=Colors.CYAN.with_alpha(0.6),
    glow_radius=5.0,
    stroke_width=2.0
)
```