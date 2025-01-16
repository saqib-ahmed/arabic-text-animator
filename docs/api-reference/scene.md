# Scene

::: arabic_animations.core.scene.Scene
    handler: python
    options:
      show_root_heading: true
      show_source: true
      heading_level: 2

## Usage Examples

### Basic Scene Setup
```python
from arabic_animations.core.scene import Scene

# Create a scene with default settings (1920x1080, 60fps)
scene = Scene()

# Create a scene with custom settings
scene = Scene(
    width=1280,
    height=720,
    fps=30
)
```

### Adding Objects
```python
# Add a single object
scene.add(text)

# Add multiple objects in parallel
scene.add(text1, text2, serial=False)

# Add multiple objects serially
scene.add(text1, text2, serial=True)
```

### Scene Background
```python
from arabic_animations.core.color import Colors

# Set scene background color
scene.background_color = Colors.PAPER_CREAM
```