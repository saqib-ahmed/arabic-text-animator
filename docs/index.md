# Arabic Text Animator

Welcome to Arabic Text Animator, a Python library for creating beautiful Arabic text writing animations.

## Features

- 🎨 Create smooth writing animations for Arabic text
- 🔠 Support for RTL text rendering
- 📐 Flexible positioning and layout system
- 🎯 Easy-to-use API
- 🎬 Export to various video formats
- 🖥️ Live preview during development
- ⚙️ Command-line interface with preview and render options

## Quick Links

- 📚 [Getting Started](getting-started/index.md)
- 📖 [User Guide](user-guide/index.md)
- 🔍 [API Reference](api-reference/index.md)
- 💡 [Examples](examples/index.md)

## Installation

```bash
pip install arabic-text-animator
```

## Basic Usage

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

## Command Line Usage

```bash
# Preview animation
ata render my_animation.py --preview

# Render to video
ata render my_animation.py --output my_animation.mp4
```

## Contributing

We welcome contributions! Check out our [GitHub repository](https://github.com/saqib-ahmed/arabic-text-animator) for:

- Source code
- Issue tracking
- Feature requests
- Pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/saqib-ahmed/arabic-text-animator/blob/main/LICENSE) file for details.