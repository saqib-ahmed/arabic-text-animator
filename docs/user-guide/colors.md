# Colors and Color Management

## Color Formats

The `Color` class supports multiple color formats:

### RGB (0-1 range)
```python
color = Color.from_rgb(1.0, 0.0, 0.0)  # Red
```

### RGB (0-255 range)
```python
color = Color.from_rgb255(255, 0, 0)  # Red
```

### Hexadecimal
```python
color = Color.from_hex("#FF0000")  # Red
color = Color.from_hex("#FF0000FF")  # Red with alpha
```

### HSL (Hue, Saturation, Lightness)
```python
color = Color.from_hsl(0, 1.0, 0.5)  # Red
```

### HSV (Hue, Saturation, Value)
```python
color = Color.from_hsv(0, 1.0, 1.0)  # Red
```

## Predefined Colors

### Basic Colors
```python
Colors.WHITE
Colors.BLACK
Colors.RED
Colors.GREEN
Colors.BLUE
```

### Extended Colors
```python
Colors.TRANSPARENT
Colors.GRAY
Colors.YELLOW
Colors.CYAN
Colors.MAGENTA
```

### UI Colors
```python
Colors.PRIMARY
Colors.SECONDARY
Colors.SUCCESS
Colors.WARNING
Colors.DANGER
```

### Paper Colors
```python
Colors.PAPER_WHITE
Colors.PAPER_CREAM
Colors.PAPER_SEPIA
```

## Color Manipulation

### Alpha Channel
```python
semi_transparent = color.with_alpha(0.5)
```

### Lightness
```python
lighter = color.lighten(0.2)
darker = color.darken(0.2)
```

## Converting Between Formats
```python
color = Color.from_hex("#FF0000")

# Get different formats
rgb = color.to_rgb()  # (1.0, 0.0, 0.0, 1.0)
rgb255 = color.to_rgb255()  # (255, 0, 0, 1.0)
hex_str = color.to_hex()  # "#FF0000"
hsl = color.to_hsl()  # (0.0, 1.0, 0.5, 1.0)
hsv = color.to_hsv()  # (0.0, 1.0, 1.0, 1.0)
```