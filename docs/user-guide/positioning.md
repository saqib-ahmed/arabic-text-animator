# Positioning System

The Arabic Animations library provides a flexible positioning system for placing text elements on the screen.

## Position Types

The following position types are available through the `Position` enum:

- `Position.TOP`: Center-aligned at the top
- `Position.BOTTOM`: Center-aligned at the bottom
- `Position.LEFT`: Left-aligned at vertical center
- `Position.RIGHT`: Right-aligned at vertical center
- `Position.CENTER`: Centered both horizontally and vertically
- `Position.TOP_LEFT`: Aligned to top-left corner
- `Position.TOP_RIGHT`: Aligned to top-right corner
- `Position.BOTTOM_LEFT`: Aligned to bottom-left corner
- `Position.BOTTOM_RIGHT`: Aligned to bottom-right corner

## Padding

The `Padding` class allows you to add space around text elements:

```python
# Add padding to all sides
padding = Padding.all(20)

# Add horizontal padding only
padding = Padding.horizontal(50)

# Add vertical padding only
padding = Padding.vertical(30)

# Custom padding for each side
padding = Padding(top=20, right=40, bottom=20, left=40)
```

## Examples

### Basic Positioning

```python
text = Text(
    "Hello",
    position=Position.TOP,
    padding=Padding(top=50)
)
```

### Complex Layout

```python
title = Text(
    "Main Title",
    position=Position.TOP,
    padding=Padding(top=50)
)

subtitle = Text(
    "Subtitle",
    position=Position.CENTER
)

footer = Text(
    "Footer",
    position=Position.BOTTOM,
    padding=Padding(bottom=30)
)
```