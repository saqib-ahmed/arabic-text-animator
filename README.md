# Arabic Animations

A Python library for creating Arabic text writing animations, similar to Manim but specialized for Arabic calligraphy and text animations.

## Features

* Create smooth writing animations for Arabic text
* Support for RTL text rendering
* Live preview during development
* Export to MP4 video files
* Customizable text properties (font, size, color, stroke width)
* Multiple text elements with different timings
* Command-line interface with preview and render options

## Quick Start

### Prerequisites

#### macOS
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install system dependencies
brew install cairo pango pygobject3 pkg-config fontconfig
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install -y \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    libgirepository1.0-dev
```

#### Windows
Windows support is currently experimental. We recommend using WSL2 with Ubuntu for the best experience.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/saqib-ahmed/arabic-text-animator.git
cd arabic-text-animator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

### Basic Example

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

### Running Animations

```bash
# Live preview during development
arabic-animate render my_animation.py --preview

# Render to video file
arabic-animate render my_animation.py --output video.mp4
```

## Documentation

For detailed documentation including:
- Complete installation instructions
- API reference
- Advanced examples
- Styling guide
- Animation techniques
- Troubleshooting

Visit our [documentation site](https://saqib-ahmed.github.io/arabic-text-animator/).

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (when available)
5. Submit a pull request

## License

MIT License

## Acknowledgments

* Cairo Graphics Library
* Pango Text Layout Engine
* OpenCV for video output
